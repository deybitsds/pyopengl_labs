# Importamos las librerias a usar
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Modulo para realizar las composicion de transformaciones
def composicion_triangulo():
    # Triángulo antes de escalar
    glColor3f(0.5, 1.0, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    # Triángulo después de escalar
    glScalef(2.0, 2.0, 0.0)
    # Triángulo después de rotar
    glRotatef(30, 0, 0, 1)
    # Triángulo después de trasladar
    glTranslatef(80.0, 20.0, 0.0)

    glColor3f(1.0, 0.0, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    composicion_triangulo()
    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 599.0, 0.0, 599.0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Transformaciones con OpenGL")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()