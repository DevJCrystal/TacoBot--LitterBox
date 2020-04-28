# This is going to watch the motor.txt file to see when it is time to run. 
import os
import time
import MotorController

motorFile = "motor.txt"
lastModifiedTime = None

def SleepyTime(length=1):
    print(f"Going to sleep for: {length}")
    time.sleep(length)

def Finished():
    f = open("motor.txt", "w")
    f.write("F")
    f.close()
    FirstLoop()

def FirstLoop():
    global motorFile
    global lastModifiedTime

    f = open(motorFile, "r")
    temp = f.read()
    f.close()

    if (temp == "T"):
        f = open("motor.txt", "w")
        f.write("E")
        f.close()
    else:
        lastModifiedTime = os.stat(motorFile)
        MainLoop()

def MainLoop():
    global motorFile
    global lastModifiedTime

    SleepyTime(5)
    if (lastModifiedTime != os.stat(motorFile)):
        FirstLoop()
    else:
        MainLoop()

FirstLoop()