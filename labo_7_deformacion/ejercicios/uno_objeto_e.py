from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import random

# --- Modulos para el grafico de rectas
# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0, x1, y1] = lista_parametros
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
    lista_de_listas_puntos_deformados = []
    for lista_parametros_punto in lista_de_listas_parametros_puntos:
        lista_punto_deformado = calcular_deformacion_punto(lista_parametros_punto, lista_factores)
        lista_de_listas_puntos_deformados.append(lista_punto_deformado)
    return lista_de_listas_puntos_deformados

def calcular_todos_los_puntos_de_un_rectangulo(lista_puntos_extremos):
    [x0, y0, x1, y1] = lista_puntos_extremos
    lista_listas_puntos_rectangulo = []
    lista_listas_puntos_rectangulo.append([x0, y0])
    lista_listas_puntos_rectangulo.append([x0, y1])
    lista_listas_puntos_rectangulo.append([x1, y1])
    lista_listas_puntos_rectangulo.append([x1, y0])
    return lista_listas_puntos_rectangulo

def agrupar_lista_de_listas_de_puntos_de_a_dos_puntos(lista_de_listas_de_puntos):
    sublistas_agrupadas = []
    for i in range(len(lista_de_listas_de_puntos)):
        elem1 = lista_de_listas_de_puntos[i]
        elem2 = lista_de_listas_de_puntos[(i + 1) % len(lista_de_listas_de_puntos)]
        nueva_sublista = elem1 + elem2
        sublistas_agrupadas.append(nueva_sublista)
    return sublistas_agrupadas 

# --- MODULOS PARA EL OBJETO E
def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

def generar_parametros_iniciales_objeto_e_aleatorio():
    # Establecemos el tamaño de la pantalla
    global xmin, xmax, ymin, ymax
    xmin = int(xmax/2)
    ymin = int(ymax/20)
    # Generamos numeros aleatorios que quepan en la mitad de la pantalla
    k = generar_nro_aleatorio(1,30)
    x0 = generar_nro_aleatorio(xmin,xmax)
    y0 = generar_nro_aleatorio(ymin,ymax)
    # Devolvemos los parametros inicilaes aleatorios
    return [x0, y0, k]

def generar_puntos_objeto_e(lista_parametros_iniciales):
    # Recuperar paramatros iniciales
    [x, y, k] = lista_parametros_iniciales
    lista_de_lista_de_rectas = []
    # Generar puntos
    lista_de_lista_de_rectas.append([x, y])
    lista_de_lista_de_rectas.append([x + 4 * k, y])
    lista_de_lista_de_rectas.append([x + 4 * k, y  + k])
    lista_de_lista_de_rectas.append([x + k, y + k])
    lista_de_lista_de_rectas.append([x + k, y + 2 * k])
    lista_de_lista_de_rectas.append([x + 2 * k, y + 2 * k])
    lista_de_lista_de_rectas.append([x + 2 * k, y + 3 * k])
    lista_de_lista_de_rectas.append([x + k, y + 3 * k])
    lista_de_lista_de_rectas.append([x + k, y + 4 * k])
    lista_de_lista_de_rectas.append([x + 4 * k, y + 4 * k])
    lista_de_lista_de_rectas.append([x + 4 * k, y + 5 * k])
    lista_de_lista_de_rectas.append([x, y + 5 * k])
    # Devolver lista con las rectas
    return lista_de_lista_de_rectas

# Modulo para graficar y calcular la deformacion de un poligono
def deformar_objeto_e():
    
    # Calcular parametros iniciales
    parametros = generar_parametros_iniciales_objeto_e_aleatorio()
    parametros = [5, 5, 20]
    #  Calcular puntos objeto E
    lista_parametros_objeto_e = generar_puntos_objeto_e(parametros)
    # Graficar objeto E
    graficar_un_poligono(lista_parametros_objeto_e)
    # Calcular deformacion en y = 3
    lista_parametros_deformados = calcular_deformacion_poligono(lista_parametros_objeto_e, [0,3])
    # Calcular deformacion en x = 2
    lista_parametros_deformados = calcular_deformacion_poligono(lista_parametros_deformados, [2,0])
    # Graficar objeto E deformado
    graficar_un_poligono(lista_parametros_deformados)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    deformar_objeto_e()
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
    glutInitWindowSize(850, 400)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Deformacion con x = 2, y = 3")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    [xmin, ymin, xmax, ymax] = 0.0, 0.0, 850.0, 400.0
    main()
