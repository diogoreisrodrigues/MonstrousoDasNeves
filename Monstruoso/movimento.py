#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from ataques import ataque, pickGear

# Initialize the EV3 Brick..
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
UltrasonicSensor = UltrasonicSensor(Port.S4)

hasGear = False

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.settings(400,300,300,300)

coord = [1,1]

def move(coord, dir) : 
    newCoord = coord
    if(dir == 'N') :
        if(coord[1]>1) :
            robot.turn(380)
            robot.straight(420)
            robot.turn(-185)
            newCoord[1] = coord[1] -1
            #sound.speak('orait').
        else:
            print('fora do tabuleiro')
    elif(dir == 'S') :
        if(coord[1] < 6) :
            robot.straight(420)
            #sound.speak('ok')
            newCoord[1] = coord[1] +1
        else:
            print('fora do tabuleiro')    
    elif(dir =='W') :
        if(coord[0]>1) :
            robot.turn(-185)
            robot.straight(420)
            robot.turn(185)
            #sound.speak('ok')
            newCoord[0] = coord[0] -1
        else:
            print('fora do tabuleiro')
    elif(dir == 'E') :
        if(coord[0]<6) :
            robot.turn(185)
            robot.straight(420)
            robot.turn(-185)
            #sound.speak('orait')
            newCoord[0] = coord[0] +1
        else:
            print('fora do tabuleiro') 
    else:
        print("Erro")
        #sound.speak('Erro')
    return newCoord

def esperaSensorToque():
	sensorToque = TouchSensor(Port.S1)
	
	print('\nPressione o botao para incializar o turno...')
	while (not sensorToque.pressed()):		
			if(hasGear): 
				Sound.tone(1000, 200)
				wait(100)
			else:
				wait(100)

while(True):
    
    while(coord[0] != 6):
        coord = move(coord, "E")
        print(coord)
        ataque()
        pickGear()
        esperaSensorToque()
        
    wait(1000)
    coord = move(coord, "S")
    ataque()
    pickGear()
    esperaSensorToque()
    while(coord[0] != 1):
        coord = move(coord, "W")
        print(coord)
        ataque()
        pickGear()
        esperaSensorToque()
    wait(1000)
    coord = move(coord, "S")
    ataque()
    pickGear()
    esperaSensorToque()
    while(coord[0] != 6):
        coord = move(coord, "E")
        print(coord)
        ataque()
        pickGear()
        esperaSensorToque()
    wait(1000)
    break