import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import functions
import sys



#block type names and location on template go here
BLOCK1 = functions.tex_coords((3, 0), (3, 0), (3, 0))


pygame.init()
display = (800, 600)
scree = pygame.display.set_mode(display, RESIZABLE | DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()


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

steveViewz = 0
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
        if keypress[pygame.K_LSHIFT] and steveViewz > 0:
            glTranslatef(0,0.5,0)
            steveViewz -= 0.5
            print(steveViewz)
        if keypress[pygame.K_SPACE]:
            glTranslatef(0,-0.5,0)
            steveViewz += 0.5
            print(steveViewz)

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

        
        functions.Cube(0,0,0,BLOCK1)
        functions.Cube(1,0,0,BLOCK1)
        functions.Cube(0,1,0,BLOCK1)
        functions.Cube(0,0,1,BLOCK1)
        functions.Cube(-2,0,0,BLOCK1)
        functions.Cube(0,0,3,BLOCK1)
        #functions.Cube(0,-0.5,0,BLOCK1)
        """
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glColor4f(0.5, 0.5, 0.5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-10, -10, -1)
        glVertex3f(10, -10, -1)
        glVertex3f(10, 10, -1)
        glVertex3f(-10, 10, -1)
        glEnd()"""

        functions.Plane((-10, -10, -1), (10, -10, -1), (10, 10, -1), (-10, 10, -1), False)

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
        #print(int(clock.get_fps()))

pygame.quit()
