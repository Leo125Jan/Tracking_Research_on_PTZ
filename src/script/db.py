import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

plt.rcParams.update({'figure.max_open_warning': 0})

# Format plot
fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize = (9, 6.75))

def init():

	ax0.clear()
	ax1.clear()
	ax2.clear()

def readData():

	Data = []

	filename = "D:/Leo/IME/Paper Study/Coverage Control/Tracking_Research_on_PTZ-master/src/"
	files = Path(filename).glob("*.csv")

	for file in files:

		data_ = []

		with open(file, "r", encoding='UTF8', newline='') as f:

			reader = csv.reader(f)
			
			for mem in reader:
				
				data_.append(float(mem[0]))

		Data.append(data_)

	return Data

def animate(i):

	Data = readData()
	
	for (mem, i) in zip(Data, range(np.shape(Data)[0])):

		globals()["x_" + str(i)] = np.ndarray.tolist(np.arange(0, len(mem), 1))
		globals()["y_" + str(i)] = mem

	init()

	if y_0 == []:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax0.plot([], [], color = "r", label = lables)
		ax0.legend(loc = "upper right")
	elif (y_0[-1] > 5060):

		lables = "Coverage Mode: 1-3" + "\n" + "Quality: " + str(np.round(y_0[-1], 5))
		ax0.plot(x_0, y_0, color = "r", label = lables)
		ax0.legend(loc = "upper right")
	elif (y_0[-1] <= 5060 and y_0[-1] > 3300):

		lables = "Coverage Mode: 1-2" + "\n" + "Quality: " + str(np.round(y_0[-1], 5))
		ax0.plot(x_0, y_0, color = "r", label = lables)
		ax0.legend(loc = "upper right")
	elif (y_0[-1] <= 3300 and y_0[-1] > 0):

		lables = "Coverage Mode: 1-1" + "\n" + "Quality: " + str(np.round(y_0[-1], 5))
		ax0.plot(x_0, y_0, color = "r", label = lables)
		ax0.legend(loc = "upper right")
	else:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax0.plot(x_0, y_0, color = "r", label = lables)
		ax0.legend(loc = "upper right")

	ax0.set_title('Coverage Quality of Agent 0 (Red)')
	ax0.set_xlabel("Instant")
	ax0.set_ylabel("Quality")
	ax0.set_ylim((0, 10000))

	if y_1 == []:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax1.plot([], [], color = "g", label = lables)
		ax1.legend(loc = "upper right")
	elif (y_1[-1] > 5060):

		lables = "Coverage Mode: 1-3" + "\n" + "Quality: " + str(np.round(y_1[-1], 5))
		ax1.plot(x_1, y_1, color = "g", label = lables)
		ax1.legend(loc = "upper right")
	elif (y_1[-1] <= 5060 and y_1[-1] > 3300):

		lables = "Coverage Mode: 1-2" + "\n" + "Quality: " + str(np.round(y_1[-1], 5))
		ax1.plot(x_1, y_1, color = "g", label = lables)
		ax1.legend(loc = "upper right")
	elif (y_1[-1] <= 3300 and y_1[-1] > 0):

		lables = "Coverage Mode: 1-1" + "\n" + "Quality: " + str(np.round(y_1[-1], 5))
		ax1.plot(x_1, y_1, color = "g", label = lables)
		ax1.legend(loc = "upper right")
	else:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax1.plot(x_1, y_1, color = "g", label = lables)
		ax1.legend(loc = "upper right")

	ax1.set_title('Coverage Quality of Agent 1 (Green)')
	ax1.set_xlabel("Instant")
	ax1.set_ylabel("Quality")
	ax1.set_ylim((0, 10000))

	if y_2 == []:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax2.plot([], [], color = "b", label = lables)
		ax2.legend(loc = "upper right")
	elif (y_2[-1] > 5060):

		lables = "Coverage Mode: 1-3" + "\n" + "Quality: " + str(np.round(y_2[-1], 5))
		ax2.plot(x_2, y_2, color = "b", label = lables)
		ax2.legend(loc = "upper right")
	elif (y_2[-1] <= 5060 and y_2[-1] > 3300):

		lables = "Coverage Mode: 1-2" + "\n" + "Quality: " + str(np.round(y_2[-1], 5))
		ax2.plot(x_2, y_2, color = "b", label = lables)
		ax2.legend(loc = "upper right")
	elif (y_2[-1] <= 3300 and y_2[-1] > 0):

		lables = "Coverage Mode: 1-1" + "\n" + "Quality: " + str(np.round(y_2[-1], 5))
		ax2.plot(x_2, y_2, color = "b", label = lables)
		ax2.legend(loc = "upper right")
	else:

		lables = "Coverage Mode: None" + "\n" + "Quality: " + str(0)
		ax2.plot(x_2, y_2, color = "b", label = lables)
		ax2.legend(loc = "upper right")

	ax2.set_title('Coverage Quality of Agent 2 (Blue)')
	ax2.set_xlabel("Instant")
	ax2.set_ylabel("Quality")
	ax2.set_ylim((0, 10000))

	plt.tight_layout()

if __name__ == "__main__":

	# animate(1)
	ani = animation.FuncAnimation(plt.gcf(), animate, \
									init_func = init, interval = 30, blit = False)

	# ani.save("Agent.gif", dpi = 300, fps = 30, writer = "gif")
	plt.show()