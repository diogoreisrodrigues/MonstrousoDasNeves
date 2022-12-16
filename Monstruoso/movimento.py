#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, UltrasonicSensor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from ataques import ataque



# Initialize the EV3 Brick..

ev3 = EV3Brick()

# Initialize the motors....
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
UltrasonicSensor = UltrasonicSensor(Port.S4)
gripper_motor = Motor(Port.A)

# Initialize the Color Sensor. It is used to detect the color of the objects.
color_sensor = ColorSensor(Port.S3)

hasGear = False
Zombie1 = False
Zombie2 = False
NumGear = 0

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.settings(405,300,300,300)

coord = [1,1]

def move(coord, dir) : 

    newCoord = coord
    if(dir == 'N') :
        if(coord[1]>1) :
            robot.turn(405)
            robot.straight(420)
            robot.turn(-405)
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
            robot.turn(-195)
            robot.straight(420)
            robot.turn(195)
            #sound.speak('ok')
            newCoord[0] = coord[0] -1
        else:
            print('fora do tabuleiro')
    elif(dir == 'E') :
        if(coord[0]<6) :
            robot.turn(195)
            robot.straight(420)
            robot.turn(-195)
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

def pickGear(coord):
    global NumGear      #Numero de peças que já estão na mota
    color = color_sensor.color()    
    if color == Color.BLUE:
        ev3.speaker.say('I will take this bullet')
        #gripper_motor.run_until_stalled(405, then=Stop.HOLD, duty_limit=60)
        #gripper_motor.run_target(200, -50)
        print("teste1")
        NumGear = NumGear + 1                   #coloca uma peça na mota
        print(NumGear)
        if(NumGear == 2):                       #verifica se já tem as duas peças na mota1
            while(coord[0] != 6):                   #anda tudo para a esquerda
                recon(coord)
                coord = move(coord, "E")
                print(coord)
                esperaSensorToque()
            while(coord[1] != 6):                   #anda tudo para baixo
                recon(coord)
                coord = move(coord, "S")
                print(coord)
                esperaSensorToque()
            ev3.speaker.say('Bye Bye motherfuckers')            #se tiver acaba o jogo 
            print("acabou o jogo")
            esperaSensorToque()
        


def smell():
    global Zombie1
    global Zombie2
    if(140 <= UltrasonicSensor.distance() <= 405 ):
        Zombie1 = True
        Zombie2 = False
        ev3.speaker.say('I smell you bitch')
        robot.straight(200)
        ataque()
        robot.straight(-200)

    if(450 <= UltrasonicSensor.distance() <= 740 ):
        Zombie2 = True
        Zombie1 = False
        ev3.speaker.say('I see you pendejo')
    print("Zombie1:"+ str(Zombie1))
    print("Zombie2:"+ str(Zombie2))

def recon(coord):
    x = coord[0]
    y = coord[1]

    if(x == 1 and y == 1 ):
        smell()  
        robot.turn(195)
        smell()
        robot.turn(-195)
    elif(x == 1 and 1<y<6):
        smell()  
        robot.turn(195)
        smell()
        robot.turn(195)
        smell()
        robot.turn(-405)
    elif(x == 1 and y == 6):
        robot.turn(195)
        smell()
        robot.turn(195)
        smell()
        robot.turn(-405)
    elif(1<x<6 and y == 1):
        smell()  
        robot.turn(195)
        smell()
        robot.turn(405)
        smell()
        robot.turn(195)
    elif(x == 6 and y == 1):
        smell()
        robot.turn(-195)
        smell()
        robot.turn(195)
    elif(x == 6 and 1<y<6):
        smell()
        robot.turn(-195)
        smell()
        robot.turn(-195)  
        smell()
        robot.turn(405)
    elif(x == 6 and y == 6):
        robot.turn(-195)
        smell()
        robot.turn(-195)  
        smell()
        robot.turn(405)
    elif(1<x<6 and y == 6):
        robot.turn(195)
        smell()
        robot.turn(195)  
        smell()
        robot.turn(195)
        smell()
        robot.turn(195)
    else:
        smell()
        robot.turn(195)
        smell()
        robot.turn(195)  
        smell()
        robot.turn(195)
        smell()
        robot.turn(195)

def pickBullet():
    color = color_sensor.color()
    if color == Color.GREEN:
        ev3.speaker.say('I will take this BULLET')
        #gripper_motor.run_until_stalled(405, then=Stop.HOLD, duty_limit=60)
        #gripper_motor.run_target(200, -50)


while(True):
    
    while(coord[0] != 6):
        recon(coord)
        coord = move(coord, "E")                #percorre primeira fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    wait(1000)
    
    if(coord[1] != 6):
        recon(coord)
        coord = move(coord, "S")
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    
    while(coord[0] != 1):
        recon(coord)
        coord = move(coord, "W")                #percorre segunda fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()

    if(coord[1] != 6):
        recon(coord)
        coord = move(coord, "S")                #desce para a terceira fila
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    
    while(coord[0] != 6):
        recon(coord)
        coord = move(coord, "E")                #percorre terceira fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    wait(1000)
    
    if(coord[1] != 6):
        recon(coord)
        coord = move(coord, "S")
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    
    while(coord[0] != 1):
        recon(coord)
        coord = move(coord, "W")                #percorre quarta fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()

    if(coord[1] != 6):
        recon(coord)
        coord = move(coord, "S")
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    
    while(coord[0] != 6):
        recon(coord)
        coord = move(coord, "E")                #percorre quinta fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    wait(1000)
    
    if(coord[1] != 6):
        recon(coord)
        coord = move(coord, "S")
        pickGear(coord)
        pickBullet()
        esperaSensorToque()
    
    while(coord[0] != 1):
        recon(coord)
        coord = move(coord, "W")                #percorre sexta fila
        print(coord)
        pickGear(coord)
        pickBullet()
        esperaSensorToque()

    break

