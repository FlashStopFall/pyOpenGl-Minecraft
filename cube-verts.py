
def verts(x, y, z, n):
    vertices = (
        (x, -y, -z),
        (x, y, -z),
        (-x, y, -z),
        (-x, -y, -z),
        (x, -y, z),
        (x, y, z),
        (-x, -y, z),
        (-x, y, z)
        )
    return(vertices)

print(verts(1, 1, 1, 1))


surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verts(1, 1, 1, 1)[vertex])
    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
