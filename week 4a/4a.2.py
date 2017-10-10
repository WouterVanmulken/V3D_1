import Shadow
import viz
import vizshape
import vizact
import vizfx

lab = viz.addChild('lab.osgb')

sphere1 = vizshape.addSphere()
sphere1.setPosition(0,1,4)

quad1 = vizshape.addQuad(size=[10,10,10])
quad1.setPosition(0,1,8)

quad2 = vizshape.addQuad(size=[10,10,10])
quad2.setPosition(0,1,-8)
quad2.setEuler(180,0,0)

SHADOW_RES = 1000
SHADOW_POS = [0,0,0]
SHADOW_AREA = [20,20]
	

shadow = Shadow.ShadowProjector(size=SHADOW_RES, pos=SHADOW_POS, area=SHADOW_AREA)
shadow.setEuler([0,0,0]);
shadow.addCaster(sphere1)

shadow.addReceiver(quad1)
shadow.addReceiver(quad2)
shadow.addReceiver(lab)


light = vizfx.addDirectionalLight(euler=(0,90,0), color=viz.WHITE)


angle = 0
speed = .1
def setPos():
	global SHADOW_POS
	global angle
	global speed
	
	angle +=speed
	shadow.setPosition([angle,0,0])

#vizact.ontimer(0,setPos)
viz.go()