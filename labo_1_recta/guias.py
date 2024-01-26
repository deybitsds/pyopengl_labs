from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# ALGORITMO DDA
def DDA(x0, y0, x1, y1):
    if x0 == x1:
        for y in range(y0, y1 + 1):
            plot(x0, y)
    else:
        m = (y1 - y0) / (x1 - x0)
        y = y0
        for x in range(x0, x1 + 1):
            plot(x, int(y))
            y = y + m

#ALGORITMO DE LÏNEA DE BRESENHAM
def swap(x, y):
    x, y = y, x
    
def Bresenham(x0, y0, x1, y1):
    dy = 0
    x, y, error = 0, 0, 0
    delta_x, delta_y = 0, 0
    steep = abs(y1 - y0) > abs(x1 - x0)

    if steep:
        swap(x0, y0)
        swap(x1, y1)

    if x0 > x1:
        swap(x0, x1)
        swap(y0, y1)

    if y0 > y1:
        dy = -1
    else:
        dy = 1

    delta_x = x1 - x0
    delta_y = abs(y1 - y0)
    y = y0
    error = 0

    for x in range(x0, x1 + 1):
        if steep:
            plot(y, x)
        else:
            plot(x, y)
        
        error = error + delta_y

        if 2 * error >= delta_x:
            y = y + dy
            error = error - delta_x

# ALGORITMO DE PUNTO MEDIO
def PtoMedio(x0, y0, x1, y1):
    delta_x = x1 - x0
    delta_y = y1 - y0
    dm = 2 * delta_y - delta_x
    dm_p1 = 2 * delta_y
    dm_p2 = 2 * delta_y - 2 * delta_x
    y = y0

    for x in range(x0, x1 + 1):
        plot(x, y)
        if dm <= 0:
            dm = dm + dm_p1
        else:
            dm = dm + dm_p2
            y = y + 1



# DESARROLLO DE LA PRACTICA
def plot(ix, iy):
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    DDA(30, 70, 30, 20)
    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 100.0, 0.0, 100.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Algoritmo de Punto Medio")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()
