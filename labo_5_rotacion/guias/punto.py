from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random


# Modulos para calcular funciones trigonometricas con grados sexagesimales
def calcular_seno_angulo(angulo):
    # Transformamos el angulo en sexagesimal a radianes
    angulo_radianes = math.radians(angulo) 
    # Calculamos el seno 
    seno = math.sin(angulo_radianes)
    return seno

def calcular_coseno_angulo(angulo):
    # Transformamos el angulo en sexagesimal a radianes
    angulo_radianes = math.radians(angulo)
    # Calculamos el seno 
    coseno = math.cos(angulo_radianes)
    return coseno 

# Modulos para mostrar graficos 
# --- Función para dibujar un punto
def plot(ix, iy):

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

# --- Funcion para dibujar rectas


def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

def generar_pto_aleatorio(min, max):
    x = generar_nro_aleatorio(min, max)
    y = generar_nro_aleatorio(min, max)
    return [x, y]

def calcular_rotacion_punto(lista_coordenadas_punto, angulo):
    [x, y] = lista_coordenadas_punto
    seno = calcular_seno_angulo(angulo)
    coseno = calcular_coseno_angulo(angulo)
    x1 = x * coseno - y * seno
    y1 = y * coseno + x * seno
    return [x1, y1]

def graficar_punto(lista_coordenadas):
    [x, y] = lista_coordenadas
    plot(int(x) ,int(y))

# Funcion para
def rotacion_de_un_punto():
    p = generar_pto_aleatorio(50, 60)
    glColor3f(0.0, 1.0, 0.0)
    graficar_punto(p)
    grado = generar_nro_aleatorio(1, 90)
    pN = calcular_rotacion_punto(p,grado)
    glColor3f(1.0, 0.0, 0.0)
    graficar_punto(pN)

# Despliega el gráfico
def display():

    glClear(GL_COLOR_BUFFER_BIT)  # Establece el color de la ventana
    rotacion_de_un_punto()  # Traslada objeto E
    glFlush()  # Fuerza la ejecución de los comandos de OpenGL

# Inicializa OpenGL
def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)  # Activa la matriz de transformación
    glLoadIdentity()  # Carga la identidad para poder hacer transformaciones
    gluOrtho2D(0.0, 100.0, 0.0, 100.0)  # Establece una ventana de dibujo 2D

# Función principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  # Ventana 500x500 píxeles
    glutInitWindowPosition(0, 0)  # Coloca la ventana de despliegue en esq. sup. izq
    glutCreateWindow("Rotacion de un punto")  # Título de la ventana
    glutDisplayFunc(display)  # Llama a la función display cuando se abre la ventana
    myinit()  # Fija o establece los atributos
    glutMainLoop()  # Entra a un ciclo de evento

if __name__ == "__main__":
    main()