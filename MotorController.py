import time
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

motorPath = "/home/pi/Scripts/motor.txt"

kit = MotorKit()

# Motor
motorSwitcher = {
        1: kit.stepper1.onestep,
        2: kit.stepper2.onestep
    }

# Style
styleSwitcher = {
        "S": stepper.SINGLE,
        "D": stepper.DOUBLE,
        "I": stepper.INTERLEAVE,
        "M": stepper.MICROSTEP
    }

# Direction
directionSwitcher = {
        "F": "stepper.FORWARD",
        "B": "stepper.BACKWARD"
    }

# Release
# 0 = All Motors | 1 = Motor1 | 2 = Motor2
def ReleaseMotors(motor=0):
    if (motor == 0):
        kit.stepper1.release()
        kit.stepper2.release()

    if (motor == 1):
        kit.stepper1.release()

    if (motor == 2):
        kit.stepper2.release()

# Let's GOOOOOO!
def StepperController(Motor=1, Style="D", Direction="F", StepCount = 200):

    tempMotor = Motor
    Motor = motorSwitcher.get(Motor)
    Style = styleSwitcher.get(Style)
    Direction = directionSwitcher.get(Direction)

    print(f"Motor: {tempMotor} | Style: {Style} | Direction: {Direction} | StepCount: {StepCount}")

    #timeStart = time.time()
    for i in range(StepCount):
        Motor(direction=Direction, style=Style)
    #finishedTime = time.time() - timeStart
    #print(finishedTime)

def PhaseOne():
    FinishedPhases()

def FinishedPhases():
    
    # for testing purposes
    StepperController(Style="D", StepCount=1000)
    StepperController(Style="S", StepCount=1000)
    ReleaseMotors(1)

    # Update everyone we finished!
    f=open(motorPath, "w")
    f.write("F1")
    f.close()
