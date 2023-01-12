import numpy as np
from Voronoi2D import Voronoi2D

if __name__ == "__main__":

	map_size = (20, 20)
	grid_size = (0.1, 0.1)

	cameras = [];
	camera0 = { 'id'            :  0,
	            'position'      :  np.array([0,0]),
	            'perspective'   :  np.array([1,1]),
	            'AngleofView'   :  10,
	            'range_limit'   :  3,
	            'lambda'        :  2,
	            'color'         : (200, 0, 0)}

	cameras.append(camera0)
	ptz = Voronoi2D.PTZcamera(camera0, map_size, grid_size)

	size = (np.array(map_size) / np.array(grid_size)).astype(np.int64)
	event = np.zeros((size[0], size[1]))

	target1 = [[(20, 20), 1e-10, 1e-10]]
	event1 = event_density(event, target1, grid_size)
	event_plt1 = ((event1 - event1.min()) * (1/(event1.max() - event1.min()) * 255)).astype('uint8')

	voronoi = Voronoi2D(map_size, grid_size, len(cameras), cameras, event1, event_plt1, target1)

	Done = False

	while not Done:

		for op in pygame.event.get():

			if op.type == pygame.QUIT:

				Done = True

			voronoi.Update()

	pygame.quit()