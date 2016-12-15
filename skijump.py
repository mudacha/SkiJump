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
# loripack1@mail.weber.edu
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
#set scene width height and center it
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

#define skier dudes size and color
dude = box(size=(2.5,2.5,2.5),color=color.blue)
#define the dudes mass as 90kg
dude.mass = 90.0
#set the dude to initially be invisible 
dude.visible=False


# define time step
timeStep = 0.0004

#Define air resistance constant, this is a arbitrary number that represents all of the variables that
# part of air resitance  air density / crossectional drag etc..
drag = -.00006

#define constant for gravity
acclerationDueToGravity = vector(0,-9.8,0)

#define the the frame that will encapsulate the the jump
f = frame()

#slope object stuff
#semicircle defines a path that our extrusion will follow. The path for this is based off an arc and has a defined radius and a starting angle pi to a ending angle which is pi * 1.75
semicircle = paths.arc(radius=23,angle1=pi, angle2 = pi * 1.75)

#rect defines the shape that will be extruded. This is exactly like the shape you can put on a playdough extrusion toy. 
rect = shapes.rectangle(pos=(0,-10), width=5, height=15)

#the ramp object is the extrusion that brings together the path and the shape in order to extrude the ramp shape we want.
#there is a extra parameter called frame that allows us to tie this extrusion to an object. Other wise we could not rotate the extrusion.
ramp = extrusion(frame=f,pos=semicircle, 
          shape=rect, 
          color=color.white)

#set the posistion of the frame object
f.pos = (-20,20,10)

#rotate the frame object about the origin - pi * 1.5
f.rotate(angle=-pi * 1.5, origin=f.pos)

# support for the jump is a box.
jumpSupport = box(pos=(-46,7,0),size=(8,25,20),material = materials.wood)


#Define text that is displayed when the program starts. Text works like an extrussion as you define a position and height and then extrude by defining the depth parameter
intro = text(text='Select A Number Between 1-5',
    align='center', depth=-1.9, color=color.green, height=10,pos=(0,50,0))

#define initial force text variable.
ForceText = text(text=' ')

# define variable for impact force
impactF = vector(0,0,0)


#function air time this function will be in charge of calculations related to the skiers posistion , velocity and impact force as well as some cosmetic features of the program
# This function accepts
def airTime(offsetx,offsety):
    #do all of the calculations listed below until the skier is just above the ground.
    while dude.pos.y > (ground.pos.y + 6):
        #set rate of the loop
        rate(5000)

        #calculate the drag by multipling our drag constant by the dudes velocity in the x direction.
        airDrag = drag  * dude.velocity.x
        #assign airdrag to a vector in the appropriate x posistion
        fD = vector(airDrag,0,0)
        #calculate the new velocity by adding the current velocity to the drag force and accelration due to gravity then multiplying all of that by our timestep
        dude.velocity = dude.velocity + fD + acclerationDueToGravity * timeStep
        #calculate the skiers posistion by adding the current posistion to the dude.velocity * the timestep
        dude.pos = dude.pos + dude.velocity*timeStep

    #set the text color to green
    textColor = color.green
    #calculation for the impact force
    impactF = (0.5 * dude.mass) * dude.velocity.y**2
    #scale the impact force down (This is nessary because our scene isnt quite to scale........)
    impactF = impactF/10

    #Check to see if the impact force is great enough to cause serious injury.
    #if the force is greater then 3000 then change the skier dudes color to red... he is bleading duh ;)
    #if the force is greater then 3000 then also change the text to red as well.
    if impactF > 3300:
        dude.color=color.red
        textColor = color.red
    impactF = format(impactF, '.2f')
    ForceText = text(text='Impact Force = ' + str(impactF) + 'N', align='center', depth=-1.9, color=textColor, height=5, pos=(offsetx,offsety,0))
            

#Ramp function: This function needs to figure out the skiers posistion on the ramp as well as final velocity on the ramp
# that gets passed into the airtime function.
#def onRamp():


# main program loop
while(true):
    #setting the key variable to grab key info
    key = scene.kb.getkey() # wait for and get keyboard info
    #set intro text to be invisible if the user selected a simulation use case
    intro.visible = False
    #make the dude visible
    dude.visible = True
    #reset the dudes starting position
    dude.pos=(-7.7,6,0)

    # if the key input is 1 then set the velocity to the slowest test case
    if key == '1':
        #reset the dudes color
        dude.color=color.blue
        #set the dudes velocity
        dude.velocity = vector(12.0,12.0,0.0)
    # pass in the offset for the result text to the airTime function
        airTime(75,35)
        
    #if the key input 2 then set the initial velocity to a faster test case  
    if key == '2':
        #reset the dudes color
        dude.color=color.blue
        #set the dudes initial velocity
        dude.velocity = vector(16.0,16.0,0.0)
        # pass in the offset for the result text to the airTime function
        airTime(75,45)
        
    #if the key input is 3 then set the initial velocity to a even faster test case
    if key == '3':
        #reset the dudes color
        dude.color=color.blue
        dude.velocity = vector(20.0,20.0,0.0)
        # pass in the offset for the result text to the airTime function
        airTime(75,55)
        
    #if the key input is 4 then set the initial velocity to the second fastest test case
    if key == '4':
        #reset the dudes color
        dude.color=color.blue
        #set the dudes initial velocity
        dude.velocity = vector(24.0,24.0,0.0)
        # pass in the offset for the result text to the airTime function
        airTime(75,65)

    #if the key input is 5 then set the initial velocity to the fastest test case
    if key == '5':
        #reset the dudes color
        dude.color=color.blue
        dude.velocity = vector(28.0,28.0,0.0)
        # pass in the offset for the result text to the airTime function
        airTime(75,75)

    if key == '6':
        intro = text(text='Thanks for using Ski Jump Simulator! ',
    align='center', depth=-1.9, color=color.green, height=10,pos=(0,-50,0))

