import viz
import vizact
import vizshape
from random import randint


#viz init stuff
viz.phys.enable()
viz.go();

# Top window
BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeWindow.visible(0,viz.SCREEN)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0])


# mouse stuff
viz.mouse(viz.OFF)
viz.mouse.setVisible(viz.ON)

#create the plane
quad = vizshape.addQuad(size=[50,50]);
quad.setEuler(0,90,0)
quad.emissive(1,1,1)
quad.collideMesh()

# generate random cubes
for i in range(0,50):
	box = vizshape.addBox();
	box.setPosition(randint(0,50)-25,1,randint(0,50)-25)
	box.collideBox()


counter = 0
line = 0

# pick a line 
def pickLine():
	global line
	global counter
	object = viz.pick()

	lineScreen = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
	if line is not 0:
		line.remove()
	
	viz.startLayer(viz.LINES)  
	if object.valid() and object.id is not quad.id :
		viz.vertexColor(1,0,0)
	else:
		viz.vertexColor(0,0,1)
	viz.vertex(lineScreen.begin)
	viz.vertex(lineScreen.end)		
	line = viz.endLayer() 


# reset the view
def reset():
	viz.MainView.setEuler(0,0,0)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pickLine)
vizact.onkeydown('r',reset)



MOVE_SPEED = .5
view = viz.MainView

# move the person
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

# move the looking axis with the mouse
def mousemove(e):
	euler = view.getEuler(viz.HEAD_ORI)
	euler[0] += e.dx*0.1
	euler[1] += -e.dy*0.1
	euler[1] = viz.clamp(euler[1],-85.0,85.0)
	view.setEuler(euler,viz.HEAD_ORI)

viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)



vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatePerson)




