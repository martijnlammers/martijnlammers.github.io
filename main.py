
##Rubix cube, created by Martijn Lammers 0983308. Final Computer Graphics assignment.
#Import PyOpenGL [smile]
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Set window length and width as constants
WINDOW_LENGTH = 1080
WINDOW_WIDTH = 700

#Set RGB values of colors as constants
RED = 0.8627,0.0784,0.2352
ORANGE = 0.9372,0.5098,0.0784
BLUE = 0.2745,0.5098,0.7058
GREEN = 0.1333,0.5450,0.1333
YELLOW = 1,0.7647,0.0000
WHITE = 1,1,1
BLACK = 0,0,0

#These variables are used for camera angle
x_axis = 0.0
y_axis = 0.0

OPACITY = 0.6
def InitGL(Width, Height): 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

def keyboardInput(*args):
    global x_axis,y_axis
    if args[0] == b'\x1b':  ##Escape : When pressed, quit program.
        pass
    #a button resets the camera by resetting the variables to 0
    elif args[0] == b'a':
        y_axis = 0
        x_axis = 0
    #ZXSC are used to change camera position.
    #Z rotates left
    elif args[0] == b'z':
        y_axis = y_axis - 5
    #X rotates down
    elif args[0] == b'x':
        x_axis = x_axis + 5
    #S rotates up
    elif args[0] == b's':
        x_axis = x_axis - 5
    #C rotates right
    elif args[0] == b'c':
        y_axis = y_axis + 5
        
    #Controls used to rotate slices
    elif args[0] == b'U':   #SHIFT + U, Horizontal top slice 
         #Kind of laziness here I suppose, but rotating one slice three times would be sort of thesame as rotating it the opposite direction.
        rotateSlice("horizontal",0,1,2,9,10,11,18,19,20)  
        rotateSlice("horizontal",0,1,2,9,10,11,18,19,20)
        rotateSlice("horizontal",0,1,2,9,10,11,18,19,20)
    elif args[0] == b'L':   #SHIFT + L, Vertical left slice 
        rotateSlice("vertical",0,3,6,9,12,15,18,21,24) 
    elif args[0] == b'F':   #SHIFT + F, Front slice 
        rotateSlice("stacked",0,1,2,3,4,5,6,7,8)   
    elif args[0] == b'R':   #SHIFT + R, Vertical right slice 
        rotateSlice("vertical",2,5,8,11,14,17,20,23,26)   
        rotateSlice("vertical",2,5,8,11,14,17,20,23,26)   
        rotateSlice("vertical",2,5,8,11,14,17,20,23,26) 
    elif args[0] == b'B':   #SHIFT + B, Back slice 
        rotateSlice("stacked",18,19,20,21,22,23,24,25,26) 
        rotateSlice("stacked",18,19,20,21,22,23,24,25,26)    
        rotateSlice("stacked",18,19,20,21,22,23,24,25,26)   
    elif args[0] == b'D':   #SHIFT + D, Horizontal bottom slice 
        rotateSlice("horizontal",6,7,8,15,16,17,24,25,26)  
        
    elif args[0] == b'\x15':   #CTRL + U, Inverse Horizontal top slice 
        rotateSlice("horizontal",0,1,2,9,10,11,18,19,20)  
    elif args[0] == b'\x0c':   #CTRL + L, Inverse Vertical left slice 
        rotateSlice("vertical",0,3,6,9,12,15,18,21,24) 
        rotateSlice("vertical",0,3,6,9,12,15,18,21,24) 
        rotateSlice("vertical",0,3,6,9,12,15,18,21,24) 
    elif args[0] == b'\x06':   #CTRL + F, Inverse Front slice 
        rotateSlice("stacked",0,1,2,3,4,5,6,7,8) 
        rotateSlice("stacked",0,1,2,3,4,5,6,7,8) 
        rotateSlice("stacked",0,1,2,3,4,5,6,7,8) 
    elif args[0] == b'\x12':   #CTRL + R, Inverse Vertical right slice 
        rotateSlice("vertical",2,5,8,11,14,17,20,23,26)    
    elif args[0] == b'\x02':   #CTRL + B, Inverse Back slice 
        rotateSlice("stacked",18,19,20,21,22,23,24,25,26)   
    elif args[0] == b'\x04':   #CTRL + D, Inverse Horizontal bottom slice 
        rotateSlice("horizontal",6,7,8,15,16,17,24,25,26)  
        rotateSlice("horizontal",6,7,8,15,16,17,24,25,26)  
        rotateSlice("horizontal",6,7,8,15,16,17,24,25,26)  
        
        
    elif args[0] == b'M':   #M, Inverse Horizontal top slice 
        rotateSlice("vertical",1,4,7,10,13,16,19,22,25)  
    elif args[0] == b'\r':   #CTRL + L, Inverse Vertical left slice 
        rotateSlice("vertical",1,4,7,10,13,16,19,22,25) 
        rotateSlice("vertical",1,4,7,10,13,16,19,22,25) 
        rotateSlice("vertical",1,4,7,10,13,16,19,22,25) 
    elif args[0] == b'E':   #E, Inverse Front slice 
        rotateSlice("horizontal",3,4,5,12,13,14,21,22,23)
    elif args[0] == b'\x05':   #CTRL + R, Inverse Vertical right slice 
        rotateSlice("horizontal",3,4,5,12,13,14,21,22,23)
        rotateSlice("horizontal",3,4,5,12,13,14,21,22,23)
        rotateSlice("horizontal",3,4,5,12,13,14,21,22,23)        
    elif args[0] == b'S':   #S, Inverse Back slice 
        rotateSlice("stacked",9,10,11,12,13,14,15,16,17)    
    elif args[0] == b'\x13':   #CTRL + D, Inverse Horizontal bottom slice 
        rotateSlice("stacked",9,10,11,12,13,14,15,16,17)  
        rotateSlice("stacked",9,10,11,12,13,14,15,16,17)  
        rotateSlice("stacked",9,10,11,12,13,14,15,16,17)  
        
