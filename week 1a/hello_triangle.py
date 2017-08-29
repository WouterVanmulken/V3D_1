import viz
import vizact
import vizshape
viz.go()
vizshape.addAxes()
viz.startLayer(viz.POLYGON)
viz.vertex(0,0,0)
viz.vertex(0,10,0)
viz.vertex(0,0,20)

mypoint = viz.endLayer()
mypoint.setEuler(10,10,10)
#mypoint.setPosition(1,0,0)

test_slider = viz.addSlider()

def scaleTriangle(val):
	for plant in plants:
		plant.setScale([val]*3)
		
		
viz.addChild('lab.osgb')