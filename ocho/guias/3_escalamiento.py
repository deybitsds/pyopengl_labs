from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Escala():
    # Triángulo antes de escalar
    glColor3f(0.5, 1.0, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    # Triángulo después de escalar
    glScalef(2.0, 2.0, 0.0)
    glColor3f(1.0, 0.0, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    Escala()
    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Transformaciones con OpenGL")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()
