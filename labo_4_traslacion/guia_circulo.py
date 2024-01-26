from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

width, height, r, change = 0.3, 0, 0.3, 0

# Dibuja círculos
def draw(tx, ty):
    glBegin(GL_LINE_LOOP)
    for i in range(1, 1201):
        theta = (2 * math.pi * i) / 1200
        x1 = r * math.cos(theta) * height / width
        y1 = r * math.sin(theta)
        glVertex3f(x1, y1, 0)
    glEnd()
    glTranslatef(tx, ty, 0)

def display():
    global width, height, r, change
    p = [[0]*2 for _ in range(6)]
    j = 0

    if change == 0:
        change = 1
    elif change == 1:
        change = 0

    width = glutGet(GLUT_WINDOW_WIDTH)
    height = glutGet(GLUT_WINDOW_HEIGHT)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)

    glBegin(GL_LINE_LOOP)
    for i in range(1, 1201):
        theta = (2 * math.pi * i) / 1200
        x1 = r * math.cos(theta) * height / width
        y1 = r * math.sin(theta)
        glVertex3f(x1, y1, 0)

        if i in [100, 300, 500, 700, 900, 1100]:
            if change == 0:
                p[j][0] = x1
                p[j][1] = y1
                j += 1

    glEnd()

    if change == 0:
        for i in range(6):
            draw(p[i][0], p[i][1])

    glutSwapBuffers()

def main():
    global width, height, r, change
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 500)
    glutCreateWindow("Traslacion de circunferencias")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
