import pygame
import numpy as np
from math import cos, acos, sqrt, exp, sin
from time import sleep, time
from scipy import ndimage, sparse
from cvxopt import matrix, solvers
import osqp
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import random
from shapely.plotting import plot_polygon, plot_points
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

class Voronoi2D():
    def __init__(self, map_size, grid_size, camera_num, \
        camera_prop, event, event_plt, target):
        self.event_plt = event_plt
        self.map = self.Map(map_size, grid_size)
        self.camera_num = camera_num
        self.size = (int(map_size[0]/grid_size[0]), int(map_size[1]/grid_size[1]))
        self.PTZs = []

        for i in range(0, camera_num):
            ptz = self.PTZcamera(camera_prop[i], map_size, grid_size, target)
            self.PTZs.append(ptz)

        self.event = event
        self.ptz_tg = target
        self.chk_l = len(target)
        self.target_s = target

    def Update(self, step = 0.5, event_plt = None, target = []):

        if len(target) > 0 :

            self.event_plt = event_plt
            self.true_ep = event_plt
            self.true_tg = target

            for i in range(self.camera_num):

                self.PTZs[i].targets = [self.target_s[i]]

        for ptz in self.PTZs:
            ptz.voronoi = []
            ptz.FoV = np.zeros(self.size)
            ptz.ComputeFoV()

        for i in range(self.camera_num):
            self.PTZs[i].UpdateVoronoi([self.PTZs[j].FoV \
                for j in range(len(self.PTZs)) if j != i])

        for i in range(self.camera_num):
                self.PTZs[i].targets = target

        sum = 0
        area = 0
        cnt = [0 for i in range(len(target))]
        map_plt = np.zeros((self.map.size)) - 1
        for i in range(self.camera_num):
            map_plt = self.PTZs[i].map_plt + map_plt
            sum += self.PTZs[i].quality
            area += len(self.PTZs[i].voronoi[0])
            if self.PTZs[i].target_assigned != -1:
                cnt[self.PTZs[i].target_assigned] += 1
        # print("Covered Quality: ",sum)
        # print("Total Covered Area: ", area)        

        self.map.Update(map_plt, self.PTZs, self.true_ep, self.true_tg, self.target_s)

        self.target_s = []

        for i in range(self.camera_num):
            self.ptz_tg, self.chk_l = self.PTZs[i].UpdateState([self.PTZs[j].pos \
                for j in range(self.camera_num) if j != i], step, self.PTZs, self.true_tg)

            if self.chk_l != 3:

                self.target_s.extend(self.ptz_tg)
            else:
                self.target_s.extend(self.ptz_tg)

        # self.map.Update(map_plt, self.PTZs, self.true_ep, self.true_tg, self.ptz_tg)

        # Calculatin Switch Quality
        # if len(target) > 0 :

        #     self.event_plt = event_plt
        #     self.true_ep = event_plt

        #     for i in range(self.camera_num):

        #         self.PTZs[i].targets = [target[self.PTZs[i].switch_assigned]]

        # for ptz in self.PTZs:
        #     ptz.voronoi = []
        #     ptz.FoV = np.zeros(self.size)
        #     ptz.ComputeFoV()

        # for i in range(self.camera_num):
        #     self.PTZs[i].UpdateVoronoi([self.PTZs[j].FoV \
        #         for j in range(len(self.PTZs)) if j != i])

        # for i in range(self.camera_num):
            
        #     print("i: " + str(i) + ", Best One Quality: " + str(self.PTZs[i].quality))

        return cnt

    def norm(self, arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]**2
        return sqrt(sum)

    def event_density(self, event, target, grid_size):

        x = np.arange(event.shape[0])*grid_size[0]
        for y_map in range(0, event.shape[1]):
            y = y_map*grid_size[1]
            density = 0
            for i in range(len(target)):
                density += target[i][2]*np.exp(-target[i][1]*np.linalg.norm(np.array([x,y], dtype=object)\
                                -np.array((target[i][0][1],target[i][0][0]))))
            event[:][y_map] = density

        return 0 + event
    
    class PTZcamera():
        def __init__(self, properties, map_size, grid_size, targets, \
                        Kv = 25, Kvo = 1, Ka = 1, Kao = 0, Kp = 5):
            self.grid_size = grid_size
            self.map_size = map_size
            self.size = (int(map_size[0]/grid_size[0]), int(map_size[1]/grid_size[1]))
            self.id = properties['id']
            self.pos = properties['position']
            self.perspective = properties['perspective']/self.norm(properties['perspective'])
            self.alpha = properties['AngleofView']/180*np.pi
            self.R = properties['range_limit']
            self.lamb = properties['lambda']
            self.color = properties['color']
            self.translation_force = 0  # dynamics of positional changes
            self.perspective_force = 0  # dynamics of changing perspective direction
            self.alpha_dot = 0          # dynamics of zoom-in level
            self.stage = 1              # 1: Free player 2: Occupied Player 3: Cooperative player
            self.targets = targets
            self.target_assigned = -1
            self.switch_assigned = -1
            self.FoV = np.zeros(self.size)
            self.Kv = Kv                # control gain for perspective control law toward voronoi cell
            self.Kvo = Kvo              # control gain for perspective control law toward overlap cell
            self.Ka = Ka                # control gain for zoom level control stems from voronoi cell
            self.Kao = Kao              # control gain for zoom level control stems from overlap cell
            self.Kp = Kp                # control gain for positional change toward voronoi cell 
            self.event = np.zeros((self.size[0], self.size[1]))
            self.top = 0
            self.ltop = 0
            self.rtop = 0
            self.tar_oc = np.zeros(len(self.targets))
            self.r = 0
            self.center = 0
            self.last_x = 0
            self.last_y = 0
            self.last_t = 0
            self.cls_t = 0

        def UpdateState(self, neighbors, step, neighborhoods, true_tg):

            centroidal_forces, centroid = self.ComputeCentroidal(self.event)
            
            chk = self.Cluster_Formation()
            self.targets, chk_l = self.Cluster_Tracking(chk, neighborhoods)
            self.TargetAssignment(neighborhoods, centroid)

            event = np.zeros((size[0], size[1]))
        
            if self.target_assigned == -1:
                
                event1 = self.event_density(event, self.targets, grid_size)
            else:
                
                event1 = self.event_density(event, [self.targets[self.target_assigned]], grid_size)
                
            self.event = event1

            formation_force = self.FormationControl(neighbors, true_tg)
            control_input = self.CBF(centroidal_forces[0], formation_force, \
                                        centroidal_forces[1], stage = self.stage)
            
            self.pos += control_input[0]*step
            self.perspective += control_input[1]*step
            self.perspective /= self.norm(self.perspective)
            self.alpha = self.alpha + centroidal_forces[2]*step

            # print("Center Quality: " + str(self.quality) + "\n")

            return self.targets, chk_l

        def CBF(self, translational_force = 0, formation_force = 0, rotational_force = 0,\
                    coe = 0.8, stage = 1):

            if stage == 2:
                # td = np.asarray(self.targets[self.target_assigned][0]) - self.pos
                # td = td/self.norm(td)

                # ux = rotational_force[0]
                # uy = rotational_force[1]

                # # Define problem data
                # P = sparse.csc_matrix([[1, 0], [0, 1]])
                # q = np.array([-2*ux, -2*uy])
                # A = sparse.csc_matrix([[td[0], td[1]],[self.perspective[0], self.perspective[1]]])
                # l = np.array([cos(self.alpha) - td@self.perspective, 0])
                # u = np.array([0.1*np.pi, 0])
                # # Create an OSQP object
                # prob = osqp.OSQP()

                # # Setup workspace and change alpha parameter
                # prob.setup(P, q, A, l, u, alpha = 1, verbose=False)

                # # Solve problem
                # res = prob.solve()
                # ux = res.x[0]; uy = res.x[1]
                # cl = np.array([ux, uy])
                # n_p = (self.perspective+coe*cl)/self.norm(self.perspective+coe*cl)
                # rotational_force = cl
                # td = np.asarray(self.targets[self.target_assigned][0]) - self.pos
                # td = td/self.norm(td)
                # theta = acos(td@self.perspective)
                # rotational_force = theta*np.array([0.5, 0.5])

                res = translational_force + formation_force

                return [res, rotational_force]

            else:
                res = translational_force + formation_force
                return [res, rotational_force]

        def event_density(self, event, target, grid_size):

            x = np.arange(event.shape[0])*grid_size[0]
            for y_map in range(0, event.shape[1]):
                y = y_map*grid_size[1]
                density = 0
                for i in range(len(target)):
                    density += target[i][2]*np.exp(-target[i][1]*np.linalg.norm(np.array([x,y], dtype=object)\
                                    -np.array((target[i][0][1],target[i][0][0]))))
                event[:][y_map] = density

            return 0 + event

        def Cluster_Formation(self):

            checklist = np.zeros((len(self.targets), len(self.targets)))
            threshold = 2.3
            self.cls_t = 0

            for i in range(len(self.targets)):

                for j in range(len(self.targets)):

                    if j != i:

                        p1 = np.array([self.targets[i][0][0], self.targets[i][0][1]])
                        p2 = np.array([self.targets[j][0][0], self.targets[j][0][1]])

                        dist = self.norm(p1 - p2)

                        if dist <= threshold:

                            checklist[i][j] = 1
                            self.cls_t += 1
                        else:

                            checklist[i][j] = 0

            return checklist

        def Cluster_Tracking(self, chk, neighborhoods):

            count = 0
            targets = []
            nebi_chk = []

            for i in range(np.shape(chk)[0]):

                nonindex = np.nonzero(chk[i][:])[0]

                if i > 0:

                    for j in nonindex:

                        if j < i and i in np.nonzero(chk[j][:])[0]:

                            if self.id == 0:

                                pass
                        else:

                            c_x = 0.5*(self.targets[i][0][0] + self.targets[j][0][0])
                            c_y = 0.5*(self.targets[i][0][1] + self.targets[j][0][1])

                            targets.append([(c_x, c_y), 1, 10])

                elif i == 0:

                    for j in nonindex:
                    
                        c_x = 0.5*(self.targets[i][0][0] + self.targets[j][0][0])
                        c_y = 0.5*(self.targets[i][0][1] + self.targets[j][0][1])

                        targets.append([(c_x, c_y), 1, 10])

            x = 0
            y = 0
            score = np.inf

            for mem in neighborhoods:

                nebi_chk.append(mem.cls_t)

            if nebi_chk == [6, 0, 0] or nebi_chk == [6, 6, 0]:

                nebi_chk = np.array([6, 6, 6])
                nebi_chk = nebi_chk == 6
            else:
                nebi_chk = np.array(nebi_chk)
                nebi_chk = nebi_chk == 6

            if len(targets) == 3 and nebi_chk.all():

                for mem in self.targets:

                    x += mem[0][0]
                    y += mem[0][1]

                if (x == self.last_x and y == self.last_y) or (self.last_x == 0 and self.last_y == 0):

                    self.last_x = x
                    self.last_y = y
                    target_ = [[(x/3, y/3), 1, 10]]
                else:

                    target_ = [[(x/3, y/3), 1, 10]]
                    self.last_t = target_
            else:

                for mem in self.targets:

                    x += mem[0][0]
                    y += mem[0][1]

                target_ = [[(x/3, y/3), 1, 10]]

            cluster_quality = 0
            best_quality = 0
            score = np.inf
            switch_target = None
            self.switch_assigned = -1
            for_chk_one = []

            pt = [self.pos, self.ltop, self.top, self.rtop, self.pos]
            polygon = Polygon(pt)

            for (target, i) in zip(self.targets, range(0,len(self.targets))):
                
                gemos = Point(target[0])

                if polygon.is_valid and polygon.contains(gemos):

                    event = np.zeros((size[0], size[1]))
                    event1 = self.event_density(event, [target], self.grid_size)
                    event1 = np.transpose(event1)
                    cluster_quality += np.sum(self.FoV*event1)
            
            # print("Cluster Quality: " + str(cluster_quality))

            if len(targets) != 3 and nebi_chk.all() == False:

                if (cluster_quality <= 5060):

                    if len(targets) == 2:

                        for mem in targets:

                            p1 = np.array([mem[0][0], mem[0][1]])
                            p2 = np.array([self.pos[0], self.pos[1]])

                            dist = self.norm(p1 - p2)

                            if dist < score and dist > 0:

                                score = dist
                                target_ = [mem]

                    if len(targets) == 1:

                        for i in range(np.shape(chk)[0]):

                            temp = chk[i,:]

                            if (temp == 0).all():

                                for_chk_one.append(self.targets[i])
                                for_chk_one.extend(targets)
                                break

                        for mem in for_chk_one:

                                p1 = np.array([mem[0][0], mem[0][1]])
                                p2 = np.array([self.pos[0], self.pos[1]])

                                dist = self.norm(p1 - p2)

                                if dist < score and dist > 0:

                                    score = dist
                                    target_ = [mem]

                    event = np.zeros((size[0], size[1]))
                    event1 = self.event_density(event, target_, self.grid_size)
                    event1 = np.transpose(event1)
                    best_quality = np.sum(self.FoV*event1)

                    # print("Best One Quality: " + str(best_quality))

                score = np.inf
                if (cluster_quality < 3300) or len(targets) == 0:

                    for (target, i) in zip(self.targets, range(0,len(self.targets))):

                        p1 = np.array([target[0][0], target[0][1]])
                        p2 = np.array([self.pos[0], self.pos[1]])

                        dist = self.norm(p1 - p2)

                        if dist < score and dist > 0:

                            score = dist
                            switch_target = target

                    target_ = [switch_target]

                    event = np.zeros((size[0], size[1]))
                    event1 = self.event_density(event, [switch_target], self.grid_size)
                    event1 = np.transpose(event1)
                    best_quality = np.sum(self.FoV*event1)

                    # print("Best One Quality: " + str(best_quality))

            filename = "D:/Leo/IME/Paper Study/Coverage Control/Tracking_Research_on_PTZ-master/src/"
            filename += "Data_" + str(self.id) + ".csv"
            with open(filename, "a", encoding='UTF8', newline='') as f:

                row = [cluster_quality]
                writer = csv.writer(f)
                writer.writerow(row)

            return target_, len(targets)

        def TargetAssignment(self, neighborhoods, centroid):

            # range_max = 0.85*(self.lamb + 1)/(self.lamb)*self.R*cos(self.alpha)
            range_max = self.R*cos(self.alpha)

            if centroid is not None:

                range_local_best = (self.norm(np.asarray(centroid) - self.pos))
                r = range_max*range_local_best/(range_max+range_local_best)\
                            + range_local_best*range_max/(range_max+range_local_best)
                if self.stage == 1:
                    r = max(r, range_max - sqrt(1/(2*self.targets[self.target_assigned][1])))
            else:
                r = self.R*cos(self.alpha)

            tmp = 0
            for i in range(len(self.targets)):
                dist = self.norm(self.pos - np.asarray(self.targets[i][0]))
                if dist <= r and -dist <= tmp:
                    tmp = -dist
                    self.target_assigned = i
                    self.stage = 2

            self.r = r

            # print(self.id,"=>", self.target_assigned, "=>", self.stage, "\n")

        def FormationControl(self, neighbors, true_tg):
            # TO-DO after Chinese New Year
            # Consider which neighbor is sharing the same target and only use them to obtain formation force
            neighbor_force = np.array([0.,0.])
            for neighbor_pos in neighbors:
                neighbor_force += (self.pos - neighbor_pos)/(self.norm(self.pos - neighbor_pos))
            
            neighbor_norm = self.norm(neighbor_force)

            if self.stage == 2:

                target_force = (np.asarray(self.targets[self.target_assigned][0]) - self.pos)\
                                /(self.norm(np.asarray(self.targets[self.target_assigned][0])\
                                     - self.pos))

                target_norm = self.norm(target_force)

                center_force = (np.asarray(self.targets[self.target_assigned][0]) - self.pos)\
                                /(self.norm(np.asarray(self.targets[self.target_assigned][0])\
                                     - self.pos))

                formation_force = (target_force*(neighbor_norm/(target_norm+neighbor_norm))\
                                    + neighbor_force*(target_norm/(target_norm+neighbor_norm)))

                formation_force -= (center_force/self.norm(center_force))*(self.r - self.norm\
                             (self.pos - np.asarray(self.targets[self.target_assigned][0])))

                return formation_force

            else:
                formation_force = neighbor_force
                return formation_force

        def polygon_FOV(self):

            range_max = (self.lamb + 1)/(self.lamb)*self.R*cos(self.alpha)
            R = np.array([[np.cos(self.alpha), -np.sin(self.alpha)]
                        ,[np.sin(self.alpha), np.cos(self.alpha)]])

            self.top = self.pos + range_max*self.perspective;

            self.ltop = self.pos + range_max*np.reshape(R@np.reshape(self.perspective,(2,1)),(1,2));
            self.ltop = self.ltop[0]

            self.rtop = self.pos + range_max*np.reshape(np.linalg.inv(R)@np.reshape(self.perspective,(2,1)),(1,2));
            self.rtop = self.rtop[0]
        
        def ComputeCentroidal(self, event):
            translational_force = np.array([0.,0.])
            rotational_force = np.array([0.,0.]).reshape(2,1)
            zoom = 0
            centroid = None
            if len(self.voronoi[0]) > 0:
                mu_V = 0
                v_V_t = np.array([0, 0], dtype=np.float64)
                delta_V_t = 0
                x_center = 0
                y_center = 0

                # Control law for maximizing resolution and perspective quality
                for i in range(len(self.voronoi[0])):
                    x_map = self.voronoi[1][i]
                    y_map = self.voronoi[0][i]

                    x, y = x_map*self.grid_size[0], y_map*self.grid_size[1]
                    x_p = np.array([x,y]) - self.pos
                    norm = self.norm(x_p)
                    if norm == 0: continue
                    mu_V += ((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb)
                    v_V_t += ((x_p)/norm)*(cos(self.alpha) - \
                                    ( ( self.lamb*norm )/((self.lamb+1)*self.R)))*\
                                        ( (norm**self.lamb)/(self.R**self.lamb) )*event[x_map,y_map]
                    dist = (1 - (self.lamb*norm)/((self.lamb+1)*self.R))
                    dist = dist if dist >= 0 else 0
                    delta_V_t += (1 - (((x_p)@self.perspective.T))/norm)\
                                    *dist*((norm**self.lamb)/(self.R**self.lamb))\
                                        *event[x_map,y_map]
                    x_center += x*(((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb))
                    y_center += y*(((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb))
                
                v_V = v_V_t/mu_V
                delta_V = delta_V_t/mu_V
                delta_V = delta_V if delta_V > 0 else 1e-10
                alpha_v = acos(1-sqrt(delta_V))
                alpha_v = alpha_v if alpha_v > 5/180*np.pi else 5/180*np.pi
                
                centroid = np.array([x_center/mu_V, y_center/mu_V])
                translational_force += self.Kp*(self.norm(centroid - self.pos) - self.R*cos(self.alpha))\
                                                *self.perspective
                rotational_force += self.Kv*(np.eye(2) - np.dot(self.perspective[:,None],\
                                                self.perspective[None,:]))  @  (v_V.reshape(2,1))
                zoom += -self.Ka*(self.alpha - alpha_v)

            # control law for minimizing overlap area
            if len(self.overlap[0]) > 0:
                mu_V_o = 0
                v_V_t_o = np.array([0, 0], dtype=np.float64)
                delta_V_t_o = 0
                x_center_o = self.pos[0]
                y_center_o = self.pos[1]

                for i in range(len(self.overlap[0])):
                    x_map = self.overlap[1][i]
                    y_map = self.overlap[0][i]
                    x, y = x_map*self.grid_size[0], y_map*self.grid_size[1]
                    x_p = np.array([x,y]) - self.pos
                    norm = self.norm(x_p)
                    mu_V_o += ((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb)
                    v_V_t_o += ((x_p)/norm)*(cos(self.alpha) - \
                                    ( ( self.lamb*norm )/((self.lamb+1)*self.R)))*\
                                        ( (norm**self.lamb)/(self.R**self.lamb) )*event[x_map,y_map]
                    dist = (1 - (self.lamb*norm)/((self.lamb+1)*self.R))
                    dist = dist if dist >= 0 else 0
                    delta_V_t_o += (1 - (((x_p)@self.perspective.T))/norm)\
                                    *dist*((norm**self.lamb)/(self.R**self.lamb))\
                                        *event[x_map,y_map]
                    x_center_o += x*(((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb))
                    y_center_o += y*(((norm**self.lamb)*event[x_map,y_map] )/(self.R**self.lamb))

                v_V_o = v_V_t_o/mu_V_o
                delta_V_o = delta_V_t_o/mu_V_o
                delta_V_o = delta_V_o if delta_V_o > 0 else 1e-10
                alpha_v_o = acos(1-sqrt(delta_V_o))
                alpha_v_o = alpha_v_o if alpha_v_o > 5/180*np.pi else 5/180*np.pi

                rotational_force -= self.Kvo*(np.eye(2) - np.dot(self.perspective[:,None],\
                                                self.perspective[None,:]))@(v_V_o.reshape(2,1))
                zoom -= -self.Kao*(self.alpha - alpha_v_o)

            translational_force = translational_force if self.stage != 2 else 0
            return [translational_force, np.asarray([rotational_force[0][0], rotational_force[1][0]])\
                        , zoom], centroid

        def PerspectiveQuality(self, x, y):
            x_p = np.array([x,y], dtype=object) - self.pos
            return (np.matmul(x_p,self.perspective.transpose())/np.linalg.norm(x_p)\
                - np.cos(self.alpha))/(1 - np.cos(self.alpha))

        def ResolutionQuality(self, x, y):
            x_p = np.array([x, y], dtype=object) - self.pos
            return (((np.linalg.norm(x_p)**self.lamb)*(self.R*np.cos(self.alpha)\
                 - self.lamb*( np.linalg.norm(x_p) - self.R*np.cos(self.alpha)) ))\
                    /(self.R**(self.lamb+1)))    

        def ComputeFoV(self):
            range_max = (self.lamb + 1)/(self.lamb)*self.R
            quality_map = None
            for y_map in range(max(int((self.pos[1] - range_max)/self.grid_size[1]), 0),\
                                min(int((self.pos[1] + range_max)/self.grid_size[1]), self.size[1])):
                x_map = np.arange(max(int((self.pos[0] - range_max)/self.grid_size[0]), 0),\
                                min(int((self.pos[0] + range_max)/self.grid_size[0]), self.size[0]))
                q_per = self.PerspectiveQuality(x_map*self.grid_size[0], y_map*self.grid_size[1])
                q_res = self.ResolutionQuality(x_map*self.grid_size[0], y_map*self.grid_size[1])
                quality = np.where((q_per > 0) & (q_res > 0), q_per*q_res, 0)
                if quality_map is None:
                    quality_map = quality
                else:
                    quality_map = np.vstack((quality_map, quality))

            self.FoV[max(int((self.pos[1] - range_max)/self.grid_size[1]), 0):\
                        min(int((self.pos[1] + range_max)/self.grid_size[1]), self.size[0]),\
                            max(int((self.pos[0] - range_max)/self.grid_size[0]), 0):\
                                min(int((self.pos[0] + range_max)/self.grid_size[0]), self.size[0])]\
                                    = quality_map

            self.polygon_FOV()

        def UpdateVoronoi(self, FoVs):
            if self.stage == 1:
                self.event = self.event_density(self.event, self.targets, self.grid_size) 
                self.event_plt = ((self.event - self.event.min()) * (1/(self.event.max() - self.event.min()) * 255)).astype('uint8')
            elif self.stage == 2:
                self.event = self.event_density(self.event, [self.targets[self.target_assigned]], self.grid_size) 
                self.event_plt = ((self.event - self.event.min()) * (1/(self.event.max() - self.event.min()) * 255)).astype('uint8')
            
            quality_map = self.FoV

            for FoV in FoVs:
                quality_map = np.where((quality_map > FoV), quality_map, 0)

            # self.quality = np.sum(quality_map*self.event)
            # self.voronoi = np.array(np.where((quality_map != 0) & (self.FoV != 0)))
            self.voronoi = np.array(np.where((self.FoV != 0)))
            self.quality = np.sum(self.FoV*self.event)
            self.overlap = np.array(np.where((quality_map == 0) & (self.FoV != 0)))
            self.map_plt = np.array(np.where(quality_map != 0, self.id + 1, 0))

        def norm(self, arr):
            sum = 0
            for i in range(len(arr)):
                sum += arr[i]**2
            return sqrt(sum)

    class Map():
        def __init__(self, map_size, grid_size):
            self.size = (np.array(map_size) / np.array(grid_size)).astype(np.int64)
            self.grid_size = grid_size
            self.window_size = np.array(self.size)*4
            self.display = pygame.display.set_mode(self.window_size)
            self.display.fill((0,0,0))
            self.blockSize = int(self.window_size[0]/self.size[0]) #Set the size of the grid block
            for x in range(0, self.window_size[0], self.blockSize):
                for y in range(0, self.window_size[1], self.blockSize):
                    rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                    pygame.draw.rect(self.display, (125,125,125), rect, 1)
            pygame.display.update()

        def Update(self, map_plt, cameras, event, targets, ptz_tg):
            x_map = 0
            for x in range(0, self.window_size[0], self.blockSize):
                y_map = 0
                for y in range(0, self.window_size[1], self.blockSize):
                    dense = event[x_map][y_map]
                    w = 0.6
                    id = int(map_plt[y_map][x_map])
                    if id == -1:
                        gray = (1-w)*125 + w*dense
                        rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                        pygame.draw.rect(self.display, (gray, gray, gray), rect, 0)
                    else:
                        color = ((1-w)*cameras[id].color[0] + w*dense, \
                                    (1-w)*cameras[id].color[1] + w*dense,\
                                        (1-w)*cameras[id].color[2] + w*dense)
                        rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                        pygame.draw.rect(self.display, color, rect, 0)
                    y_map += 1
                x_map += 1 

            for camera in cameras:
                color = (camera.color[0], camera.color[1], camera.color[2])
                center = camera.pos/self.grid_size*self.blockSize

                R = camera.R*cos(camera.alpha)/self.grid_size[0]*self.blockSize
                pygame.draw.line(self.display, color, center, center + camera.perspective*R, 3)
                pygame.draw.circle(self.display, color, camera.pos/self.grid_size*self.blockSize, 10)

            for camera in cameras:

                color = (camera.color[0]*0.5, camera.color[1]*0.5, camera.color[2]*0.5)
                pygame.draw.polygon(self.display, color, [camera.pos/self.grid_size*self.blockSize, \
                                                            camera.ltop/self.grid_size*self.blockSize, \
                                                            camera.top/self.grid_size*self.blockSize, \
                                                            camera.rtop/self.grid_size*self.blockSize], 2)
            for target in targets:
                pygame.draw.circle(self.display, (0,0,0), np.asarray(target[0])/self.grid_size\
                                    *self.blockSize, 6)

            for tar in ptz_tg:

                pygame.draw.circle(self.display, (100,100,100), np.asarray(tar[0])/self.grid_size\
                                    *self.blockSize, 3)

            pygame.draw.rect(self.display, (0, 0, 0), (0, 0, map_size[0]/grid_size[0]*self.blockSize, \
                                                        map_size[1]/grid_size[1]*self.blockSize), width = 3)
            pygame.display.flip()

def norm(arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]**2
        return sqrt(sum)

def event_density(event, target, grid_size):
    x = np.arange(event.shape[0])*grid_size[0]
    for y_map in range(0, event.shape[1]):
        y = y_map*grid_size[1]
        density = 0
        for i in range(len(target)):
            density += target[i][2]*np.exp(-target[i][1]*np.linalg.norm(np.array([x,y], dtype=object)\
                            -np.array((target[i][0][1],target[i][0][0]))))
        event[:][y_map] = density

    return 0 + event 

def dynamicTarget(x, y):
    dx = np.random.uniform(-0.5, 0.5, 1)
    dy = np.random.uniform(-0.5, 0.5, 1)

    return (x, y)#(np.round(float(np.clip(dx/2 + x, 0, 24)),1), np.round(float(np.clip(dy/2 + y, 0, 24)),1))

if __name__ == "__main__":
    pygame.init()

    map_size = (25, 25)    
    grid_size = (0.1, 0.1)

    cameras = []
    camera0 = { 'id'            :  0,
                'position'      :  np.array([1., 8.]),
                'perspective'   :  np.array([0.9,1]),
                'AngleofView'   :  20,
                'range_limit'   :  5,
                'lambda'        :  2,
                'color'         : (200, 0, 0)}

    cameras.append(camera0)

    camera1 = { 'id'            :  1,
                'position'      :  np.array([1., 1.]),
                'perspective'   :  np.array([0.7,1]),
                'AngleofView'   :  20,
                'range_limit'   :  5,
                'lambda'        :  2,
                'color'         : (0, 200, 0)}

    cameras.append(camera1)

    camera2 = { 'id'            :  2,
                'position'      :  np.array([8., 1.]),
                'perspective'   :  np.array([0.7,1]),
                'AngleofView'   :  20,
                'range_limit'   :  5,
                'lambda'        :  2,
                'color'         : (0, 0, 200)}

    cameras.append(camera2)

    size = (np.array(map_size) / np.array(grid_size)).astype(np.int64)
    event = np.zeros((size[0], size[1]))

    target = [[(6.5, 19), 1, 10], [(6.0, 18.0), 1, 10], [(7.0, 18.0), 1, 10]] #target, certainty
    event1 = event_density(event, target, grid_size)    
    event_plt1 = ((event1 - event1.min()) * (1/(event1.max() - event1.min()) * 255)).astype('uint8')

    voronoi = Voronoi2D(map_size, grid_size, len(cameras), cameras, np.ones(size), np.ones(size), target)

    Done = False
    last = time()
    cnt = [0 for i in range(len(target))]

    for i in range(len(cameras)):

        filename = "D:/Leo/IME/Paper Study/Coverage Control/Tracking_Research_on_PTZ-master/src/"
        filename += "Data_" + str(i) + ".csv"

        f = open(filename, "w+")
        f.close()

    while not Done:

        for op in pygame.event.get():

            if op.type == pygame.QUIT:
                Done = True

        if np.round(time() - last, 2) > 40.00 and np.round(time() - last, 2) < 80.00:

            target[0][0] = (target[0][0][0] + 0.00, target[0][0][1] + 0.01)
            target[1][0] = (target[1][0][0] - 0.01, target[1][0][1] - 0.02)
            target[2][0] = (target[2][0][0] + 0.03, target[2][0][1] - 0.04)
            # target[0][0] = (10, 14)
            # target[1][0] = (7, 7)
            # target[2][0] = (13, 6)

            sleep(0.001)
        elif np.round(time() - last, 2) > 70.00 and np.round(time() - last, 2) < 130:

            target[0][0] = (target[0][0][0] + 0.06, target[0][0][1] - 0.01)
            target[1][0] = (target[1][0][0] + 0.008, target[1][0][1] - 0.05)
            target[2][0] = (target[2][0][0] + 0.03, target[2][0][1] - 0.03)

            sleep(0.001)

        elif np.round(time() - last, 2) > 130.00 and np.round(time() - last, 2) < 180:

            target[0][0] = (target[0][0][0] + 0.008, target[0][0][1] - 0.07)
            target[1][0] = (target[1][0][0] + 0.065, target[1][0][1] - 0.008)
            target[2][0] = (target[2][0][0] + 0.015, target[2][0][1] - 0.015)

            sleep(0.001)

        event = np.zeros((size[0], size[1]))

        target = [[dynamicTarget(target[0][0][0], target[0][0][1]), 1, target[0][2]],
                   [dynamicTarget(target[1][0][0], target[1][0][1]), 1, target[1][2]],
                        [dynamicTarget(target[2][0][0], target[2][0][1]), 1, target[2][2]]]
        event1 = event_density(event, target, grid_size) 
        event_plt1 = ((event - event1.min()) * (1/(event1.max() - event1.min()) * 255)).astype('uint8')
        cnt = voronoi.Update(event_plt=event_plt1, target=target, step = 0.1)
    
    pygame.quit()