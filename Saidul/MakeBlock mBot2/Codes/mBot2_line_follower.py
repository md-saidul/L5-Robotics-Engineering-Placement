import event, time, cyberpi, mbot2, mbuild

motor_power = 0
turn_speed = 0
left_motor_power = 0
right_motor_power = 0

@event.is_press('a')
def is_btn_press():
    global motor_power, turn_speed, left_motor_power, right_motor_power
    mbot2.drive_power(0, 0)

@event.is_press('b')
def is_btn_press1():
    global motor_power, turn_speed, left_motor_power, right_motor_power
    while True:
      motor_power = 30
      turn_speed = 0.8
      while True:
        left_motor_power = (motor_power - turn_speed * mbuild.quad_rgb_sensor.get_offset_track(1))
        right_motor_power = -1 * ((motor_power + turn_speed * mbuild.quad_rgb_sensor.get_offset_track(1)))
        mbot2.drive_power(left_motor_power, right_motor_power)