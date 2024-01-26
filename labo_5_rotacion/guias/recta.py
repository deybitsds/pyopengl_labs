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

    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

# --- Funcion para dibujar rectas
# Algoritmo DDA
def DDA_mejorado(x0, y0, x1, y1):
    if (x0 == x1):
        if y1 < y0:
            y1, y0 = y0, y1
        for y in range(y0, y1 + 1):
            plot(x0, y)
    else:
        if x1 < x0:
            x0, y0, x1, y1 = x1, y1, x0, y0
        m = (y1 - y0) / (x1 - x0)
        y = y0
        for x in range(x0, x1 + 1):
            plot(x, int(y))
            y = y + m

# --- Funcion para dibujar rectas
# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0] = lista_parametros[0]
    [x1,y1] = lista_parametros[1]
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(int(x0), int(y0), int(x1), int(y1))


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

def calcular_rotacion_recta(lista_coordenadas_recta, angulo):
    punto_a_inicial = lista_coordenadas_recta[0]
    punto_a_final = lista_coordenadas_recta[1]
    
    punto_b_inicial = calcular_rotacion_punto(punto_a_inicial, angulo)
    punto_b_final = calcular_rotacion_punto(punto_a_final, angulo)

    return [punto_b_inicial, punto_b_final]

# Funcion para
def rotacion_de_un_punto():
    recta_uno = [[50, 40],[120, 70]]
    glColor3f(0.0, 1.0, 0.0)
    graficar_una_recta_DDA(recta_uno)
    recta_dos = calcular_rotacion_recta(recta_uno, 45)
    glColor3f(1.0, 0.0, 0.0)
    graficar_una_recta_DDA(recta_dos)

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
    gluOrtho2D(0.0, 250.0, 0.0, 250.0)  # Establece una ventana de dibujo 2D

# Función principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  # Ventana 500x500 píxeles
    glutInitWindowPosition(0, 0)  # Coloca la ventana de despliegue en esq. sup. izq
    glutCreateWindow("Rotacion de una recta")  # Título de la ventana
    glutDisplayFunc(display)  # Llama a la función display cuando se abre la ventana
    myinit()  # Fija o establece los atributos
    glutMainLoop()  # Entra a un ciclo de evento

if __name__ == "__main__":
    main()