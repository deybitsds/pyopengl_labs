from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Función que traslada un rectángulo
def trasladaRectangulo(P, T):
    glBegin(GL_LINES)
    # -- IZQUIERDA
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[0][0], P[1][1])
    # -- ARRIBA
    glVertex2f(P[0][0], P[1][1])
    glVertex2f(P[1][0], P[1][1])
    # -- DERECHA
    glVertex2f(P[1][0], P[1][1])
    glVertex2f(P[1][0], P[0][1])
    # -- ABAJO
    glVertex2f(P[1][0], P[0][1])
    glVertex2f(P[0][0], P[0][1])
    glEnd()

    # Calcula las coordenadas de traslación
    P[0][0] = P[0][0] + T[0]
    P[0][1] = P[0][1] + T[1]
    P[1][0] = P[1][0] + T[0]
    P[1][1] = P[1][1] + T[1]

    # Dibuja el rectángulo trasladado
    glBegin(GL_LINES)
    # -- IZQUIERDA
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[0][0], P[1][1])
    # -- ARRIBA
    glVertex2f(P[0][0], P[1][1])
    glVertex2f(P[1][0], P[1][1])
    # -- DERECHA
    glVertex2f(P[1][0], P[1][1])
    glVertex2f(P[1][0], P[0][1])
    # -- ABAJO
    glVertex2f(P[1][0], P[0][1])
    glVertex2f(P[0][0], P[0][1])
    glEnd()

# Despliega el gráfico
def display():
    P = [[50, 80], [220, 180]]  # Coordenadas del rectangulo
    T = [120, 210]  # Vector de traslación

    glClear(GL_COLOR_BUFFER_BIT)  # Establece el color de la ventana
    trasladaRectangulo(P, T)  # Traslada el rectangulo
    glFlush()  # Fuerza la ejecución de los comandos de OpenGL

# Inicializa OpenGL
def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)  # Activa la matriz de transformación
    glLoadIdentity()  # Carga la identidad para poder hacer transformaciones
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)  # Establece una ventana de dibujo 2D

# Función principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  # Ventana 500x500 píxeles
    glutInitWindowPosition(0, 0)  # Coloca la ventana de despliegue en esq. sup. izq
    glutCreateWindow("Traslacion de rectangulo")  # Título de la ventana
    glutDisplayFunc(display)  # Llama a la función display cuando se abre la ventana
    myinit()  # Fija o establece los atributos
    glutMainLoop()  # Entra a un ciclo de evento

if __name__ == "__main__":
    main()
