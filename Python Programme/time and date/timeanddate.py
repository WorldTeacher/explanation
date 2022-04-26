import time #encodes time in unix/epoch timestamps (aka seconds since Jan 1, 1970)
import datetime as dt #encodes time in human readable format

#declare variables that the program is based on
raw_time=time.time() #this gives a floating number, which is encoded in unix time
conv_time=dt.datetime.fromtimestamp(raw_time) #this converts the unix time to a human readable time
print(conv_time)
current=dt.datetime.now() #this gives the current time, already encoded in human readable format
print(current)