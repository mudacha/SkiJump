from visual import *

scene = display(title='Projectile Motion', x=0, y=0,
                width=2000, height=2000, center=(0,2,0),
                autoscale=True, background=(0,1,1))
class Tree:
    def __init__(self, xpos):
        treeFrame = frame()
        treeTrunk = cylinder(frame=treeFrame , pos=(0,0,0), axis=(5,0,0), radius=1, material = materials.wood)
        treeTop = cone(frame = treeFrame, pos=(5,0,0), axis=(9,0,0), radius=4,color=color.green)
        treeFrame.axis = (0,1,0) # change orientation of both objects
        treeFrame.pos = (xpos,-5,-20) # change position of both objects


#set up some locations that we want to show a tree
locations = [-100,-93,-85,-76,-65,-60,-50,-33,-23,-15,2,13,21,30,44,52,64,71,80,90,96]
for each in locations:
    NewTree = Tree(each)

        
# This floor will be used as the ground that our border will land on 
floor = box(pos=(0.0,-8.0,0.0),size=(200.0,8,50),material = materials.rough, color=color.white)
#define tree frame objects

dude = box(pos=(0,7,0),size=(2.5,2.5,2.5),color=color.blue);

f = frame()
#slope object stuff
semicircle = paths.arc(radius=23,angle1=pi, angle2 = pi * 1.75)
circ = shapes.rectangle(pos=(0,-10), width=5, height=15)
ramp = extrusion(frame=f,pos=semicircle, 
          shape=circ, 
          color=color.white)
# support for the jump
jumpSupport = box(pos=(-46,7,0),size=(8,25,20),material = materials.wood)
f.pos = (-20,20,10)
f.rotate(angle=-pi * 1.5, origin=f.pos)
