import viz
import vizact
import math

def createCube(size, pos):
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

	a =  viz.endLayer()
	a.setPosition(pos[0],pos[1],pos[2])
	return a
#4
cube = createCube([.25,.25,.25],[4,3,0])
cube.enable(viz.LIGHTING)


#1
viz.go()
matte = viz.addChild('matteMonkey.obj')
matte.emissive(1,0,0)

shiny = viz.addChild('shinyMonkey.obj')
shiny.setPosition(3,-.2,1.2)

viz.MainView.setPosition(1.2,1.5,-7)

headLight = viz.MainView.getHeadLight() 
headLight.disable() 


#2

#directional lights
dlight = viz.addLight() 
dlight.setEuler( 90, 0 ,0 ) 
dlight.color(1,0,0)

#point lights
plight = viz.addLight()
plight.enable()
plight.position(0,1,0)
plight.spread(180)
plight.intensity(2)
plight.color(0,1,0)

#spot lights
slight = viz.addLight()
slight.position(0,0,0)
slight.direction(0,0,1)
slight.spread(90)
slight.intensity(2)
slight.spotexponent(2)
slight.setPosition(0,1,0)
slight.color(0,0,1)



def Switch(light,checked):
	if not checked :
		light.disable()
	else:
		light.enable()

dlightCheck = viz.addCheckbox()
dlightCheck.message('directional light')
dlightCheck.setPosition(.05,.9) 

plightCheck = viz.addCheckbox()
plightCheck.message('point light')
plightCheck.setPosition(.05,.85)

slightCheck = viz.addCheckbox()
slightCheck.message('spot light')
slightCheck.setPosition(.05,.8)
slightCheck.set(1)

mainCheck = viz.addCheckbox()
mainCheck.message('spot light')
mainCheck.setPosition(.05,.75)

degree = 0
def rotateSpotlight(cx,cz):
	r = 3
	global degree
	degree +=-.1
	x = cx + r * math.cos(degree)
	z = cz + r * math.sin(degree)
	
	slight.setPosition(x,0,z)
	slight.setEuler(degree,0,0)
	cube.setPosition(x,0,z)

	viz.startLayer(viz.POINTS)
	viz.vertexColor(1,0,0)
	viz.vertex(x,0,z)
	viz.vertex(x,0,z+.1)
	viz.endLayer()

def update():
	Switch(dlight,dlightCheck.get())
	Switch(plight,plightCheck.get())
	Switch(slight,slightCheck.get())
	Switch(viz.MainView.getHeadLight(),mainCheck.get())
	rotateSpotlight(shiny.getPosition()[0],shiny.getPosition()[2])

vizact.ontimer(0,update)