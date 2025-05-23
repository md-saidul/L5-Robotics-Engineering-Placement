import event, time, cyberpi, mbuild, mbot2

@event.is_press('b')
def is_btn_press():
    while True:
      if mbuild.ultrasonic2.get(1) < 10:
        mbot2.turn(-97)

      mbot2.forward(50)