import viz
import vizact
import vizshape


viz.add('gallery.osgb')

text = viz.addText('Gallery',pos=[0,2,4],scale=[0.5]*3)
text.billboard(viz.BILLBOARD_VIEW)
text.alignment(viz.ALIGN_CENTER)
text.resolution(1)
text.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)

text.setAutoScale(True)
text.fontSize(35)

# Add ball fixed to the view  
ball = viz.add('beachball.osgb',pos=(0,0,3))
ball.setReferenceFrame(viz.RF_VIEW)

viz.go()