from visual import *
f = frame()
semicircle = paths.arc(radius=20, angle2=pi/1.3)
circ = shapes.rectangle(pos=(-2,3), width=5, height=10)
ramp = extrusion(frame=f,pos=semicircle, 
          shape=circ, 
          color=color.yellow)
f.pos = (-2,3,0)
f.rotate(angle=pi/4, axis=(0,0,1), origin=f.pos)
