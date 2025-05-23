import event, time, cyberpi, mbot2, mbuild

@event.is_press('b')
def is_btn_press():
    
    while True:
        if (mbuild.quad_rgb_sensor.is_color("red", "R1", 1)):
            mbot2.EM_stop("ALL")
        elif (mbuild.quad_rgb_sensor.is_color("green", "R1", 1)):
            mbot2.turn(90)
            mbot2.forward(50)
        elif (mbuild.quad_rgb_sensor.is_color("blue", "R1", 1)):
            mbot2.turn(-90)
            mbot2.forward(50)
        else:
            mbot2.forward(50)