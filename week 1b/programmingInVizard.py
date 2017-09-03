import viz
import vizshape
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

ground = viz.addChild('ground.osgb')


#1
	

chest = viz.addChild('./objects/chest_without_cover.fbx')
chest.setPosition(0,0,-.4)

chest_cover = viz.addChild('./objects/chest_cover.fbx')
chest_cover.setPosition(0,.8,0)
chest_cover.setEuler(0,90,0)

rotation = 0

def test():
	global rotation
	rotation +=1
	chest_cover.setEuler(0,rotation,0)

vizact.ontimer(0,test)

#2

def createCube(size, position):
	x = size[0]
	y = size[1]
	z = size[2]
	
	viz.MainView.setPosition(0,-.3,-1)
	viz.startLayer(viz.QUADS)
	
	viz.vertexColor(x,0,0)
	viz.vertex(0,0,0) 
	viz.vertex(x,0,0)
	viz.vertex(x,0,z) 
	viz.vertex(0,0,z)  

	viz.vertexColor(0,y,0)
	viz.vertex(0,0,0) 
	viz.vertex(0,y,0)
	viz.vertex(x,y,0) 
	viz.vertex(x,0,0)

	viz.vertexColor(0,0,z)
	viz.vertex(0,0,0) 
	viz.vertex(0,y,0)
	viz.vertex(0,y,z) 
	viz.vertex(0,0,z)  

	viz.vertexColor(0.5,0,0)
	viz.vertex(x,0,0) 
	viz.vertex(x,0,z)
	viz.vertex(x,y,z) 
	viz.vertex(x,y,0)  

	viz.vertexColor(0,0.5,)
	viz.vertex(0,y,0)
	viz.vertex(0,y,z)
	viz.vertex(x,y,z) 
	viz.vertex(x,y,0)  

	viz.vertexColor(0,0,.5)
	viz.vertex(0,0,z)
	viz.vertex(x,0,z)
	viz.vertex(x,y,z) 
	viz.vertex(0,y,z)  

	cube = viz.endLayer()
	cube.setPosition(position[0],position[1],position[2])
	return cube




text = viz.addText3D('Snek',pos=[0,2.5,4])
text.name = 'Snek'
text.alignment(viz.ALIGN_CENTER_BOTTOM)
text.color(viz.BLUE)

for i in range(0,5):
	cube = createCube([1,1,1],[i,0-2.5,0])
	cube.setParent(parent=text)

textScreen = viz.addText(text.name,viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.setPosition([0.95,0.05,0])


#3
window = viz.addWindow()
window.fov=60

view = viz.addView()
window.setView(view)
view.setPosition([0,15,0])
view.setEuler([0,90,0])
