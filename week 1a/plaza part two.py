import viz
import vizshape
import decimal


viz.setMultiSample(4)
piazza = viz.addChild('piazza.osgb')

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
	print(size[0])
	print(size[0]/2)
	x1.setPosition(xOffset + (size[0]/2),yOffset,zOffset)
	x2.setPosition(xOffset - (size[0]/2),yOffset,zOffset)
	y1.setPosition(xOffset, yOffset+ (size[1]/2), zOffset)
	y2.setPosition(xOffset, yOffset- (size[1]/2), zOffset)
	z1.setPosition(xOffset, yOffset, zOffset+ (size[2]/2))
	z2.setPosition(xOffset, yOffset, zOffset- (size[2]/2))

#todo fix 1/2 being 0 since it uses ints
createCube([1,1,1],[2,2,2]);

viz.go()