import viz
import vizshape
import vizact

viz.clearcolor(.5,.5,.5)

viz.MainView.setPosition(2,0,-10)

sphere1 = vizshape.addSphere(1)
sphere1.color(1,0,0)


sphere2 = vizshape.addSphere(1)
sphere2.color(0,1,0)
sphere2.setPosition(2.5,0,10)

sphere3 = vizshape.addSphere(1)
sphere3.color(0,0,1)
sphere3.setPosition(5,0,5)

z = [0,10,5]

steps = 5
goingUp = False

def changePos():
	speed = .1
	global steps
	global goingUp
	if goingUp :
		steps +=speed
		z[0] +=speed
		z[1] +=speed
		z[2] +=speed
		if steps >5:
			goingUp = False
	else:
		steps -=speed
		z[0] -=speed
		z[1] -=speed
		z[2] -=speed
		if steps <0:
			goingUp = True
	
	sphere1.setPosition(0,0,z[0])
	sphere2.setPosition(2.5,0,z[1])
	sphere3.setPosition(5,0,z[2])

viz.fogcolor(0.5,0.5,0.5)


vizact.ontimer(0.02	,changePos)
vizact.onkeydown('1',viz.fog,1,10)
vizact.onkeydown('2',viz.fog,.2)
vizact.onkeydown('3',viz.fog,0)

viz.go()