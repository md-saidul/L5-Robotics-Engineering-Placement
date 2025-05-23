from makeblock import *
import cyberpi
from cyberpi import *
import mbot2
import time
import random

testInProgress = False
displayStartMessage = False

def BeginRGBSensorTest():
    cyberpi.display.clear()

    # Global variables for display purposes
    global testInProgress
    global displayStartMessage 
    testInProgress = True

    testSensor = "l2"

    rValue = 0
    gValue = 0
    bValue = 0

    # Sensor Test

    while (True):
        cyberpi.display.clear()
        #cyberpi.console.print("Object detected " + str(cyberpi.ultrasonic2.get(1)) + "cm from sensor\nPress \"A\" to end test.")
        rValue = cyberpi.quad_rgb_sensor.get_red(testSensor, 1)
        gValue = cyberpi.quad_rgb_sensor.get_green(testSensor, 1)
        bValue = cyberpi.quad_rgb_sensor.get_blue(testSensor, 1)

        cyberpi.console.print("Red Value: " + str(rValue) + "\nGreen Value: " + str(gValue) + "\nBlue Value: " + str(bValue) + "\nPress \"A\" to end test.")

        if cyberpi.controller.is_press("a"):
            break
        time.sleep(1)

    testInProgress = False
    displayStartMessage = False
    cyberpi.display.clear()

# Main loop
while True:

    if not testInProgress:
        
        if not displayStartMessage:
            cyberpi.display.clear()
            cyberpi.console.print("Please press button \"A\" to begin Sensor test.")
            displayStartMessage = True

        if cyberpi.controller.is_press("a"):
            BeginRGBSensorTest()

    time.sleep(0.1)