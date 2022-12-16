#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Button, Color, Stop
from pybricks.tools import wait

# The colored objects are either red, green, blue, or yellow.
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]

# Initialize the EV3 brick.
ev3 = EV3Brick()
gripper_motor = Motor(Port.A)

# Initialize the Color Sensor. It is used to detect the color of the objects.
color_sensor = ColorSensor(Port.S3)


def ataque():
    color = color_sensor.color()
    #if color == Color.GREEN:1
    gripper_motor.run_until_stalled(400, then=Stop.HOLD, duty_limit=60)
    gripper_motor.run_target(200, -50)
    print("teste1")
        
