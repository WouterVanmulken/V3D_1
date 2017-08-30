import viz
import vizshape

viz.setMultiSample(4)
viz.clearcolor(0.75, 0.75, 0.75)
piazza = viz.addChild('piazza.osgb')
def createCube(size):
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

	viz.endLayer()

createCube([1,2,3])
viz.go()