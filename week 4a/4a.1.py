import viz
import vizact
import vizfx
import vizconfig
import vizshape
import math


viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.MainView.move([0,1,-3])

vizfx.addChild('lab.osgb')
projectedTexture = viz.addTexture('bricks.jpg')

proj = vizfx.addProjector(projectedTexture,blend=vizfx.BLEND_OVERLAY)
proj.setPosition([0,1.3,0])
proj.setFov(40)


#sphere = vizshape.addSphere(.5)
#sphere.setPosition(0,1,4)


sphere = vizfx.addChild('duck.cfg')
#proj.effect(sphere)

vizfx.getComposer().addEffect(proj.getEffect())



#met projector

#
#
#import viz
#import vizact
#import vizfx
#import vizconfig
#import vizshape
#import math
#import projector
#
#viz.setMultiSample(4)
#viz.fov(60)
#viz.go()
#
#viz.MainView.move([0,1,-3])
#
##lab = viz.addChild('lab.osgb')
#quad = vizshape.addQuad(size=[100,10,10])
#quad.setPosition(0,1,8)
#
#quad2 = vizshape.addQuad(size=[100,10,10])
#quad2.setPosition(0,1,-10)
#quad2.setEuler(180,0,0)
#
#projectedTexture = viz.addTexture('bricks.jpg')
#
#proj = projector.add(projectedTexture)
#proj.setPosition([0,1.3,0])
#
#
#
#sphere = vizshape.addSphere(.5)
#sphere.setPosition(0,1,4)
#
#proj.affect(quad)
#proj.affect(quad2)
#proj.affect(sphere)
#
#angle =0
#speed = 1
#def set_projector():
#	global proj
#	global angle
#	global speed
#	angle += speed
#	proj.setEuler(angle)
#
#vizact.ontimer(0,set_projector)