#!/usr/bin/python
import subprocess
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

isRunning = "F"
startUp = True

def UpdateVar():
    global isRunning
    global startUp

    f = open("/home/pi/Scripts/motor.txt", "r")
    isRunning = f.read()
    f.close()

    if (isRunning == "T" and startUp):
        isRunning = "E"
        f = open("/home/pi/Scripts/motor.txt","w")
        f.write(isRunning)
        f.close()

    # Set this to false after first fun
    startUp = False

@app.route('/')
def homepage():
    global isRunning
    UpdateVar()
    Message = None

    print(isRunning)
    if (isRunning == "E"):
        Message = "LitterBox in Error State!"
    else:
        Message = ""

    return render_template('home.html', motorRunning=isRunning, Message=Message)

@app.route('/run')
def run_task():
    global isRunning

    # This is to prevent running if there was a loss of power.
    # Will need to be reset.
    if (isRunning != "E"):
        isRunning = "T"
        print ("Run Litter Cleanup")
        f = open("/home/pi/Scripts/motor.txt", "w")
        f.write(isRunning)
        f.close()
    return redirect(url_for('homepage'))

@app.route('/reset')
def reset_task():
    global isRunning
    isRunning = "F"
    f = open("/home/pi/Scripts/motor.txt", "w")
    f.write(isRunning)
    f.close()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    p = subprocess.Popen(['python3', '/home/pi/Scripts/Monitor.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
    app.run(host="0.0.0.0")
