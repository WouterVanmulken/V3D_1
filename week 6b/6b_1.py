import viz
import vizact
import vizshape
from random import randint


# create bird eye window
BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeWindow.visible(0,viz.SCREEN)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,20,0])
BirdEyeView.setEuler([0,90,0])


# Add stick
stick = vizshape.addCylinder()
stick.setScale(.1,1,.1)
stick.color(1,0,0)
#link = viz.link(viz.MainView,stick)
link = viz.grab(viz.MainView,stick)
link.setOffset([0,1,5])
#link.setOffset([0,-.3,1])
link.setEuler(0,45,0)

#stick.setEuler(0,45,0)
stick.setPosition(0,1.5,1)

#make ground
plane = vizshape.addQuad(size=[50,50]);
plane.setEuler(0,90,0)
plane.emissive(1,1,1)
plane.collideMesh()

#make random cubes
for i in range(0,50):
	box = vizshape.addBox();
	box.setPosition(randint(0,50)-25,1,randint(0,50)-25)
	box.collideBox()

#enable physics
viz.phys.enable()
viz.setMultiSample(4)
viz.fov(60)
viz.go();