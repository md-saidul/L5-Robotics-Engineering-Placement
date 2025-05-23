import event, time, cyberpi, mbot2

@event.is_press('b')
def is_btn_press():
    mbot2.forward(50, 2)
    time.sleep(1)
    mbot2.forward(100, 3)
    time.sleep(1)
    mbot2.straight(-50)
    time.sleep(2)
    mbot2.turn(-90)
    mbot2.forward(50, 2)
    time.sleep(2)
    mbot2.turn(90)
    mbot2.forward(50, 2)