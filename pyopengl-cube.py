import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
"""
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-0, 0, -0),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
"""
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



    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verts(vx,vy,vz,1)[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)

    glDepthMask(GL_TRUE)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)
    #glFrontFace(GL_CCW)
    #glShadeModel(GL_SMOOTH)
    glDepthRange(0.0,1.0)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -10)

    glRotatef(25, 2, 1, 0)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

                if event.key == pygame.K_q:
                    glRotatef(5,0,0,1)
                if event.key == pygame.K_e:
                    glRotatef(5,0,0,-1)

                if event.key == pygame.K_w:
                    glRotatef(5,-1,0,0)
                if event.key == pygame.K_s:
                    glRotatef(5,1,0,0)

                if event.key == pygame.K_a:
                    glRotatef(5,0,-1,0)
                if event.key == pygame.K_d:
                    glRotatef(5,0,1,0)

                if event.key == pygame.K_l:
                    gluLookAt(0,0,1,1,0,0,0,1,0)



            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(0,0,0)
        Cube(1,0,0)
        Cube(0,1,0)
        Cube(0,0,1)
        Cube(-2,0,0)
        pygame.display.flip()
        pygame.time.wait(10)

main()
