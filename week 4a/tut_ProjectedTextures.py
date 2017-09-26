""" 
This script demonstrates how to project textures onto objects. 
The texture is being projected from a position above the origin. 
Use the controls to adjust the projection FOV and alpha. 
""" 
import viz
import vizfx
import vizact
import vizconfig
import math

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel()

#Move the viewpoint
viz.MainView.move([0,1,-3])

# Add environment
vizfx.addChild('lab.osgb')

# Add objects to environment
##vizfx.addChild('beachball.osgb', pos=(-1.5,2,3.5))
#vizfx.addChild('logo.osgb',pos=(0,1,3.5))
#vizfx.addChild('plant.osgb',pos=(1.5,1,3.5))

# Add a texture which will be projected
texture = viz.addTexture('image2.jpg')

# Create a projector using the texture
proj = vizfx.addProjector(texture, blend=vizfx.BLEND_OVERLAY)

# Translate the projector to the center of the room
proj.setPosition([0,1.3,0])

#Set the projectors fov
proj.setFov(40)

# Apply the projector effect to the global composer
vizfx.getComposer().addEffect(proj.getEffect())







#Create a yaw variable for the projector
proj.yaw = 0

def AnimateProjector():

    #Have the projector look around in a circle
    proj.yaw += viz.getFrameElapsed() * 60.0

    x = math.sin(viz.radians(proj.yaw))
    y = math.cos(viz.radians(proj.yaw))

    proj.lookAt([x,1.3+y,5])

vizact.ontimer(0, AnimateProjector)

# Setup controls to configure projector
bc = vizconfig.BasicConfigurable('Projector')
bc.addFloatRangeItem('FOV',[10,90],fset=proj.setFov,fget=lambda:proj.getProjectionMatrix().getVerticalFOV())
bc.addFloatRangeItem('Alpha',[0,1],fset=proj.setAlpha,fget=proj.getAlpha)
vizconfig.register(bc)
vizconfig.getConfigWindow().setWindowVisible(True)