﻿import viz
import vizact
import vizshape
from random import randint

#used for drawing the line and draging the selected object
line = 0
selected = 0
difference = [0,0,0]

#mouse helper var
mouseDown = False

#movement
MOVE_SPEED = .5
view = viz.MainView


#viz init stuff
viz.phys.enable()
viz.go();

# Top window
BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeWindow.visible(0,viz.SCREEN)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,50,0])
BirdEyeView.setEuler([0,90,0])


# mouse stuff
viz.mouse(viz.OFF)
viz.mouse.setVisible(viz.ON)

#create the plane
plane = vizshape.addQuad(size=[50,50]);
plane.setEuler(0,90,0)
plane.emissive(1,1,1)
plane.collideMesh()

# generate random cubes
for i in range(0,50):
	box = vizshape.addBox();
	box.setPosition(randint(0,50)-25,1,randint(0,50)-25)
	box.collideBox()


farPlane = vizshape.addQuad(size=[50,50]);
farPlane.color(.6,0,0)
farPlane.setPosition(0,0,25)
farPlane.setEuler(0,0,90)



# reset the view
def reset():
	viz.MainView.setEuler(0,0,0)




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



# move the looking axis with the mouse
def mousemove(e):
	euler = view.getEuler(viz.HEAD_ORI)
	euler[0] += e.dx*0.1
	euler[1] += -e.dy*0.1
	euler[1] = viz.clamp(euler[1],-85.0,85.0)
	view.setEuler(euler,viz.HEAD_ORI)

	

#resets stuff
def mouseUp():
	global selected
	global mouseDown
	global difference
	
	selected = 0
	mouseDown = False
	difference = [0,0,0]

def drawLine(lineScreen, selected):
	global line
	
	if line is not 0:
		line.remove()
		
	viz.startLayer(viz.LINES)  
	
	if selected.valid() and selected.id is not plane.id and selected.id is not farPlane.id :
		viz.vertexColor(1,0,0)
	else:
		viz.vertexColor(0,0,1)

	viz.vertex(lineScreen.begin)
	viz.vertex(lineScreen.end)		
	line = viz.endLayer() 


# draw a line and select an object, called on mouseDown
def pickLine():
	global line
	global counter
	global selected	
	global mouseDown
	global difference
	mouseDown = True
	selected = viz.pick()
	
	lineScreen = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
	
	drawLine(lineScreen,selected)
	
	if selected.valid():
		farPlane.setPosition(plane.getPosition()[0],plane.getPosition()[1],selected.getPosition()[2])
		difference[0] =  selected.getPosition()[0] - viz.MainView.getPosition()[0]
		difference[1] =  selected.getPosition()[1] - viz.MainView.getPosition()[1] 
		difference[2] =  selected.getPosition()[2] - viz.MainView.getPosition()[2] 


def update():
	global mouseDown
	global selected
	global difference
	if mouseDown and selected is not 0:
		
		selected2 = viz.pick()
		
		lineScreen = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
		if selected2.id is farPlane.id:
			print lineScreen.getEnd()[0]
			drawLine(lineScreen,selected2)
			difference[0] =  lineScreen.getEnd()[0]
			difference[1] =  lineScreen.getEnd()[1]
#			difference[2] =  lineScreen.end[2]  
#			print 'x : ',lineScreen.end[0], ' y : ', lineScreen.end[1], ' z : ', lineScreen.end[2]
		
			pos = [0,0,0]
			pos[0] =  difference[0]
			pos[1] =  difference[1]
			pos[2] = viz.MainView.getPosition()[2] +difference[2]
			selected.setPosition(pos)
#			print 'x : ',pos[0], ' y : ', pos[1], ' z : ', pos[2]
		


 


viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)

vizact.onkeydown('r',reset)

vizact.ontimer(0,updatePerson)
vizact.ontimer(0,update)

vizact.onmouseup(viz.MOUSEBUTTON_LEFT,mouseUp)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pickLine)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatePerson)