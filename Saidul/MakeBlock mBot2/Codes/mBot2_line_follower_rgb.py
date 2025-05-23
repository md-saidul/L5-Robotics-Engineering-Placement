import event, time, cyberpi, mbuild, mbot2

motor_power = 0
turn_speed = 0
left_motor_power = 0
right_motor_power = 0
offset = 0

def followLine():
    offset = mbuild.quad_rgb_sensor.get_offset_track(1)
    left_motor_power = (motor_power - turn_speed * offset)
    right_motor_power = -1 * ((motor_power + turn_speed * offset))
    mbot2.drive_power(left_motor_power, right_motor_power)

@event.is_press('b')
def is_btn_press():
    global motor_power, turn_speed, left_motor_power, right_motor_power, offset
    motor_power = 40
    turn_speed = 0.8
    while True:
        if (mbuild.quad_rgb_sensor.is_color("red","R1",1)):
            mbot2.EM_stop("ALL")
            time.sleep(3)
            motor_power = 40
            followLine()
            
        elif (mbuild.quad_rgb_sensor.is_color("yellow","R1",1)):
            motor_power = 10
            followLine()

        elif (mbuild.quad_rgb_sensor.is_color("green","R1",1)):
            motor_power = 40
            followLine()

        followLine()