def rotateSlice(string, front_left_top, front_left, front_left_bottom, middle_left_top, middle_left, middle_left_bottom, back_left_top, back_left, back_left_bottom):
    
    #Save the cubes in temporary variables so the original will be kept after changing the other colors to new ones.
    temp1 = singleCubePositions[front_left_top]
    temp2 = singleCubePositions[front_left]
    temp3 = singleCubePositions[front_left_bottom]
    
    temp4 = singleCubePositions[middle_left_top]
    temp5 = singleCubePositions[middle_left]
    temp6 = singleCubePositions[middle_left_bottom]
    
    temp7 = singleCubePositions[back_left_top]
    temp8 = singleCubePositions[back_left]
    temp9 = singleCubePositions[back_left_bottom]
    
    #This is very ugly code, but it happened to work better than rotating individual cubits. This method will just change the colours of the squares.
    if(string=="vertical"):
        temp10 = temp9.color_left
        temp11 = temp9.color_bottom
        temp12 = temp9.color_back
        temp13 = temp9.color_right
        
        temp14 = temp6.color_left
        temp15 = temp6.color_bottom
        temp16 = temp6.color_right
    
        singleCubePositions[middle_left_bottom].setColour(BLACK,temp2.color_left,temp2.color_right,BLACK,BLACK,temp2.color_front)
        singleCubePositions[back_left_bottom].setColour(BLACK,temp3.color_left,temp3.color_right,BLACK,temp3.color_bottom,temp3.color_front)
        singleCubePositions[front_left_bottom].setColour(BLACK,temp1.color_left,temp1.color_right,temp1.color_top,BLACK,temp1.color_front)
        singleCubePositions[front_left_top].setColour(temp7.color_back, temp7.color_left, temp7.color_right, temp7.color_top, BLACK, BLACK)
        singleCubePositions[front_left].setColour(BLACK,temp4.color_left,temp4.color_right,temp4.color_top,BLACK,BLACK)
        singleCubePositions[middle_left_top].setColour(temp8.color_back,temp8.color_left,temp8.color_right,BLACK,BLACK,BLACK)
        singleCubePositions[back_left_top].setColour(temp12,temp10,temp13,BLACK,temp11,BLACK)
        singleCubePositions[back_left].setColour(BLACK,temp14,temp16,BLACK,temp15,BLACK)
        
    elif(string=="horizontal"):
        temp10 = temp9.color_right
        temp11 = temp9.color_back
        temp12 = temp9.color_top
        temp13 = temp9.color_bottom
        
        temp14 = temp6.color_right
        temp15 = temp6.color_top
        temp16 = temp6.color_bottom
        
        singleCubePositions[middle_left_bottom].setColour(temp2.color_top,BLACK,temp2.color_front,BLACK,BLACK,temp2.color_bottom)
        singleCubePositions[back_left_bottom].setColour(temp3.color_top,BLACK,temp3.color_front,BLACK,temp3.color_right,temp3.color_bottom)
        singleCubePositions[front_left_bottom].setColour(temp1.color_top,BLACK,temp1.color_front,temp1.color_left,BLACK,temp1.color_bottom)
        singleCubePositions[front_left_top].setColour(temp7.color_top,temp7.color_back,BLACK,temp7.color_left,BLACK,temp7.color_bottom)
        singleCubePositions[front_left].setColour(temp4.color_top,BLACK,BLACK,temp4.color_left,BLACK,temp4.color_bottom)
        singleCubePositions[middle_left_top].setColour(temp8.color_top,temp8.color_back,BLACK,BLACK,BLACK,temp8.color_bottom)
        singleCubePositions[back_left_top].setColour(temp12,temp11,BLACK,BLACK,temp10,temp13)
        singleCubePositions[back_left].setColour(temp15,BLACK,BLACK,BLACK,temp14,temp16)
    
    elif(string=="stacked"):
        temp10 = temp9.color_right
        temp11 = temp9.color_front
        temp12 = temp9.color_back
        temp13 = temp9.color_bottom
        
        temp14 = temp6.color_front
        temp15 = temp6.color_back
        temp16 = temp6.color_right
        
        singleCubePositions[middle_left_bottom].setColour(BLACK,BLACK,temp2.color_top,temp2.color_front,temp2.color_back,BLACK)
        singleCubePositions[back_left_bottom].setColour(BLACK,BLACK,temp3.color_top,temp3.color_front,temp3.color_back,temp3.color_right)
        singleCubePositions[front_left_bottom].setColour(temp1.color_left,BLACK,temp1.color_top,temp1.color_front,temp1.color_back,BLACK)
        singleCubePositions[front_left_top].setColour(temp7.color_left,temp7.color_bottom,BLACK,temp7.color_front,temp7.color_back,BLACK)
        singleCubePositions[front_left].setColour(temp4.color_left,BLACK,BLACK,temp4.color_front,temp4.color_back,BLACK)
        singleCubePositions[middle_left_top].setColour(BLACK,temp8.color_bottom,BLACK,temp8.color_front,temp8.color_back,BLACK)
        singleCubePositions[back_left_top].setColour(BLACK,temp13,BLACK,temp11,temp12,temp10)
        singleCubePositions[back_left].setColour(BLACK,BLACK,BLACK,temp14,temp15,temp16)
        
        
   
