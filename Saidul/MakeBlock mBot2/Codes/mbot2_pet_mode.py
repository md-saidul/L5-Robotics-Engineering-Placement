import event, time, cyberpi, mbuild, mbot2

distance = 0

@event.is_press('b')
def is_btn_press():
    global distance
    while True:
      distance = mbuild.ultrasonic2.get(1)
      cyberpi.display.show_label(distance, 16, "center", index= 0)
      if distance < 80:
        if distance > 10:
          mbot2.forward(50)

        else:
          mbot2.EM_stop("ALL")
          time.sleep(3)
          mbot2.turn(-90)

      else:
        mbot2.EM_stop("ALL")
        mbot2.turn(-90)