#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor, Sound)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from ataques import ataque
from movimento import move


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

Sound = Sound()

Start = [1,1]  #coordenada inicial do robo
fixedBike = False  # váriavel para saber se a mota está arranjada
hasBullet = False # variável boleana para saber se robo tem bala
hasGear = False # variável boleana para saber se robo tem peça
squareRecon = ["-","-","-","-"] #S E N array com o reconhecimento das casa em seu redor
smellZombie = ["-","-"] # cheiro de zombie dos dois zombies pode ser 1 ou 2 
squareAction = False # variável que permite saber se efetuou alguma ação tendo em conta os quadrados a seu redor
zombieSmell1 = False #tem pelo menos um zombie a 1 casa
zombieSmell2 = False #tem pelo menos um zombie a 2 casas
zombie1 = [] #guarda a posição do zombie 1
zombie2 = [] #guarda a posição do zombie 2
sleepZombie1 = [] #coordenada do zombie atordoado 
sleepZombie2 = [] #coordenada do zombie atordoado
sleepTime1 = 2 #numero de turnos que o zombie 1 fica atordoado
sleepTime2 = 2 #numero de turmos que o zombie 2 fica atordoado
coord = [1,1]

def esperaSensorToque():
	sensorToque = TouchSensor(Port.S1)
	
	print('\nPrecione o botao para incializar o turno...')
	while (not sensorToque.pressed()):		
			if(hasGear): 
				Sound.tone(1000, 200)
				sleep(0.2)
			else:
				sleep(0.2)
				
while(True):
    
    while(coord[0] != 6):
        coord = move(coord, "E")
        print(coord)
        ataque()
        esperaSensorToque()
    wait(1000)
    coord = move(coord, "S")
    ataque()
    while(coord[0] != 1):
        coord = move(coord, "W")
        print(coord)
        ataque()
        esperaSensorToque()
    wait(1000)
    coord = move(coord, "S")
    ataque()
    while(coord[0] != 6):
        coord = move(coord, "E")
        print(coord)
        ataque()
        esperaSensorToque()
    wait(1000)
    break