class SingleCube():
    #Constructor sets the colors of a cubit
    def __init__(self,color_top, color_left, color_right, color_front, color_back, color_bottom):
        self.color_top = color_top
        self.color_left = color_left
        self.color_right = color_right
        self.color_front = color_front
        self.color_back = color_back
        self.color_bottom = color_bottom
    #Function to change all the colors.
    def setColour(self, color_top, color_left, color_right, color_front, color_back, color_bottom):
        self.color_top = color_top
        self.color_left = color_left
        self.color_right = color_right
        self.color_front = color_front
        self.color_back = color_back
        self.color_bottom = color_bottom
        
    #Draws squares at certain coordinates and colors them.
    def draw(self):
        global OPACITY
        glBegin(GL_QUADS)#Tell opengl I'm about to draw something
        
        #Top pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_top[0],self.color_top[1],self.color_top[2], OPACITY])
        glNormal(0, 1, 0)
        glVertex3f( 0.25, 0.25,-0.25)
        glVertex3f(-0.25, 0.25,-0.25)
        glVertex3f(-0.25, 0.25, 0.25)
        glVertex3f( 0.25, 0.25, 0.25) 
        
        #Bottom pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_bottom[0],self.color_bottom[1],self.color_bottom[2], OPACITY]) 
        glNormal(0, -1, 0)
        glVertex3f( 0.25,-0.25, 0.25)
        glVertex3f(-0.25,-0.25, 0.25)
        glVertex3f(-0.25,-0.25,-0.25)
        glVertex3f( 0.25,-0.25,-0.25) 
        
        #Back pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_back[0],self.color_back[1],self.color_back[2], OPACITY]) 
        glNormal(0, 0, -1)
        glVertex3f( 0.25,-0.25,-0.25)
        glVertex3f(-0.25,-0.25,-0.25)
        glVertex3f(-0.25, 0.25,-0.25)
        glVertex3f( 0.25, 0.25,-0.25)
       
        #Front pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_front[0],self.color_front[1],self.color_front[2], OPACITY]) 
        glNormal(0, 0, 1)
        glVertex3f( 0.25, 0.25, 0.25)
        glVertex3f(-0.25, 0.25, 0.25)
        glVertex3f(-0.25,-0.25, 0.25)
        glVertex3f( 0.25,-0.25, 0.25)
        
        #Right pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_right[0],self.color_right[1],self.color_right[2], OPACITY])
        glNormal(1, 0, 0)
        glVertex3f( 0.25, 0.25,-0.25) 
        glVertex3f( 0.25, 0.25, 0.25)
        glVertex3f( 0.25,-0.25, 0.25)
        glVertex3f( 0.25,-0.25,-0.25)
        
        #Left pane
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [self.color_left[0],self.color_left[1],self.color_left[2], OPACITY]) 
        glNormal(-1, 0, 0)
        glVertex3f(-0.25, 0.25, 0.25) 
        glVertex3f(-0.25, 0.25,-0.25)
        glVertex3f(-0.25,-0.25,-0.25) 
        glVertex3f(-0.25,-0.25, 0.25) 
        glEnd()
        
