from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def TransfComp():
    # Triángulo antes de la transformación compuesta
    glColor3f(0.5, 1.0, 0.7)
    glColor3f(0.5, 1.0, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    # Rotación de 45 grados
    glRotatef(10, 0, 0, 1)

    # Traslación a la posición (200, 200)
    glTranslatef(200.0, 200.0, 0.0)
    glColor3f(1.0, 0.0, 0.7)
    # Triángulo después de la transformación compuesta
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    TransfComp()

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
