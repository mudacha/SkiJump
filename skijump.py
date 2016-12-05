from visual import *

floor = box(pos=(0.0,-5.0,0.0),size=(100.0,0.2,100),material = materials.rough, color=color.white)
treeTop = cone(pos=(-500,-100,-100), axis=(9,0,0), radius=4,color=color.green)
treeTop.pos=(0,5,-40)
treeTop.rotate(angle=pi/2, axis=(0,0,1), origin=treeTop.pos)
f = frame()
semicircle = paths.arc(radius=20,angle1=pi, angle2 = pi * 1.75)
circ = shapes.rectangle(pos=(0,-10), width=10, height=15)
ramp = extrusion(frame=f,pos=semicircle, 
          shape=circ, 
          color=color.white)
f.pos = (-20,20,10)
f.rotate(angle=-pi * 1.5, axi2s=(0,0,1), origin=f.pos)
