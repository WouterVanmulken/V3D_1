import viz
import vizact
import vizshape
import vizinfo

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
viz.vertexColor(viz.YELLOW)
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