#Function 'translateAndDraw' is used to translate the cubits to the correct position. Takes in arguments: Position in cubits array and xyz coordinates of translation.
#Mainly used to shorten code.
def translateAndDraw(number,x,y,z):

    glTranslate(x,y,z)
    glPushMatrix()
    #Function draw creates the cubit 
    singleCubePositions[number].draw()
    glPopMatrix()

    
def drawInstructions():
    glPushMatrix()
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 1, 1]) 
    glTranslate(-2.5,-1.5,-3)
    
    glPopMatrix()
    
def drawRubixCube():
   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #Save current matrix to pop at the end of drawing.
    drawInstructions()
    
    glPushMatrix()
    #Rotate pseudo camera based on user key input in order to look at different angles at the cube.
    glRotatef(x_axis,1.0,0.0,0.0)
    glRotatef(y_axis,0.0,1.0,0.0)
    
    glRotatef(20,0,1.0,0.0)
    glTranslate(-0.5,0.5,0.5)
    #Scale the cube down to fit better in the screen.
    glScalef(0.75,0.75,0.75);

    #Draw 3x3x1 frontal pane
    #Left 1x3x1 pillar
    translateAndDraw(0,0,0,0)
    translateAndDraw(3,0,-0.6,0)
    translateAndDraw(6,0,-0.6,0)
    #Middle 1x3x1 pillar
    translateAndDraw(1,0.6,1.2,0)
    translateAndDraw(4,0,-0.6,0)
    translateAndDraw(7,0,-0.6,0)
    #Right 1x3x1 pillar
    translateAndDraw(2,0.6,1.2,0)
    translateAndDraw(5,0,-0.6,0)
    translateAndDraw(8,0,-0.6,0)
    
    #Draw 3x3x3 middle pane
    #Left 1x3x1 pillar
    translateAndDraw(9,-1.2,1.2,-0.6)
    translateAndDraw(12,0,-0.6,0)
    translateAndDraw(15,0,-0.6,0)
    #Middle 1x3x1 pillar
    translateAndDraw(10,0.6,1.2,0)
    translateAndDraw(13,0,-0.6,0)
    translateAndDraw(16,0,-0.6,0)
    #Right 1x3x1 pillar
    translateAndDraw(11,0.6,1.2,0)
    translateAndDraw(14,0,-0.6,0)
    translateAndDraw(17,0,-0.6,0)
    
    #Draw 3x3x1 back pane
    #Left 1x3x1 pillar
    translateAndDraw(18,-1.2,1.2,-0.6)
    translateAndDraw(21,0,-0.6,0)
    translateAndDraw(24,0,-0.6,0)
    #Middle 1x3x1 pillar
    translateAndDraw(19,0.6,1.2,0)
    translateAndDraw(22,0,-0.6,0)
    translateAndDraw(25,0,-0.6,0)
    #Right 1x3x1 pillar
    translateAndDraw(20,0.6,1.2,0)
    translateAndDraw(23,0,-0.6,0)
    translateAndDraw(26,0,-0.6,0)
    
    #Create a pseudo glass cube around the Rubix cube for sake of aesthetics.
    glTranslate(-0.6,0.6,0.6)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0, 0, 0, 1]) #First three parameters are RGB values, 4th is opacity.
    glutSolidCube(1.6)
    
    #Pop the matrix that was active before started to draw the Rubix cube.
    glPopMatrix()
    glutSwapBuffers()
    
