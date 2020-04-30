#!/usr/bin/python
import os
import time
import schedule
import threading
import subprocess
import MotorController
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

# Data collecting

# Error Count
EC = 0

# Success Count
SC = 0

# Important vars
startUp = True
isRunning = "F"
schedTime = None
isRunningTimeStamp = None
dataPath = "/home/pi/Scripts/data.txt"
motorPath = "/home/pi/Scripts/motor.txt"
schedulePath = "/home/pi/Scripts/sched.txt"


# Set Data file
def SetDataFileState():
    global EC
    global SC

    f = open(dataPath, "w")
    f.writelines(str(EC) + "\n" + str(SC))
    f.close()

def GetDataFileState():
    global EC
    global SC

    f = open(dataPath, "r")
    EC = f.readline().strip("\n")
    SC = f.readline().strip("\n")
    f.close()


# Set Motor File
def SetMotorFileState(Letter):
    global isRunning

    f = open(motorPath, "w")
    f.write(Letter)
    f.close()

    isRunning = Letter

def GetMotorFileState():
    global isRunning

    f = open(motorPath, "r")
    isRunning = f.readline().strip()
    f.close()


# Set Sched File
def SetSchedFileState(Time):
    global schedTime

    schedule.clear('daily-tasks')

    f = open(schedulePath, "w")
    f.write(Time)
    f.close()

    if (Time == ""):
        Time = None
    else: 
        schedule.every().day.at(Time).do(Start_Task).tag('daily-tasks', 'pi')

    schedTime = Time

def GetSchedFileState():
    global schedTime

    schedule.clear('daily-tasks')

    f = open(schedulePath, "r")
    schedTime = f.readline().strip()
    f.close()

    if (schedTime == ""):
        schedTime = None
    else:
        schedule.every().day.at(schedTime).do(Start_Task).tag('daily-tasks', 'pi')

def UpdateVar():
    global EC
    global SC

    global startUp
    
    global motorPath
    global isRunning
    global schedTime
    global isRunningTimeStamp

    GetMotorFileState()
    print(isRunning)

    GetDataFileState()

    GetSchedFileState()
    if (schedTime != None):
        print(schedTime)

    if (isRunning == "F1"):
        isRunningTimeStamp = None

        SC = int(SC) + 1

        SetDataFileState()

        # Do this so the score doesn't keep going up
        SetMotorFileState("F")

    if (isRunning == "T" and startUp):
        SetMotorFileState("E")

    # Set this to false after first fun
    startUp = False

def Start_Task():
    RunningThread().start()

@app.route('/')
def homepage():

    UpdateVar()
    Message = None

    if (isRunning == "E"):
        # We won't increase the error count here because every refresh/connection would increase it
        # Adding it to the reset
        Message = "LitterBox in Error State!"
    else:
        Message = ""

    return render_template('home.html', motorRunning=isRunning, Message=Message, EC=EC, SC=SC, nextRun=schedule.next_run())

@app.route('/sched')
def sched():
    global schedTime
    UpdateVar()
    
    return render_template('schedule.html', scheduledTime=schedTime)

@app.route('/SetScheduledTime')
def setScheduledTime():
    tempTime = str(request.args.get('sched')).replace("%3A",":")
    SetSchedFileState(tempTime)

    return redirect(url_for('sched'))

@app.route('/clearSched')
def clearSchedTime():
    SetSchedFileState("")

    return redirect(url_for('sched'))

@app.route('/run')
def run_task():
    # Moved the code for the job schuduler
    Start_Task()
        
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

class ScheduleThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

    def run(self):
        while True:
            #print(schedule.next_run())
            schedule.run_pending()
            # schedule.idle_seconds() 
            # Might add the schedule.idle seconds back when I learn more about schedule
            # Currently when we adjust the time, we kinda break the task until the timer is over on the new task.
            time.sleep(1)

class RunningThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

    def run(self):
        global motorPath
        global isRunning
        global isRunningTimeStamp

        # This is to prevent running if there was a loss of power.
        # Will need to be reset.
        if (isRunning != "E"):
            print ("Run Litter Cleanup")
            SetMotorFileState("T")
            isRunningTimeStamp = os.stat(motorPath)
            MotorController.PhaseOne()

if __name__ == '__main__':
    UpdateVar()
    ScheduleThread().start()
    app.run(host="0.0.0.0")