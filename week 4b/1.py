import viz
import vizact
import vizshape

viz.MainView.setPosition(0,0,-4)

def makeTree(pos):
	tree =viz.addTexture('tree.png')

	viz.startLayer(viz.QUADS)
	viz.texCoord(0,0)
	viz.vertex(0,0,0)

	viz.texCoord(0,1)
	viz.vertex(0,1,0)

	viz.texCoord(1,1)
	viz.vertex(1,1,0)

	viz.texCoord(1,0)
	viz.vertex(1,0,0)
	quad = viz.endLayer()
	quad.texture(tree)
	quad.setPosition(pos)
	return quad

tree1 = makeTree([0,0,0]);
tree1.billboard(viz.BILLBOARD_VIEW)

tree2 = makeTree([2,0,0]);
tree2.billboard(viz.BILLBOARD_YAXIS)

tree3 = makeTree([4,0,0]);
tree3.billboard(viz.BILLBOARD_VIEW_POS)



viz.go()