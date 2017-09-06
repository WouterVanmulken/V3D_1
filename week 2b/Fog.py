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
limits = []

limits[0] = [0,1]
limits[1] = [0,10]
limits[2] = [0,5]

#def setpos(sphere, index):
#	if sphere.
viz.go()