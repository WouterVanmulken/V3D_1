﻿import viz
import vizshape
import math

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

#createCube([1,2,3])

def createCylinder(pos,r,height):
	
	cx = pos[0]
	cz = pos[1]
	
	viz.MainView.setPosition(0,-.3,-1)
	viz.startLayer(viz.QUADS)
	
	viz.vertexColor(1,0,0)
	
	for degree in range(0,360):
				x1 = cx + r * math.cos(degree)
				z1 = cz + r * math.sin(degree)
				
				x2 = cx + r * math.cos(degree +1)
				z2 = cz + r * math.sin(degree+1)
								
				viz.vertex(x1,0,z1) 
				viz.vertex(x1,height,z1) 
				
				viz.vertex(x2,height,z2)  
				viz.vertex(x2,0,z2)
	
	viz.startLayer(viz.TRIANGLE_FAN)
	viz.vertexColor(0,1,0)
	for degree in range(0,360):
				x1 = cx + r * math.cos(degree)
				z1 = cz + r * math.sin(degree)
								
				viz.vertex(x1,0,z1)
	viz.startLayer(viz.TRIANGLE_FAN)
	viz.vertexColor(0,0,1)
	for degree in range(0,360):
				x1 = cx + r * math.cos(degree)
				z1 = cz + r * math.sin(degree)
				
				viz.vertex(x1,height,z1)
	viz.endLayer()


createCylinder([2,2],0.5,.4)

viz.go()