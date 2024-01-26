#Codigo Punto.py
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

def Inicio():
  glClearColor(0,0,0,0)
  gluOrtho2D(0,35,0,35)

def DibujaPunto():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(1,1,0)
     glPointSize(30)
     glBegin(GL_POINTS)
     glVertex2i(17,17)
     glEnd()
     glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Puntos")
    # desde aca
    glutDisplayFunc(DibujaPunto)
    Inicio()
    glutMainLoop()
if __name__ == '__main__':
    main()