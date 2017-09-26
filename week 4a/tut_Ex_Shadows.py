""" 
Demonstrates a method to simulate shadows. 
Move eyes around with the arrow keys and up/down with a/z. 
""" 
import viz
import vizact
import projector

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel()

viz.MainView.setPosition([ 0, 1, 0.5 ])

#Add objects for the shadow to be cast upon
ground = viz.addChild( 'ground.osgb' )

#Sphere to have the shadow cast upon
import vizshape
ball = vizshape.addSphere(pos=(0,0,4))

#Create projector group object
eyeBalls = projector.add( viz.addTexture('eyeshadow.jpg') )

#Point shadow down
eyeBalls.setEuler([ 0, 90, 0 ])


#State the geometry that can have the shadow cast upon them
eyeBalls.affect( ground )
eyeBalls.affect( ball )

#Use a orthographic projection matrix instead of the default perspective projection matrix
eyeBalls.ortho( 0.25, 0.15 )

#Add child geometry that follows shadow around
eyeGeometry = viz.addChild( 'eyeballs.osg' )
eyeGeometry.setParent(eyeBalls)
eyeGeometry.setEuler([ 0, 90, 0 ])
eyeBalls.setPosition([ 0, 1, 3 ])
eyeBalls.addAction( vizact.spin( 0, 0, 1, 90 ) )

#Code to move eyes with the arrow keys
#Ajust elevation with 'a', and 'z'
def MoveEyes():
    if viz.key.isDown(viz.KEY_LEFT):
        eyeBalls.setPosition([-0.05,0,0],viz.REL_PARENT)
    elif viz.key.isDown(viz.KEY_RIGHT):
        eyeBalls.setPosition([0.05,0,0],viz.REL_PARENT)

    if viz.key.isDown(viz.KEY_UP):
        eyeBalls.setPosition([0,0,0.05],viz.REL_PARENT)
    elif viz.key.isDown(viz.KEY_DOWN):
        eyeBalls.setPosition([0,0,-0.05],viz.REL_PARENT)

    if viz.key.isDown('a'):
        eyeBalls.setPosition([0,0.01,0],viz.REL_PARENT)
    elif viz.key.isDown('z'):
        eyeBalls.setPosition([0,-0.01,0],viz.REL_PARENT)

vizact.ontimer(0,MoveEyes)