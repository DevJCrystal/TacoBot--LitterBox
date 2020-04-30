import time
import schedule
import threading

schedTime = None
schedulePath = "E:\Python_Projects\MotorProject\TacoBot--LitterBox\sched.txt"

def Start_Task():
    print("Running!")

def GetSchedFileState():
    global schedTime
    global schedulePath

    schedule.clear('daily-tasks')

    f = open(schedulePath, "r")
    schedTime = f.readline().strip()
    f.close()

    if (schedTime == ""):
        schedTime = None
    else:
        schedule.every().day.at(schedTime).do(Start_Task).tag('daily-tasks')

while True:
    GetSchedFileState()
    print(schedule.next_run())
    schedule.run_pending()
    # schedule.idle_seconds() 
    # Might add the schedule.idle seconds back when I learn more about schedule
    # Currently when we adjust the time, we kinda break the task until the timer is over on the new task.
    time.sleep(1)