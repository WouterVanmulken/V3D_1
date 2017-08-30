import viz
import vizshape
import decimal
import math

viz.clearcolor(0.75, 0.75, 0.75)
#vizshape.addAxes()
viz.setMultiSample(4)
#piazza = viz.addChild('piazza.osgb')
#viz.addChild('donut.obj')
def createCube(position,size):
	xOffset = position[0]
	yOffset = position[1]
	zOffset = position[2]

	x1 = vizshape.addQuad([size[0],size[1]],vizshape.AXIS_X)
	x2 = vizshape.addQuad([size[0],size[1]],vizshape.AXIS_X)
	y1 = vizshape.addQuad([size[1],size[0]],vizshape.AXIS_Y)
	y2 = vizshape.addQuad([size[1],size[0]],vizshape.AXIS_Y)
	z1 = vizshape.addQuad([size[2],size[1]],vizshape.AXIS_Z)
	z2 = vizshape.addQuad([size[2],size[1]],vizshape.AXIS_Z)

	x1.setPosition(xOffset + (size[0]/2),yOffset,zOffset)
	x2.setPosition(xOffset - (size[0]/2),yOffset,zOffset)
	y1.setPosition(xOffset, yOffset+ (size[1]/2), zOffset)
	y2.setPosition(xOffset, yOffset- (size[1]/2), zOffset)
	z1.setPosition(xOffset, yOffset, zOffset+ (size[2]/2))
	z2.setPosition(xOffset, yOffset, zOffset- (size[2]/2))
	
	return [x1,x2,y1,y2,z1,z2]


def createCylinder(r,pos):
    # x = cx + r * cos(a)
    # y  = cy + r * sin(a)

    cx = pos[0]
    cy = pos[1]
    
    for degree in range(0,360):
        x = cx + r * math.cos(degree)
        y = cy + r * math.sin(degree)
        a = vizshape.addQuad([1,1],vizshape.AXIS_X)
        a.setPosition(x,y)
    
#todo fix 1/2 being 0 since it uses ints
#createCube([1,1,1],[2,2,2]);
#createCylinder(1,[1,1]);
#vizshape.addCylinder()



print(1./2)



viz.startLayer(viz.POINTS)

#viz.startLayer(viz.POINTS)
#viz.vertexColor(1,0,0)
#viz.vertex(0,1,0)
#viz.startLayer(viz.LINES)
#viz.vertex(-1,0,0)
#viz.vertex(1,0,0)
#object = viz.endLayer()

viz.MainView.setPosition(0,0,-2)
viz.startLayer(viz.POINTS)
viz.vertexColor(0,0,0)
viz.vertex(0,0,0) 
viz.endLayer()



viz.go()