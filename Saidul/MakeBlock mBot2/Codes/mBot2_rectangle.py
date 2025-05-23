import event, time, cyberpi, mbot2, mbuild

@event.is_press('b')
def is_btn_press():
    mbot2.straight(50)
    mbot2.turn(90)
    mbot2.straight(25)
    mbot2.turn(90)
    mbot2.straight(50)
    mbot2.turn(90)
    mbot2.straight(25)
    mbot2.turn(90)
    time.sleep(4)

