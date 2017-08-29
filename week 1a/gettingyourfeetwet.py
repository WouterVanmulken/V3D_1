import viz
import vizshape
import vizact
import random
from random import randint
import decimal

viz.go()


#Setting the scene
viz.collision(True)
vizshape.addAxes() 

piazza = viz.addChild('piazza.osgb')

plant = viz.addChild('plant.osgb')
plant.setPosition([4,0,0])

viz.setMultiSample(4)
viz.MainWindow.fov(60)


# moving the viewpoint


viz.MainView.move([3,0,-7])
# why does the setposition only work if the move is called before
viz.MainView.setPosition(0,15,-15)
#viz.MainView.setEuler([0,30,0])

xpos = [-3, -1, 1, 3]
zpos = [4, 2, 0, -2, -4]
plants = []


def randomSize():
	return decimal.Decimal(random.randrange(5,10))/10
	
for x in xpos:
	for z in zpos:
		plant = viz.addChild('plant.osgb',cache= viz.CACHE_CLONE)
		plant.setPosition([x,0,z])
		plant.setEuler([randint(0,360),0,0])
		plant.setScale([randomSize(),randomSize(),randomSize()])
		plants.append(plant)

# timer events
spin = vizact.spin(0,1,0,30)

#for plant in plants:
#	plant.addAction(spin)

def spinPlant(plant):
	plant.addAction(spin)
vizact.ontimer(0.2,spinPlant,vizact.choice(plants))

# adding avatars

male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5,0,7])
male.setEuler([0,0,0])

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])


male.state(14)
female.state(14)

#pigeones

pigeons = []
for i in range(10):

    #Generate random values for position and orientation
    x = random.randint(-4,3)
    z = random.randint(4,8)
    yaw = random.randint(0,360)

    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')

    #Set position, orientation, and state
    pigeon.setPosition([x,0,z])
    pigeon.setEuler([yaw,0,0])
    pigeon.state(1)

    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon)

# inserting user interation

def walkAvatars():
    walk1 = vizact.walkTo([4.5, 0,-40])
    vizact.ontimer2(0.5,0,female.addAction,walk1)

    walk2 = vizact.walkTo([3.5,0,-40])
    male.addAction(walk2)

vizact.onkeydown('w',walkAvatars)


def pigeonsFeed():

    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)



