from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0

def dibujar_rectangulo(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def idle():
    glutPostRedisplay()

def graficar_rectangulo(x, y, ancho, altura):
    glPushMatrix()
    glRotatef(angle, 0.0, 0.0, 1.0)
    dibujar_rectangulo(x, y, ancho, altura)
    glPopMatrix()   

def graficar_objeto_e(x, y, grosor, RED, GREEN, BLUE):
    # Establecemos el color del grafico
    glColor3f(RED, GREEN, BLUE)
    # Primer rectángulo
    graficar_rectangulo(x + grosor, y, 3 * grosor, grosor)
    # Segundo rectángulo
    graficar_rectangulo(x, y, grosor, 5 * grosor)
    # Tercer rectángulo
    graficar_rectangulo(x + grosor, y + 2 * grosor, grosor, grosor)
    # Cuarto rectángulo
    graficar_rectangulo(x + grosor, y + 4 * grosor, 3 * grosor, grosor)

def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    

    glTranslatef(-0.3, 0.2, 0.0)  # Translate

    # OBJETO E 1
    graficar_objeto_e(-0.2, -0.2, 0.13, 0.0, 1.0, 0.0)

    # ?
    glTranslatef(0.5, -0.7, 0.0)  # Translate

    # OBJETO E 2
    graficar_objeto_e(-0.2, -0.2, 0.13, 1.0, 0.0, 0.0)

    glutSwapBuffers()
    angle += 0.2

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Grafico Objetos E giratorios")
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    initGL()
    glutMainLoop()

if __name__ == "__main__":
    main()