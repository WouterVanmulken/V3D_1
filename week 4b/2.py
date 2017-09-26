import viz
import vizshape
import vizact



viz.MainView.setPosition(0,0,-30)

cylinder = vizshape.addCylinder(2,.3)


sparks = viz.addChild('sparks.osg')

sparks.setEuler(0,180,0)

cone = vizshape.addCone()

cylinder.setParent(cone)
sparks.setParent(cone)

cone.setPosition(0,3,0)
cylinder.setPosition(0,-1.5,0)
sparks.setPosition(0,-2,0)

count = 0
space = .3

def move():
	global cone
	global count
	global space
	count += space
	cone.setPosition(0,count,0)
	if count > 20:
		count = 0

vizact.ontimer(0,move)

viz.go()