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

def calcular_reflejo_punto_eje_y(lista_parametros_punto):
    [x1, y1] = lista_parametros_punto
    matriz_ref = np.array([[-1, 0], [0, 1]])
    matriz_p1 = np.array([[x1], [y1]])
    matriz_p2 = np.dot(matriz_ref, matriz_p1)
    [x2, y2] = [matriz_p2[0,0], matriz_p2[1, 0]]
    return [x2, y2]

def calcular_reflejo_poligono_eje_y(lista_de_listas_de_puntos):
    lista_de_listas_de_puntos_reflejados = []
    for elem in lista_de_listas_de_puntos:
        lista_puntos_reflejados = calcular_reflejo_punto_eje_y(elem)
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

def escalar_poligono_con_respecto_a_eje_y(lista_de_lista_de_puntos):
    global xmin, ymin, xmax, ymax
    inc_x = int(xmax/2 + xmin)
    inc_y = int(ymax/10 + ymin)
    for lista_puntos in lista_de_lista_de_puntos:
        lista_puntos[0] += inc_x
        lista_puntos[1] += inc_y
    
def graficar_ejes_escalados():
    global xmin, ymin, xmax, ymax
    inc_x = int(xmax/2 + xmin)
    inc_y = int(ymax/10 + ymin)
    lista = [[0, inc_y, xmax, inc_y], [inc_x, 0, inc_x, ymax]]
    for recta in lista:
        graficar_una_recta_DDA(recta)

def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

def generar_poligono_aleatorio(cantidad_vertices):
    global xmin, ymin, xmax, ymax
    xmax2 = int(xmax/2)
    ymax2 = int(ymax - ymax/10)
    lista_de_listas_de_puntos_poligono = []
    for i in range (0,cantidad_vertices):
        x = generar_nro_aleatorio(xmin, xmax2)
        y = generar_nro_aleatorio(ymin, ymax2)
        lista_de_listas_de_puntos_poligono.append([x,y])
    return lista_de_listas_de_puntos_poligono

def graficar_reflejo_de_triangulo_en_y(lista_puntos_poligono):

    graficar_ejes_escalados()
    lista_puntos_reflejados_en_y = calcular_reflejo_poligono_eje_y(lista_puntos_poligono)
    escalar_poligono_con_respecto_a_eje_y(lista_puntos_poligono)
    graficar_poligono(lista_puntos_poligono)
    escalar_poligono_con_respecto_a_eje_y(lista_puntos_reflejados_en_y)
    graficar_poligono(lista_puntos_reflejados_en_y)

def display():
    #lista_puntos_poligono = [[120.0, 160.0], [100.0, 200.0], [10.0, 100.0]]
    lista_puntos_triangulo = generar_poligono_aleatorio(3)
    glClear(GL_COLOR_BUFFER_BIT)
    graficar_reflejo_de_triangulo_en_y(lista_puntos_triangulo)
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
    glutCreateWindow("Reflexion con respecto al eje y")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    [xmin, ymin, xmax, ymax] = 0.0, 0.0, 499.0, 499.0
    main()