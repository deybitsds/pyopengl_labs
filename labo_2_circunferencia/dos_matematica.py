# Importamos las librerias a usar ------------------------------------
import random
import math
from collections import Counter
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# MODULOS MATETICA ------------------------------------


# Modulo para calcular parametros aleatorios de una circunferencia
def generar_una_circunferencia_aleatoria(xi, xf, yi, yf):
    minimo = xf / 100
    r = random.randint(int(minimo), int(xf/4))
    h = random.randint(int(xi + r + minimo), int(xf - r - minimo))
    k = random.randint(int(xi + r + minimo), int(xf - r - minimo))
    return [h, k, r]

def generar_circunferencias_aleatorias(numero):
    lista_circunferencias = []
    for k in range(0, numero):
        circunferencia_aleatoria = generar_una_circunferencia_aleatoria(xi, xf, yi, yf)
        lista_circunferencias.append(circunferencia_aleatoria)
    return lista_circunferencias

def generar_puntos_interseccion_dos_circunferencias(parametros_circunferencia_A, parametros_circunferencia_B):
    return 1

def generar_intersecciones_de_golpe(lista_de_listas):
    # Iterar a través de la lista
    contador = Counter(tuple(sublista) for sublista in lista_de_listas)
    # Recuperamos las sublistas que tienen un contador mayor que 1 (es decir, son duplicadas)
    duplicados = [list(sublista) for sublista, count in contador.items() if count > 1]
    return duplicados

def generar_puntos_interseccion_n_circunferencias(lista_circunferencias):
    lista_intersecciones = []
    for circunferencia_1 in lista_circunferencias:
        for circunferencia_2 in lista_circunferencias:
            coordenadas_interseccion = generar_interseccion_dos_circunferencias(circunferencia_1, circunferencia_2)
            if ((coordenadas_interseccion != None) and (coordenadas_interseccion not in lista_intersecciones)):
                lista_intersecciones.append(coordenadas_interseccion)

# Modulos para mostrar graficos ------------------------------------
# --- Función para dibujar un punto
def plot(ix, iy, tamaño = 2):
    glPointSize(tamaño)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    lista_puntos_graficados.append([ix, iy])
    glEnd()

# Modulo para graficar las intersecciones de cincunferencias
def graficar_intersecciones_n_circunferencias(lista_coordenadas_circunferencias):
    lista_intersecciones = generar_puntos_interseccion_n_circunferencias(lista_coordenadas_circunferencias)
    tamaño_punto = 10 # Establecemos el tamaño del punto
    for elem in lista_intersecciones:
        x = elem[0]
        y = elem[1]
        plot(x, y, tamaño_punto)

def graficar_intersecciones_2(lista_graficados):
    lista_intersecciones = generar_intersecciones_de_golpe(lista_graficados)
    tamaño_punto = 15 # Establecemos el tamaño del punto
    if lista_intersecciones != []:
        for elem in lista_intersecciones:
            color_aleatorio()
            x = elem[0]
            y = elem[1]
            plot(x, y, tamaño_punto)

# --- Funcion para dibujar circunferencias
# Algoritmo de 8 vias
def circulo8vias(x0, y0, r):
    glColor3f(0.0, 1.0, 0.0)
    plot(x0, y0 + r)
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)
    x = 1
    y = math.floor(math.sqrt(r * r - x * x) + 0.5)
    while x < y:
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)

        x = x + 1
        y = math.floor(math.sqrt(r * r - x * x) + 0.5)

        if x == y:
            plot(x0 + x, y0 + y)
            plot(x0 + x, y0 - y)
            plot(x0 - x, y0 + y)
            plot(x0 - x, y0 - y)

# Modulo para graficar circunferencias
def graficar_circunferencias(lista_circunferencias):
    for elem in lista_circunferencias:
        h = elem[0]
        k = elem[1]
        r = elem[2]
        circulo8vias(h, k, r)

# -- Funcion para cambiar el color del grafico
# Modulo para establecer el color a graficar en aleatorio
def color_aleatorio():
    # Establecemos una suma para verificar que no sea ni negro ni blanco
    # RGB(1,1,1) BLANCO
    # RGB(0,0,0) NEGRO
    suma = 0
    while (suma == 3 or suma == 0): # Mientras que el color sea negro o blanco
        # Ponemos el color a graficar en aleatorio
        a = random.randint(0,10)/10
        b = random.randint(0,10)/10
        c = random.randint(0,10)/10
        suma = a + b + c
    # Establecemos el color aleatorio
    glColor3f(a, b, c)

# -- Funciones para graficar
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # GRAFICAR CIRCUNFERENCIA 
    graficar_circunferencias(listado_circunferencias_aleatorias)
    # GRAFICAR INTERSECCIONES
    graficar_intersecciones_2(lista_puntos_graficados)

    glFlush()

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xi, xf, yi, xf)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Algoritmo de 8 vias")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()


# Programa Principal
if __name__ == "__main__":
    xi = 0
    xf = 999
    yi = 0
    yf = 999
    listado_circunferencias_aleatorias = generar_circunferencias_aleatorias(5)
    lista_puntos_graficados = []
    main()