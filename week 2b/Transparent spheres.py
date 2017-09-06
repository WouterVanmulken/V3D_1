import viz
import vizshape
import vizact

#1
viz.clearcolor(.5,.5,.5)

viz.MainView.setPosition(0,0,-10)
sphere1 = vizshape.addSphere(2)
sphere1.color(1,0,0)
sphere1.alpha(.3)
sphere1.setPosition(0,0,-1)

sphere2 = vizshape.addSphere(2)
sphere2.color(0,1,0)
sphere2.alpha(.3)

slider = viz.addSlider()
slider.setPosition(.8,.5)

def update():
	sphere2.setPosition(.5,0, -slider.get()*3)

vizact.ontimer(0,update)


viz.go()