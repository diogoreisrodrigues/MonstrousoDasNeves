sound = Sound()

coord = [1,1] #coordenada inicial do robo
bikeFixed = False # váriavel para saber se a mota está arranjada
hasBullet = False # variável boleana para saber se robo tem bala
hasPart = False # variável boleana para saber se robo tem peça
numParts = 0 #variável que guarda o numero de peças na mota
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