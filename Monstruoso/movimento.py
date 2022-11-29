#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from ataques import ataque

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

coord = [1,1]

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def movimentoBasico():
    robot.straight(200)
    robot.turn(90)

def move() : 
    newCoord = coord
    if(dir == 'N') :
        if(coord[1]>1) :
            robot.turn(180)
            robot.straight(20)
            robot.turn(-180)
            coord[1] = coord[1] -1
            #sound.speak('orait').
        else:
            print('fora do tabuleiro')
    elif(dir == 'S') :
        if(coord[1] < 6) :
            robot.straight(20)
            sound.speak('ok')
            coord[1] = coord[1] +1
        else:
            print('fora do tabuleiro')    
    elif(dir =='W') :
        if(coord[0]>1) :
            robot.turn(-90)
            robot.straight(20)
            robot.turn(90)
            sound.speak('ok')
            coord[0] = coord[0] -1
        else:
            print('fora do tabuleiro')
    elif(dir == 'E') :
        if(coord[0]<6) :
            robot.turn(90)
            robot.straight(20)
            robot.turn(-90)
            #sound.speak('orait')
            coord[0] = coord[0] +1
        else:
            print('fora do tabuleiro') 
    else:
        print("Erro")
        #sound.speak('Erro')
    return newCoord


while(True):
    move("E")
    ataque()
    move("S")
    ataque()
    move("E")
    ataque()
    move("S")
    ataque()
    move("W")
    ataque()
    move("N")
    ataque()
    move("S")
    ataque()
    break
    movimentoBasico()

#TESTE

