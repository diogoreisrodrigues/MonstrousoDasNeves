#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

sound = Sound()

Start = [1,1]  #coordenada inicial do robo
fixedBike = False  # váriavel para saber se a mota está arranjada
hasBullet = False # variável boleana para saber se robo tem bala
hasgear = False # variável boleana para saber se robo tem peça
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

