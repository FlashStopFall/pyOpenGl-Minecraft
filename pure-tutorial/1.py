import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *


width, height = 500, 400 



def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glutWireTeapot(0.5)
    #glFlush()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA )
glutInitWindowSize(width, height)
glutInitWindowPosition(200, 200)
window = glutCreateWindow("Opengl Window In Python")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
