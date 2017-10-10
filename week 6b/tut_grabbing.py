""" 
Demonstrates the single function creation of a grab object relationship. 
The arrow keys move the hand object. 
The w, a, s, d, keys rotate the hand. 
The t, g, h, f, keys rotate the ball. 
The spacebar toggles the grabbing. 
""" 
import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel()

viz.addChild('ground.osgb')

viz.clearcolor(viz.SLATE)

#Add the object that will do the grabbing
hand = viz.addChild( 'marker.wrl' )
hand.setPosition( [-0.5, 1.8, 2.5] )

#Add the object that the marker will grab
ball = viz.addChild( 'basketball.osgb',scale=[2,2,2] )
ball.setPosition( [0.5, 1.8, 2.5] )

link = None #The handle to the link object

#Grab or let go of the ball
def toggleLink():
    global link
    if link:
        #If link exits, stop grabbing
        link.remove()
        link = None
    else:
        #If no link, grab the ball with the hand
        link = viz.grab( hand, ball )

vizact.onkeydown(' ',toggleLink)


#Setup keyboard control of hand and ball
vizact.whilekeydown(viz.KEY_UP,hand.setPosition,[0,vizact.elapsed(1),0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_DOWN,hand.setPosition,[0,vizact.elapsed(-1),0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_RIGHT,hand.setPosition,[vizact.elapsed(1),0,0],viz.REL_PARENT)
vizact.whilekeydown(viz.KEY_LEFT,hand.setPosition,[vizact.elapsed(-1),0,0],viz.REL_PARENT)

vizact.whilekeydown('w',hand.setEuler,[vizact.elapsed(90),0,0],viz.REL_PARENT)
vizact.whilekeydown('s',hand.setEuler,[vizact.elapsed(-90),0,0],viz.REL_PARENT)
vizact.whilekeydown('d',hand.setEuler,[0,vizact.elapsed(90),0],viz.REL_PARENT)
vizact.whilekeydown('a',hand.setEuler,[0,vizact.elapsed(-90),0],viz.REL_PARENT)

vizact.whilekeydown('t',ball.setEuler,[vizact.elapsed(90),0,0],viz.REL_PARENT)
vizact.whilekeydown('g',ball.setEuler,[vizact.elapsed(-90),0,0],viz.REL_PARENT)
vizact.whilekeydown('h',ball.setEuler,[0,vizact.elapsed(90),0],viz.REL_PARENT)
vizact.whilekeydown('f',ball.setEuler,[0,vizact.elapsed(-90),0],viz.REL_PARENT)