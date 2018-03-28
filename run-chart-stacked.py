import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import ast
import numpy as np

f = open("output.txt", "r")
lines = list(f)

hour = lines[0]
voice = lines[1]
video = lines[2]
high = lines[3]
medium = lines[4]
low = lines[5]

hour = ast.literal_eval(hour)
voice = ast.literal_eval(voice)
video = ast.literal_eval(video)
high = ast.literal_eval(high)
medium = ast.literal_eval(medium)
low = ast.literal_eval(low)

voice2 = np.array(voice)
video2 = np.array(video)
high2 = np.array(high)
medium2 = np.array(medium)
low2 = np.array(low)

voice = voice2+video2+high2+medium2+low2
video = video2+high2+medium2+low2
high = high2+medium2+low2
medium = medium2+low2
low = low2

plt.figure(figsize=(20,10))

# convert list of strings to list of integers
xn = range(len(hour))
# use original strings in position of integers
plt.xticks(xn, hour)

# add grid
plt.grid()
plt.title("City West - Eircom NGN - Stacked")

# draw plot
plt.plot(xn, voice, label="Voice", color="red")
plt.plot(xn, video, label="Video", color="orange")
plt.plot(xn, high, label="High", color="blue")
plt.plot(xn, medium, label="Medium", color="skyblue")
plt.plot(xn, low, label="Low", color="purple")

plt.fill_between(xn, video, voice, color='red')
plt.fill_between(xn, high, video, color='orange')
plt.fill_between(xn, medium, high, color='blue')
plt.fill_between(xn, low, medium, color='skyblue')
plt.fill_between(xn, 0, low, color='purple')

# rotate x ticks verticaly
plt.xticks(xn, hour, rotation='vertical')

# add legend, set to position center below, outside of chart, 2 columns, small fontsize
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize="small")

# save to file, legend inside of the picture
plt.savefig('chart-stacked.png', bbox_inches="tight")
