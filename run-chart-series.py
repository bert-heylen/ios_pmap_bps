import ast
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

# set figure size
plt.figure(figsize=(20,10))

# convert list of strings to list of integers
xn = range(len(hour))
# use original strings in position of integers
plt.xticks(xn, hour)

# add grid
plt.grid()

plt.title("City West - Eircom NGN - Series")

# draw plot
plt.plot(xn, voice, label="Voice", color="red")
plt.plot(xn, video, label="Video", color="orange")
plt.plot(xn, high, label="High", color="blue")
plt.plot(xn, medium, label="Medium", color="skyblue")
plt.plot(xn, low, label="Low", color="purple")

# rotate x ticks verticaly
plt.xticks(xn, hour, rotation='vertical')

# add legend, set to position center below, outside of chart, 2 columns, small fontsize
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize="small")

# save to file, legend inside of the picture
plt.savefig('chart-series.png', bbox_inches="tight")
