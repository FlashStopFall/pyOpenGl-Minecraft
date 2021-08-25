import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import functions
import sys



#block type names and location on template go here
BLOCK1 = functions.tex_coords((3, 0), (3, 0), (3, 0))




def verts(x, y, z, n):
    vertices = (
        (1+(2*x), -1+(2*y), -1+(2*z)),
        (1+(2*x), 1+(2*y), -1+(2*z)),
        (-1+(2*x), 1+(2*y), -1+(2*z)),
        (-1+(2*x), -1+(2*y), -1+(2*z)),
        (1+(2*x), -1+(2*y), 1+(2*z)),
        (1+(2*x), 1+(2*y), 1+(2*z)),
        (-1+(2*x), -1+(2*y), 1+(2*z)),
        (-1+(2*x), 1+(2*y), 1+(2*z))
        )
    return(vertices)

print(verts(0, 0, 0, 1))



edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


def Cube(vx,vy,vz):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verts(vx,vy,vz,1)[vertex])
    glEnd()

    """
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verts(vx,vy,vz,1)[vertex])
    glEnd()"""







pygame.init()
display = (800, 600)
<<<<<<< HEAD
scree = pygame.display.set_mode(display, RESIZABLE | DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()

=======
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
>>>>>>> 81640d852cea0e5e7f83e551f8df1ff96492ec8f

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

glEnable(GL_CULL_FACE)
glFrontFace(GL_CCW)
"""
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(1.0)

glDepthMask(GL_TRUE)
glDepthFunc(GL_LESS)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glCullFace(GL_FRONT)
glFrontFace(GL_CCW)
##glShadeModel(GL_SMOOTH)
glDepthRange(0.0,1.0)
"""



sphere = gluNewQuadric() 

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

functions.loadTexture()

up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter) 
        if not paused: 
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)    

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        #mouseMove = pygame.mouse.get_rel()
    
        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment 
        if keypress[pygame.K_w]:
            glTranslatef(0,0,0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0,0,-0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1,0,0)
        if keypress[pygame.K_LSHIFT]:
            glTranslatef(0,0.5,0)
        if keypress[pygame.K_SPACE]:
            glTranslatef(0,-0.5,0)

        # apply the left and right rotation
        glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix 
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        #glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        scree.blit(functions.update_fps(), (10,0))

        glPushMatrix()

<<<<<<< HEAD
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)
        glEnable(GL_TEXTURE_2D)
        functions.Cube(0,0,0,BLOCK1)
        functions.Cube(1,0,0,BLOCK1)
        functions.Cube(0,1,0,BLOCK1)
        functions.Cube(0,0,1,BLOCK1)
        functions.Cube(-2,0,0,BLOCK1)

        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
=======


        Cube(0,0,0)
        Cube(1,0,0)
        Cube(0,1,0)
        Cube(0,0,1)
        Cube(-2,0,0)

>>>>>>> 81640d852cea0e5e7f83e551f8df1ff96492ec8f
        glColor4f(0.5, 0.5, 0.5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-10, -10, -1)
        glVertex3f(10, -10, -1)
        glVertex3f(10, 10, -1)
        glVertex3f(-10, 10, -1)
        glEnd()
        """
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glTranslatef(-1.5, 0, 0)
        glColor4f(0.5, 0.2, 0.2, 1)
        gluSphere(sphere, 1.0, 32, 16)

        glTranslatef(3, 0, 0)
        glColor4f(0.2, 0.2, 0.5, 1)
        gluSphere(sphere, 1.0, 32, 16)
        """
        glColor3f(1, 1, 1)

        glPopMatrix()
        
        clock.tick(60)
        pygame.display.flip()
        print(clock.get_fps())
        pygame.time.wait(10)

pygame.quit()
