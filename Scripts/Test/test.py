import time
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
 
kit = MotorKit()
 

def StepperController(Direction="F", Style="D", StepCount=200):
#    print(f"Going to turn {StepCount} going {Direction} with the style of {Style}")

    if (Direction == "F"):
        Direction = stepper.FORWARD
    elif (Direction == "B"):
        Direction = stepper.BACKWARD

    if (Style == "D"):
        Style = stepper.DOUBLE

    for i in range(StepCount):
        kit.stepper2.onestep(direction=Direction, style=Style)
        time.sleep(0.01)

def ReleaseMotor():
    kit.stepper1.release()

StepperController(Direction="F", StepCount=200)
StepperController(Direction="B", StepCount=200)
time.sleep(5)
StepperController(Direction="F", StepCount=10)
time.sleep(5)
StepperController(Direction="B", StepCount=390)
kit.stepper2.release()
