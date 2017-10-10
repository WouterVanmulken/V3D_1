import viz
import vizact
import vizshape
from random import randint


BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeWindow.visible(0,viz.SCREEN)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0])



viz.mouse(viz.OFF)
viz.mouse.setVisible(viz.ON)

quad = vizshape.addQuad(size=[50,50]);
quad.setEuler(0,90,0)
quad.emissive(1,1,1)
quad.collideMesh()


for i in range(0,50):
	box = vizshape.addBox();
	box.setPosition(randint(0,50)-25,1,randint(0,50)-25)
	box.collideBox()

viz.phys.enable()

viz.go();



cylinder = vizshape.addCylinder()
cylinder.visible(viz.OFF)
cylinder.color(1,0,0)

counter = 0
def pickBall():
	global counter
	object = viz.pick()

	line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
	line.getAxisAngle()
	
	cylinder.color(0,0,1)
	if object.valid() and object.id is not quad.id:
		print 'clicked in an object', counter
		cylinder.color(1,0,0)
		counter +=1
		cylinder.visible(viz.ON)
		pos = object.getPosition()
		pos[1] +=1  
		cylinder.setPosition(pos)
		
		object.color(0,1,0)
		object.setParent(viz.MainView)
		viz.link(viz.MainView, object)


def reset():
	viz.MainView.setEuler(0,0,0)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pickBall)
vizact.onkeydown('r',reset)



MOVE_SPEED = .5
view = viz.MainView

def updatePerson():	
	if viz.key.isDown(viz.KEY_UP):
		pos = view.getPosition()
		pos[2]+=MOVE_SPEED
		view.setPosition(pos)
	elif viz.key.isDown(viz.KEY_DOWN):
		pos = view.getPosition()
		pos[2]-=MOVE_SPEED
		view.setPosition(pos)

	if viz.key.isDown(viz.KEY_RIGHT):
		pos = view.getPosition()
		pos[0]+=MOVE_SPEED
		view.setPosition(pos)
	elif viz.key.isDown(viz.KEY_LEFT):
		pos = view.getPosition()	 
		pos[0]-=MOVE_SPEED
		view.setPosition(pos)

vizact.ontimer(0,updatePerson)

def mousemove(e):
	euler = view.getEuler(viz.HEAD_ORI)
	euler[0] += e.dx*0.1
	euler[1] += -e.dy*0.1
	euler[1] = viz.clamp(euler[1],-85.0,85.0)
	view.setEuler(euler,viz.HEAD_ORI)

viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)



vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatePerson)




