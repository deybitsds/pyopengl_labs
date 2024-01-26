# Importamos las librerias a usar
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicializamos el angulo con 0°
angle = 0.0

# --- Modulos para graficar el objeto E
# Modulo para graficar un rectangulo con funciones de OpenGL
def dibujar_rectangulo(x, y, ancho, altura):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + ancho, y)
    glVertex2f(x + ancho, y + altura)
    glVertex2f(x, y + altura)
    glEnd()

# Modulo para graficar un rectangulo configurando otro parametros
def graficar_rectangulo(x, y, ancho, altura):
    # Guardar la matriz de transformación actual y aplicar rotación
    glPushMatrix()
    glRotatef(angle, 0.0, 0.0, 1.0)
    dibujar_rectangulo(x, y, ancho, altura)
    # Restaurar la matriz de transformación
    glPopMatrix()   

# Modulo para graficar objeto E
def graficar_objeto_e(x, y, grosor, ROJO, VERDE, AZUL):
    # Establecer el color del gráfico
    glColor3f(ROJO, VERDE, AZUL)
    # Primer rectángulo
    graficar_rectangulo(x + grosor, y, 3 * grosor, grosor)
    # Segundo rectángulo
    graficar_rectangulo(x, y, grosor, 5 * grosor)
    # Tercer rectángulo
    graficar_rectangulo(x + grosor, y + 2 * grosor, grosor, grosor)
    # Cuarto rectángulo
    graficar_rectangulo(x + grosor, y + 4 * grosor, 3 * grosor, grosor)

# -- Modulos para inicializar OpenGL
def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Modulo para la ejecucion de tareas en segundo plano
def idle():
    glutPostRedisplay()

# Modulo de graficos principal
def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # OBJETO E 1
    glTranslatef(-0.3, 0.2, 0.0)  # Trasladar
    graficar_objeto_e(-0.2, -0.2, 0.13, 0.5, 1.0, 0.7)

    # OBJETO E 2
    glTranslatef(0.5, -0.7, 0.0)  # Trasladar
    graficar_objeto_e(-0.2, -0.2, 0.13, 1.0, 0.0, 7.0)

    glutSwapBuffers()
    angle += 0.2

# Programa principal
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