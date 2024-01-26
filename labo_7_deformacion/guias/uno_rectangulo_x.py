from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# --- Modulos para el grafico de rectas
# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0,x1,y1] = lista_parametros
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(int(x0), int(y0), int(x1), int(y1))

def graficar_un_poligono(lista_de_lista_de_rectas):
    # Para cada recta A de la lista de listas graficar la recta A
    lista_de_lista_de_rectas = agrupar_lista_de_listas_de_puntos_de_a_dos_puntos(lista_de_lista_de_rectas)
    for e in lista_de_lista_de_rectas:
        # Graficamos la recta mediante el algoritmo DDA
        graficar_una_recta_DDA(e)

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

# --- Modulos para el calculo de puntos
def calcular_deformacion_punto(lista_parametros_punto, lista_factores):
    [x, y] = lista_parametros_punto
    [sh_x, sh_y] = lista_factores
    sh = np.array([[1, sh_x], [sh_y, 1]])
    p1 = np.array([[x],[y]])
    lista_parametros_p2 = np.dot(sh, p1)
    return [lista_parametros_p2[0][0], lista_parametros_p2[1][0]]

def calcular_deformacion_poligono(lista_de_listas_parametros_puntos, lista_factores):
    # lista_de_listas = [[1,2],[3,4],[8,3]]
    lista_nueva = []
    for elem in lista_de_listas_parametros_puntos:
        lista_nueva1 = calcular_deformacion_punto(elem, lista_factores)
        lista_nueva.append(lista_nueva1)
    return lista_nueva

def calcular_todos_los_puntos_de_un_rectangulo(lista_puntos_extremos):
    [x0, y0, x1, y1] = lista_puntos_extremos
    lista_nueva = []
    lista_nueva.append([x0, y0])
    lista_nueva.append([x0, y1])
    lista_nueva.append([x1, y1])
    lista_nueva.append([x1, y0])
    return lista_nueva

def agrupar_lista_de_listas_de_puntos_de_a_dos_puntos(lista_de_listas_de_puntos):
    sublistas_agrupadas = []
    for i in range(len(lista_de_listas_de_puntos)):
        elem1 = lista_de_listas_de_puntos[i]
        elem2 = lista_de_listas_de_puntos[(i + 1) % len(lista_de_listas_de_puntos)]
        nueva_sublista = elem1 + elem2
        sublistas_agrupadas.append(nueva_sublista)
    return sublistas_agrupadas 


# Modulo para graficar y calcular la deformacion de un poligono
def deformar_rectangulo_eje_x():
    # Inicializar los puntos extremos del rectangulo
    lista_rectangulo_puntos_extremos = [5.0, 5.0, 160.0, 160.0]
    # Calcular puntos rectangulo
    lista_listas_parametros_rectangulo = calcular_todos_los_puntos_de_un_rectangulo(lista_rectangulo_puntos_extremos)
    # Mostrar inicial
    graficar_un_poligono(lista_listas_parametros_rectangulo)
    # Deformar
    lista_listas_parametros_rectangulo_deformado = calcular_deformacion_poligono(lista_listas_parametros_rectangulo, [2, 0])
    # Mostrar final
    graficar_un_poligono(lista_listas_parametros_rectangulo_deformado)

def display():

    glClear(GL_COLOR_BUFFER_BIT)
    deformar_rectangulo_eje_x()
    glFlush()


def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Deformacion con respecto al eje x")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    [xmin, ymin, xmax, ymax] = 0.0, 0.0, 499.0, 499.0
    main()