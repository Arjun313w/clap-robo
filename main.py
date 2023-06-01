DFRobotMaqueenPlusV2.init()
P = True

def on_forever():
    global P
    if input.sound_level() > 100:
        P = not (P)
        if P == True:
            DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_ALL_MOTOR, MyEnumDir.E_BACKWARD, 150)
            DFRobotMaqueenPlusV2.control_led(MyEnumLed.E_ALL_LED, MyEnumSwitch.E_OPEN)
        else:
            DFRobotMaqueenPlusV2.control_motor_stop(MyEnumMotor.E_ALL_MOTOR)
            DFRobotMaqueenPlusV2.control_led(MyEnumLed.E_ALL_LED, MyEnumSwitch.E_CLOSE)
basic.forever(on_forever)
