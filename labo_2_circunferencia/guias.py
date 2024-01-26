# Importamos las librerias a usar
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Implementación de los algoritmos de círcunfencia ------------------------------------
''' 2 VIAS '''
def circulo2vias(x0, y0, r):
    y = 0 
    plot(x0 + r, y0)
    plot(x0 - r, y0)

    for x in range(-r + 1, r):
        y = int(math.floor(math.sqrt(r * r - x * x) + 0.5))
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)

''' 4 VIAS '''
def circulo4vias(x0, y0, r):
    y = 0
    plot(x0, y0 + r)
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)

    for x in range(1, r):
        y = math.floor(math.sqrt(r * r - x * x) + 0.5)
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)

''' 8 VIAS '''
def circulo8vias(x0, y0, r):
    plot(x0, y0 + r)
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)
    x = 1
    y = math.floor(math.sqrt(r * r - x * x) + 0.5)
    while x < y:
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)

        x = x + 1
        y = math.floor(math.sqrt(r * r - x * x) + 0.5)

        if x == y:
            plot(x0 + x, y0 + y)
            plot(x0 + x, y0 - y)
            plot(x0 - x, y0 + y)
            plot(x0 - x, y0 - y)

''' MIDPOINT '''
def circuloPtoMedio(x0, y0, r):
    hm, x,y = 5 / 4 - r, 0, -r
    plot(x0, y0 + r)
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)
    while x < -(y + 1):
        if hm < 0:
            hm = hm + 2 * x + 3
        else:
            hm = hm + 2 * x + 2 * y + 5
            y = y + 1
        x = x + 1
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)


# Función para mostrar el grafico ------------------------------------

# Función para dibujar un punto
def plot(ix, iy):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    circulo8vias(50, 50, 30)
    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
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

# Programa Principal
#if __name__ == "__main__":
    #main()
dir = -12333
if dir:
    print("si")