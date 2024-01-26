import numpy as np
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- Función para dibujar un punto
def plot(ix, iy):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

# --- Funcion para dibujar rectas
# Algoritmo DDA
def DDA_mejorado(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    if dx >= dy:
        steps = dx
    else:
        steps = dy

    x_increment = (x1 - x0) / steps
    y_increment = (y1 - y0) / steps

    x = x0
    y = y0

    for _ in range(int(steps) + 1):
        plot(int(x), int(y))
        x += x_increment
        y += y_increment

# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0,x1,y1] = lista_parametros
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(int(x0), int(y0), int(x1), int(y1))

def graficar_una_recta_general(lista_parametros_ecuacion):
    global xmin, ymin, xmax, ymax
    [A, B, C] = lista_parametros_ecuacion
    inc_x = int(xmax/5 + xmin)
    inc_y = int(ymax/5 + ymin)

    # Para P1
    y1 = ymin
    x1 = (-1*C)/A #+ inc_x
    
    # Para P2
    x2 = xmax
    y2 = (-A * x2 - C) / B
    x2 = x2 #+ inc_x
    lista = [x1, y1, x2, y2]
    print(lista)
    graficar_una_recta_DDA(lista)

def calcular_reflejo_punto_recta_general(lista_parametros_punto, lista_parametros_recta):
    [x, y] = lista_parametros_punto
    [A, B, C] = lista_parametros_recta
    denominador = A**2 + B**2
    x_reflejado = x - (2 * (A*x + B*y + C) / denominador) * A
    y_reflejado = y - (2 * (A*x + B*y + C) / denominador) * B
    return  [x_reflejado, y_reflejado]

def calcular_reflejo_poligono_recta_general(lista_de_listas_de_puntos, lista_parametros_recta):
    lista_de_listas_de_puntos_reflejados = []
    for elem in lista_de_listas_de_puntos:
        lista_puntos_reflejados = calcular_reflejo_punto_recta_general(elem, lista_parametros_recta)
        lista_de_listas_de_puntos_reflejados.append(lista_puntos_reflejados)
    return lista_de_listas_de_puntos_reflejados

def agrupar_lista_de_listas_de_puntos_de_a_dos_puntos(lista_de_listas_de_puntos):
    sublistas_agrupadas = []
    for i in range(len(lista_de_listas_de_puntos)):
        elem1 = lista_de_listas_de_puntos[i]
        elem2 = lista_de_listas_de_puntos[(i + 1) % len(lista_de_listas_de_puntos)]
        nueva_sublista = elem1 + elem2
        sublistas_agrupadas.append(nueva_sublista)
    return sublistas_agrupadas

def graficar_poligono(lista_de_listas_de_puntos):
    #Graficar poligono
    sublistas_agrupadas = agrupar_lista_de_listas_de_puntos_de_a_dos_puntos(lista_de_listas_de_puntos)
    for elem in sublistas_agrupadas:
        graficar_una_recta_DDA(elem)    

def escalar_poligonos(lista_de_lista_de_puntos):
    global xmin, ymin, xmax, ymax
    inc_x = int(xmax/5 + xmin)
    inc_y = int(ymax/5 + ymin)
    for lista_puntos in lista_de_lista_de_puntos:
        lista_puntos[0] += inc_x
        lista_puntos[1] += inc_y
    
def graficar_ejes_escalados():
    global xmin, ymin, xmax, ymax
    inc_x = int(xmax/5 + xmin)
    inc_y = int(ymax/5 + ymin)
    lista = [[inc_x, 0, inc_x, ymax], [0, inc_y, xmax, inc_y]]
    for recta in lista:
        graficar_una_recta_DDA(recta)

def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

def generar_poligono_aleatorio(cantidad_vertices):
    global xmin, ymin, xmax, ymax
    xmax2 = int(xmax - xmax/10)
    ymax2 = int(ymax / 2)
    lista_de_listas_de_puntos_poligono = []
    for i in range (0,cantidad_vertices):
        x = generar_nro_aleatorio(xmin, xmax2)
        y = generar_nro_aleatorio(ymin, ymax2)
        lista_de_listas_de_puntos_poligono.append([x,y])
    return lista_de_listas_de_puntos_poligono

def graficar_reflejo_de_poligono_en_recta_general(lista_puntos_triangulo, lista_parametros_recta):
    # Graficar ejes x e y
    graficar_ejes_escalados()
    lista_puntos_reflejados_en_x = calcular_reflejo_poligono_recta_general(lista_puntos_triangulo, lista_parametros_recta)
    escalar_poligonos(lista_puntos_triangulo)
    
    glColor3f(1.0, 1.0, 1.0)
    graficar_una_recta_general(lista_parametros_recta)

    glColor3f(0.0, 1.0, 0.0)
    graficar_poligono(lista_puntos_triangulo)
    escalar_poligonos(lista_puntos_reflejados_en_x)
    graficar_poligono(lista_puntos_reflejados_en_x)

def display():
    lista_puntos_triangulo = generar_poligono_aleatorio(5)
    lista_puntos_recta = [10, -10, -30]
    glClear(GL_COLOR_BUFFER_BIT)
    graficar_reflejo_de_poligono_en_recta_general(lista_puntos_triangulo, lista_puntos_recta)
    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Reflexion con respecto al eje x")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    [xmin, ymin, xmax, ymax] = 0.0, 0.0, 499.0, 499.0
    main()
    print