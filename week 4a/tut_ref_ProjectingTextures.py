import viz
import projector
viz.go()

viz.MainView.setPosition([0,1,-1])

#Add objects for the shadow to be cast upon
ground = viz.add('tut_ground.wrl')

#Sphere to have the shadow cast upon
ball = viz.add('white_ball.wrl')
ball.setScale([10,10,10])
ball.setPosition([0,0,4])

#Create projector group object
eyeBalls = projector.add(viz.add('eyeshadow.jpg'))

#Point shadow down
eyeBalls.setEuler([0,90,0])

#State the geometry that can have the shadow cast upon them
eyeBalls.affect(ground)
eyeBalls.affect(ball)

#Use a orthographic projection matrix instead of the default perspective projection matrix
eyeBalls.ortho(0.25,0.15)

#Add child geometry that follows shadow around
eyeGeometry = eyeBalls.add('eyeballs.osg')
eyeGeometry.setEuler([0,90,0])
eyeBalls.setPosition([0,1,3])
eyeBalls.addAction( vizact.spin(0,0,1,90))