import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def tex_coord(x, y, n=4):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = [
        (top),
        (bottom),
        (side),
        (side),
        (side),
        (side),
    ]
    """result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)"""
    return result


#block type names and location on template go here
BLOCK1 = tex_coords((3, 0), (3, 0), (3, 0))


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

print(verts(1, 0, 0, 1))



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


forced = False
def Cube(vx,vy,vz,block):
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)
    glEnable(GL_TEXTURE_2D)
    if not forced:
        glBegin(GL_QUADS)
        y = 0
        for surface in surfaces:
            x = 0
            y+=1
            for vertex in surface:
                x+=1
                #glColor3fv(colors[x])
                glTexCoord2f(block[y-1][2*(x-1)], block[y-1][(2*x)-1])
                #print(block[y-1][2*(x-1)], block[y-1][(2*x)-1])
                glVertex3fv(verts(vx,vy,vz,1)[vertex])
        glEnd()


        glDisable(GL_TEXTURE_2D)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verts(vx,vy,vz,1)[vertex])
        glEnd()
    else:
        texX = 0.75
        texY = 0.25
        glBegin(GL_QUADS)
        glTexCoord2f(0.0+texX, 0.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(0.25+texX, 0.0)
        glVertex3f(1.0, -1.0,  1.0)
        glTexCoord2f(0.25+texX, 0.25)
        glVertex3f(1.0,  1.0,  1.0)
        glTexCoord2f(0.0+texX, 0.25)
        glVertex3f(-1.0,  1.0,  1.0)
        glEnd()


def Plane(tl, tr, bl, br, culling):
    glDisable(GL_CULL_FACE)
    glDisable(GL_TEXTURE_2D)
    glColor4f(0.5, 0.5, 0.5, 1)
    glBegin(GL_QUADS)
    glVertex3f(tl[0], tl[1], tl[2])
    glVertex3f(tr[0], tr[1],  tr[2])
    glVertex3f(bl[0], bl[1], bl[2])
    glVertex3f(br[0], br[1], br[2])
    glEnd()


def loadTexture():
    textureSurface = pygame.image.load('texture2.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glColor3f(0.5, 0.5, 0.5)
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

    glDisable(GL_TEXTURE_2D)

    
pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