#Set the positions of all the single cubits objects in an array in order to rotate the colors of the sides later. Constructor takes in colors to paint the panes.
#In order : top color, left color, right color, front color, back color, bottom color. (Assumed you look at it when its in front of you)

                        #Front pane
singleCubePositions = [SingleCube(WHITE,BLUE,BLACK,ORANGE,BLACK,BLACK),SingleCube(WHITE,BLACK,BLACK,ORANGE,BLACK,BLACK),SingleCube(WHITE,BLACK,GREEN,ORANGE,BLACK,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,ORANGE,BLACK,BLACK),SingleCube(BLACK,BLACK,BLACK,ORANGE,BLACK,BLACK),SingleCube(BLACK,BLACK,GREEN,ORANGE,BLACK,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,ORANGE,BLACK,YELLOW),SingleCube(BLACK,BLACK,BLACK,ORANGE,BLACK,YELLOW),SingleCube(BLACK,BLACK,GREEN,ORANGE,BLACK,YELLOW),
                        #Middle pane  
                       SingleCube(WHITE,BLUE,BLACK,BLACK,BLACK,BLACK),SingleCube(WHITE,BLACK,BLACK,BLACK,BLACK,BLACK),SingleCube(WHITE,BLACK,GREEN,BLACK,BLACK,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,BLACK,BLACK,BLACK),SingleCube(BLACK,BLACK,BLACK,BLACK,BLACK,BLACK),SingleCube(BLACK,BLACK,GREEN,BLACK,BLACK,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,BLACK,BLACK,YELLOW),SingleCube(BLACK,BLACK,BLACK,BLACK,BLACK,YELLOW),SingleCube(BLACK,BLACK,GREEN,BLACK,BLACK,YELLOW),
                        #Back pane 
                       SingleCube(WHITE,BLUE,BLACK,BLACK,RED,BLACK),SingleCube(WHITE,BLACK,BLACK,BLACK,RED,BLACK),SingleCube(WHITE,BLACK,GREEN,BLACK,RED,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,BLACK,RED,BLACK),SingleCube(BLACK,BLACK,BLACK,BLACK,RED,BLACK),SingleCube(BLACK,BLACK,GREEN,BLACK,RED,BLACK),
                       SingleCube(BLACK,BLUE,BLACK,BLACK,RED,YELLOW),SingleCube(BLACK,BLACK,BLACK,BLACK,RED,YELLOW),SingleCube(BLACK,BLACK,GREEN,BLACK,RED,YELLOW)]
                                     
glutInit() #Glut initialization 
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH) 
glutInitWindowSize(WINDOW_LENGTH, WINDOW_WIDTH) #Create a window with given length and width
glutCreateWindow("Rubix Cube") #Open the window with parameter as window title.
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glFrustum(-1.333, 1.333, -1, 1, 5, 20) #Use projection matrix
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, 0, 8, 0, 0, 0, 0, 1, 0) #Create the point you're looking at the scene
glEnable(GL_RESCALE_NORMAL)

#glPolygonMode(GL_BACK, GL_FILL)    #<-Debug mode for vectors I suppose.
#glPolygonMode(GL_FRONT, GL_LINE)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0) #Create a light source
glLight(GL_LIGHT0, GL_POSITION, [2, 1, 8]) #Position of the light source
glLight(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8]) 
glLight(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2])
glLight(GL_LIGHT0, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glutDisplayFunc(drawRubixCube) #Call the function that needs to draw the shapes/objects
glutKeyboardFunc(keyboardInput) #Use function 'keyboardInput' in order to handle key activations
glutIdleFunc(glutPostRedisplay) #Redraw the scene even when you're not actively using it
glutMainLoop()


    