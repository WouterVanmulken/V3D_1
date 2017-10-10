import viz


 

#Create some objects. 
for i in range(10): 
    viz.add('wheelbarrow.ive').setPosition(i,0,0) 
#Create an action to cue. 
MouseOverAction = vizact.fadeTo(1,begin=0,time=1) 

def picker(): 
    #Check if the mouse is over one of the boxes 
    item = viz.MainWindow.pick( info = True ) 
    #If there is an intersection 
    if item.valid: 
        #Add mouse over action 
        item.object.runAction(MouseOverAction) 
        #Print the point where the line intersects the object. 
        print item.point 

#Start a timer to execute picker repeatedly. 
vizact.ontimer(.1, picker )


#Add a node to apply an action to. 
myNode = viz.add( 'logo.wrl' ) 
#Add the node that you'll pick.  
myPicker = viz.add( 'box.wrl' ) 
myPicker.setPosition( 2,0,0 ) 
#Add an action. 
quickSpin = vizact.spin( 0,1,0, 90, 3 ) 
#Apply the action to the node when you pick the other object. 
vizact.onpick( myPicker, myNode.runAction, quickSpin ) 
viz.MainView.setPosition(.5,0,-5) 



viz.go();