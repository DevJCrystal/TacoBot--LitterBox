#!/usr/bin/python
import os
import time
import subprocess
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# Data collecting

# Error Count
EC = 0

# Success Count
SC = 0

# Important vars
startUp = True
isRunning = "F"
isRunningTimeStamp = None
dataPath = "/home/pi/Scripts/data.txt"
motorPath = "/home/pi/Scripts/motor.txt"

def SetMotorFileState(Letter):
    global isRunning

    f = open(motorPath, "w")
    f.write(Letter)
    f.close()

    isRunning = Letter

def ReadMotorFileState():
    global isRunning

    f = open(motorPath, "r")
    isRunning = f.readline()
    f.close()

def SetDataFileState():
    global EC
    global SC

    f = open(dataPath, "w")
    f.writelines(str(EC) + "\n" + str(SC))
    f.close()

def ReadDataFileState():
    global EC
    global SC

    f = open(dataPath, "r")
    EC = f.readline().strip("\n")
    SC = f.readline().strip("\n")
    f.close()

def UpdateVar():
    global EC
    global SC

    global startUp
    global motorPath
    global isRunning
    global isRunningTimeStamp

    ReadMotorFileState()

    ReadDataFileState()

    if (isRunning == "F1"):
        isRunningTimeStamp = None

        SC = int(SC) + 1

        SetDataFileState()

        # Do this so the score doesn't keep going up
        SetMotorFileState("F")

    if (isRunning == "T" and startUp):
        SetMotorFileState("E")

    if (startUp):
        # Starts the monitor script
        p = subprocess.Popen(['python3', '/home/pi/Scripts/Monitor.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
        

    # Set this to false after first fun
    startUp = False

@app.route('/')
def homepage():
    global isRunning

    UpdateVar()
    Message = None

    print(isRunning)
    if (isRunning == "E"):
        # We won't increase the error count here because every refresh/connection would increase it
        # Adding it to the reset
        Message = "LitterBox in Error State!"
    else:
        Message = ""

    return render_template('home.html', motorRunning=isRunning, Message=Message, EC=EC, SC=SC)

@app.route('/run')
def run_task():
    global motorPath
    global isRunning
    global isRunningTimeStamp

    # This is to prevent running if there was a loss of power.
    # Will need to be reset.
    if (isRunning != "E"):
        print ("Run Litter Cleanup")
        SetMotorFileState("T")
        isRunningTimeStamp = os.stat(motorPath)
        
    return redirect(url_for('homepage'))

@app.route('/reset')
def reset_task():
    global EC
    global motorPath
    global isRunning
    global isRunningTimeStamp

    EC = int(EC) + 1
    SetDataFileState()

    isRunningTimeStamp = None

    SetMotorFileState("F")
    return redirect(url_for('homepage'))

@app.route('/resetdata')
def resetdata_task():
    global EC
    global SC

    SC = 0
    EC = 0
    SetDataFileState()

    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
