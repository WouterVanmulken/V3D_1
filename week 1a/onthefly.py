import viz
import vizact
import vizshape
import vizinfo
import vizproximity
import random

viz.setMultiSample(4)
viz.fov(60)
viz.go()

maze = viz.addChild('maze.osgb')
viz.collision(True)
BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
BirdEyeWindow.visible(0,viz.SCREEN)
BirdEyeView = viz.addView()
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0])

viz.startLayer(viz.LINE_STRIP)
viz.vertexColor(viz.RED)
lines = viz.endLayer(parent=viz.ORTHO,scene=BirdEyeWindow)
lines.dynamic()

def UpdatePath():

    # Get main view position in bird eye window pixel coordinates
    x,y,z = BirdEyeWindow.worldToScreen(viz.MainView.getPosition(),mode=viz.WINDOW_PIXELS)

    # Get position of last line vertex
    lx,ly,lz = lines.getVertex(-1)

    # Add new vertex if current position is different from last position
    if x != lx or y != ly:
        lines.addVertex([x,y,0.0])

vizact.ontimer(0,UpdatePath)


vizact.onkeydown(' ',lines.clearVertices)

#Choose random locations for shapes 
locations = [ [9,1.5,-9.5] , [-9.3,1.5,-10] , [7.5,1.5,5.5] , [3,1.5,-9.5] , [-9.4,1.5,3] , [8.8,1.5,10.5] ]
positions = random.sample(locations,3)

pyramid = vizshape.addPyramid(base=(0.5,0.5),height=0.5,pos=positions[0],color=viz.YELLOW)

torus = vizshape.addTorus(axis=vizshape.AXIS_X, pos=positions[1])
torus.texture(viz.addTexture('images/tile_wood.jpg'))

box = vizshape.addBox(pos=positions[2],splitFaces=True)
box.color(viz.SKYBLUE)
box.color(viz.PURPLE,'left')
box.color(viz.PURPLE,'right')

#Animate shapes 
pyramid.addAction(vizact.sequence([vizact.sizeTo(size=[2,2,2],time=1),vizact.sizeTo(size=[1,1,1],time=1)], viz.FOREVER))
x,y,z = box.getPosition()
box.addAction(vizact.sequence([vizact.moveTo(pos=[x,y+0.5,z],time=2),vizact.moveTo(pos=[x,y-0.5,z],time=2)], viz.FOREVER))
torus.addAction(vizact.spin(0,1,0,45))

shapes = [pyramid,torus,box]


# Prevent shapes from rendering to birds eye window 
for s in shapes:
    s.renderToAllWindowsExcept([BirdEyeWindow])
    
    
#Add points for found shapes 
viz.startLayer(viz.POINTS)
viz.pointSize(5)
viz.vertexColor(viz.RED)
points = viz.endLayer()
points.disable(viz.CULLING)
points.renderOnlyToWindows([BirdEyeWindow])

#Create action for when shape is found 
fadeColor = vizact.fadeTo(viz.BLUE,time=2)
fadeAlpha = vizact.fadeTo(0.4,time=3)
fade = vizact.parallel(fadeColor,fadeAlpha)

def FoundShape(e):
    """Called when the viewpoint enters the proximity area of a shape"""

    # Remove shape sensor from proximity manager
    e.manager.removeSensor(e.sensor)

    # Add fade action to shape
    shape = e.sensor.getSourceObject()
    shape.runAction(fade)

    # Add found position to points
    points.addVertex(shape.getPosition())

    # Show message when all shapes have been found
    if not e.manager.getSensors():
        vizinfo.InfoPanel('Good Job! Game over.',align=viz.ALIGN_CENTER,icon=False)
    
# Create proximity manager
manager = vizproximity.Manager()

#Use main viewpoint as proximity target
manager.addTarget(vizproximity.Target(viz.MainView))

# Add a spherical proximity sensor for each shape
sphere = vizproximity.Sphere(2.0)
for s in shapes:
    sensor = vizproximity.Sensor(shape=sphere, source=s)
    manager.addSensor(sensor)
    manager.onEnter(sensor,FoundShape)