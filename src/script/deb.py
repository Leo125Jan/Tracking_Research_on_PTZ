import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

plt.rcParams.update({'figure.max_open_warning': 0})

def readData():

	Data = []

	filename = "D:/上課資料/IME/實驗室研究/Paper/Coverage Control/Tracking_Research_on_PTZ-master/src/Data_0.csv"

	with open(filename, "r", encoding='UTF8', newline='') as f:

		reader = csv.reader(f)
		
		for mem in reader:
			
			Data.append(float(mem[0]))

	return Data

def animate(i):

	Data = readData()
	x_0, y_0 = np.ndarray.tolist(np.arange(0, len(Data), 1)), Data

	plt.cla()
	plt.tight_layout()
	plt.plot(x_0, y_0)

if __name__ == "__main__":

	# animate(1)
	# ani = animation.FuncAnimation(plt.gcf(), animate, interval = 30)
	# plt.show()
	
	# ani.save("Agent.gif", dpi = 300, fps = 30, writer = "gif")

	a = np.array([3,6,6])
	b = a == 6
	print(b)
	print(all(b))
