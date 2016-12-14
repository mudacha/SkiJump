#----------------------------------------------------------------------------
# G e n e r a l I n f o r m a t i o n
#---------------------------------------------------------------------------
# Name: skijump.py
#
# Usage: Ski jump simulation
#
# Description: This program is responsible for running a simulation of a snow sports enthusiast traveling down a ramp and launching into the air.
# 
#
#
# Special Instructions: When the program is ran, in order to run a particular simulation simply
# select a number between one and five. 1 being the slowest initial velocity for the skier
# and 5 being the fastest initial velocity for the skier.
#
#----------------------------------------------------------------------------

#C o d e H i s t o r y
#----------------------------------------------------------------------------
# Version: 1.0
#
# Author(s): Haydn Hunt , Cory Dunn , And Lori Pack
# haydnhunt@mail.weber.edu
# corydunn@mail.weber.edu
# loripack@mail.weber.edu
#
# Modifications: Modification details can be found at https://github.com/mudacha/SkiJump 
#
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# I m p o r t L i b r a r i e s
#----------------------------------------------------------------------------
from visual import *

# D e f i n e C o n s t a n t s
#----------------------------------------------------------------------------

#initilize scene
scene = display(title='Ski Jump Simulation', x=0, y=0,
                width=2000, height=2000, center=(0,2,0),
                autoscale=True, background=(0,1,1))

# class "Tree" defines a abstract tree object template that is built up of a cylinder and a cone that have been appended to a
#composite frame object. The class has a construction method that accepts an additonal parameters specifiying the x, y, and  location offsets. 
class Tree:
    def __init__(self, pos):
        treeFrame = frame()
        treeTrunk = cylinder(frame=treeFrame , pos=(-3,0,0), axis=(9,0,0), radius=1, material = materials.wood)
        treeTop = cone(frame = treeFrame, pos=(5,0,0), axis=(9,0,0), radius=4,color=color.green)
        treeFrame.axis = (0,1,0) # change orientation of both objects
        treeFrame.pos = (pos[0],pos[1],pos[2]) # change position of both objects


#set up some locations that we want to show a tree
        # locations is an array that contains arrays that specify the x y and z offset of where we want to display a tree.
locations = [[-100,-3,-10],[-93,-4,-20],[-85,-4,-15],[-76,-5,-22],[-65,-5,-13],[-60,-5,-14],[-50,-5,-25],[-33,-5,-27],[-23,-2,-10],[-15,-4,-20],
             [2,-5,-23],[13,-5,-12],[21,-5,-19],[30,-5,-16],[44,-5,-11],[52,-5,-22],[64,-2,-15],[71,-3,-26],[80,-4,-24],[90,-5,-15],[96,-3,-23]]

#for every location that we specified above, call the tree contructor passing in the location offsets.
for each in locations:
    NewTree = Tree(each)

        
# This box will specify the ground will be used as the ground that our test subject will land on 
ground = box(pos=(0.0,-8.0,0.0),size=(200.0,8,75),material = materials.rough, color=color.white)
#define tree frame objects

dude = box(size=(2.5,2.5,2.5),color=color.blue)
dude.mass = 90.0
dude.visible=False
# define time step
timeStep = 0.0004

#Define air resistance constant, this is a arbitrary number that represents all of the variables that
# part of air resitance  air density / crossectional drag etc..
drag = -.00006

#define constant for gravity
acclerationDueToGravity = vector(0,-9.8,0)
f = frame(color=color.green)
#slope object stuff
semicircle = paths.arc(radius=23,angle1=pi, angle2 = pi * 1.75)
rect = shapes.rectangle(pos=(0,-10), width=5, height=15)
ramp = extrusion(frame=f,pos=semicircle, 
          shape=rect, 
          color=color.white)

f.pos = (-20,20,10)
f.rotate(angle=-pi * 1.5, origin=f.pos)
# support for the jump
jumpSupport = box(pos=(-46,7,0),size=(8,25,20),material = materials.wood)

intro = text(text='Select A Number Between 1-5',
    align='center', depth=-1.9, color=color.green, height=10,pos=(0,50,0))
ForceText = text(text=' ')
impactF = vector(0,0,0)

def airTime():
    while dude.pos.y > (ground.pos.y + 6):
        rate(5000)

        airDrag = drag  * dude.velocity.x
        fD = vector(airDrag,0,0)
        dude.velocity = dude.velocity + fD + acclerationDueToGravity * timeStep
        dude.pos = dude.pos + dude.velocity*timeStep

            ## TODO calculate the impact force by taking the derivitie of the velocity to get the accleration then times that by the mass
            ## if dude.pos = stop condition -.1 so he is at ground.pos +5.99
            ## forcetext = text(text='calculation' + N,  align='center', depth=-1.9, color=color.green, height=10,pos=(0,50,0))

    #impactF = (1/2) * dude.mass * dude.velocity**2
    ForceText = text(text='Impact Force =  N', align='center', depth=-1.9, color=color.green, height=10, pos=(0,50,0))
            

#Ramp function: This function needs to figure out the skiers posistion on the ramp as well as final velocity on the ramp
# that gets passed into the airtime function.
#def onRamp():


# main program loop
while(true):
    key = scene.kb.getkey() # wait for and get keyboard info
    intro.visible = False
    ForceText.visible = False
    dude.visible = True
    dude.pos=(-2,6,0)
        
    if key == '1':
        ForceText.visible = False
        dude.velocity = vector(12.0,12.0,0.0)
        airTime()
            
    if key == '2':
        ForceText.visible = False
        dude.velocity = vector(16.0,16.0,0.0)
        airTime()
        
    if key == '3':
        ForceText.visible = False
        dude.velocity = vector(18.0,18.0,0.0)
        airTime()

    if key == '4':
        ForceText.visible = False
        dude.velocity = vector(22.0,22.0,0.0)
        airTime()

    if key == '5':
        ForceText.visible = False
        dude.velocity = vector(25.0,25.0,0.0)
        airTime()

    if key == '6':
        ForceText.visible = False
        intro = text(text='Thanks for using Ski Jump Simulator! ',
    align='center', depth=-1.9, color=color.green, height=10,pos=(0,50,0))


