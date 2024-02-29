import time
import sys

inpt = input("Enter time in format: HH:MM:SS ")
hh = int(inpt[:2])
mm = int(inpt[3:5])
ss = int(inpt[6:])

t = hh*3600+mm*60+ss

for x in range(t,0,-1):
  sec = x % 60
  min = int(x/60) % 60
  hour = int(x / 3600)
  print(f"{hour:02}:{min:02}:{sec:02}", end="\r")
  time.sleep(1)




  # https://github.com/olaDEN/