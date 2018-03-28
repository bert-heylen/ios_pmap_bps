from netmiko import ConnectHandler
import time
import datetime
import os
import os.path
import sys

voice = []
video = []
high = []
medium = []
low = []
now = []

if os.path.exists("./output.txt"):
  os.remove("./output.txt")

while(True):
  device = ConnectHandler(device_type='cisco_ios', ip=sys.argv[1], username=sys.argv[2], password=sys.argv[3])

  # get command output
  output = device.send_command('show policy-map interface gi1/5.52 | i offered')

  # split output into a list based on newline
  rates = output.split('\n')

  # get bps from all classes and divide to get mbps, and append to list
  voice.append(int(rates[0].split(' ')[4])/1024/1024)
  video.append(int(rates[1].split(' ')[4])/1024/1024)
  high.append(int(rates[2].split(' ')[4])/1024/1024)
  medium.append(int(rates[3].split(' ')[4])/1024/1024)
  low.append(int(rates[4].split(' ')[4])/1024/1024)

  device.disconnect()

  now.append(str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))

  OUTPUT = open("output.txt", "w")
  OUTPUT.write(str(now))
  OUTPUT.write("\n")
  OUTPUT.write(str(voice))
  OUTPUT.write("\n")
  OUTPUT.write(str(video))
  OUTPUT.write("\n")
  OUTPUT.write(str(high))
  OUTPUT.write("\n")
  OUTPUT.write(str(medium))
  OUTPUT.write("\n")
  OUTPUT.write(str(low))
  OUTPUT.write("\n")
  OUTPUT.close()

  # wait 5 minutes
  time.sleep(600)
