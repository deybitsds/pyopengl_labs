# LIBRERIAS A USAR

import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

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

# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0,x1,y1] = lista_parametros
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(int(x0), int(y0), int(x1), int(y1))
        
# --- MODULOS GENERALES
#
def swap(x, y):
    return y, x

# 
def agregar_lista_a_lista(lista_unidad,lista_conjunto):
    lista_conjunto.append(lista_unidad)

# MODULOS PARA LEER DATOS
#
def leer_rectas():
    numero_rectas = int(input("Ingrese Nro. Rectas: "))
    lista_rectas_a_devolver = []
    print("======================")
    for k in range(0,numero_rectas):
        print("RECTA " + str(k + 1))
        print("=======")
        una_recta = leer_una_recta()
        lista_rectas_a_devolver.append(una_recta)
        print()
    return lista_rectas_a_devolver

#
def leer_una_recta():
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    return [x0,y0,x1,y1]

#
def leer_coordenadas_rectangulo():
    print("COORDENADAS DEL RECTÁNGULO")
    print("==========================")
    x0 = int(input("xmin: "))
    y0 = int(input("ymin: "))
    x1 = int(input("xmax: "))
    y1 = int(input("ymax: "))
    return [x0,y0,x1,y1]

# --- MODULOS PARA GRAFICAR RECTAS
#
def graficar_rectas_iniciales(lista_rectas):
    for elem in lista_rectas:
        graficar_una_recta_DDA(elem)

#
def graficar_rectas_cortadas():
    global lista_rectas, lista_coordenadas_rectangulo
    lista_final = parametrica(lista_rectas, lista_coordenadas_rectangulo)
    for elem in lista_final:
        graficar_una_recta_DDA(elem)

#
def graficar_rectangulo():
    global lista_coordenadas_rectangulo
    [xmin, ymin, xmax, ymax] = lista_coordenadas_rectangulo
    graficar_una_recta_DDA([xmin, ymin, xmin, ymax])
    graficar_una_recta_DDA([xmin, ymax, xmax, ymax])
    graficar_una_recta_DDA([xmax, ymax, xmax, ymin])
    graficar_una_recta_DDA([xmax, ymin, xmin, ymin])

# --- MODULOS PARA CALCULAR PUNTOS
#
# Función para realizar el recorte paramétrico en una lista de rectas
def parametrica(lista_rectas, lista_coordenadas_rectangulo):
    # Inicializar lista para almacenar las rectas cortadas
    lista_rectas_cortadas = []

    # Iterar sobre cada recta en la lista
    for elem in lista_rectas:
        # Llamar a la función parametrica1 para procesar cada recta
        parametrica1(elem, lista_rectas_cortadas, lista_coordenadas_rectangulo)

    # Devolver la lista de rectas después del recorte
    return lista_rectas_cortadas


#
# Función para aplicar el recorte paramétrico a una recta específica
def parametrica1(recta, lista_rectas_cortadas, lista_coordenadas_rectangulo):
    # Desempaquetar las coordenadas de la recta y del rectángulo de recorte
    [x0, y0, x1, y1] = recta
    [xmin, ymin, xmax, ymax] = lista_coordenadas_rectangulo
    
    # Verificar si los puntos iniciales y finales de la recta están dentro del rectángulo de recorte
    primera_sentencia = xmin <= x0 <= xmax and ymin <= y0 <= ymax
    segunda_sentencia = xmin <= x1 <= xmax and ymin <= y1 <= ymax

    # CASO 1: Ambos puntos de la recta están dentro del rectángulo
    if primera_sentencia and segunda_sentencia:
        lista_rectas_cortadas.append(recta)
    else:
        # CASO 2: Uno de los puntos está dentro del rectángulo
        if primera_sentencia or segunda_sentencia:
            tline = calcular_tline1(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            if 0 <= tline <= 1:
                agregar_x_i_y_a_lista(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline1, lista_rectas_cortadas, primera_sentencia)
            else:
                tline = calcular_tline2(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
                if 0 <= tline <= 1:
                    agregar_x_i_y_a_lista(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline2, lista_rectas_cortadas, primera_sentencia)
                else:
                    tline = calcular_tline3(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
                    if 0 <= tline <= 1:
                        agregar_x_i_y_a_lista(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline3, lista_rectas_cortadas, primera_sentencia)
                    else:
                        tline = calcular_tline3(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
                        agregar_x_i_y_a_lista(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline4, lista_rectas_cortadas, primera_sentencia)
        else:
            # CASO 3: Ambos puntos están fuera del rectángulo; encontrar intersecciones
            puntos_interseccion = []
            # uno
            tline = calcular_tline1(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            calcular_x_i_y_partes(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline1, tline, puntos_interseccion)

            # dos
            tline = calcular_tline2(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            calcular_x_i_y_partes(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline2, tline, puntos_interseccion)
            if len(puntos_interseccion) == 4:
                agregar_lista_a_lista(puntos_interseccion, lista_rectas_cortadas)
                return
            # tres
            tline = calcular_tline3(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            calcular_x_i_y_partes(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline3, tline, puntos_interseccion)
            if len(puntos_interseccion) == 4:
                agregar_lista_a_lista(puntos_interseccion, lista_rectas_cortadas)
                return
            # cuatro
            tline = calcular_tline4(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            calcular_x_i_y_partes(x0, y0, x1, y1, xmin, ymin, xmax, ymax, calcular_tline4, tline, puntos_interseccion)
            if len(puntos_interseccion) == 4:
                agregar_lista_a_lista(puntos_interseccion, lista_rectas_cortadas)
                return

# --- MODULOS PARA TODOS LOS CASOS
#
# Función para calcular el parámetro tline en el caso 1
def calcular_tline1(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    num = ymin - y0
    den = y1 - y0
    return num / den
#
# Función para calcular el parámetro tline en el caso 2
def calcular_tline2(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    num = ymax - y0
    den = y1 - y0
    return num / den
#
# Función para calcular el parámetro tline en el caso 3
def calcular_tline3(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    num = xmin - x0
    den = x1 - x0
    return num / den
#
# Función para calcular el parámetro tline en el caso 4
def calcular_tline4(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    num = xmax - x0
    den = x1 - x0
    return num / den

# Función para calcular la coordenada x utilizando el parámetro tline y la función específica
def calcular_x(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion1):
    tline = funcion1(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
    x = x0 + tline * (x1 - x0)
    return x
#
# MODULOS PARA CALCULAR Y EN FUNCION A LA TLINE
def calcular_y(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion1):
    # Calcula el parámetro tline utilizando la función proporcionada
    tline = funcion1(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
    # Calcula la coordenada y utilizando el parámetro tline
    y = y0 + tline * (y1 - y0)
    return y

# --- MODULOS PARA CASO DOS
def agregar_x_i_y_a_lista(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion2, lista_rectas_cortadas, primera_sentencia):
    # Calcula las coordenadas x e y utilizando la función proporcionada
    x = calcular_x(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion2)
    y = calcular_y(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion2)
    # Verifica la secuencia correcta y agrega la recta final a la lista
    recta_final = secuencia_correcta(x0, y0, x1, y1, x, y, primera_sentencia) 
    lista_rectas_cortadas.append(recta_final)

# MODULO PARA VERIFICAR LA SECUENCIA DE UNA RECTA
def secuencia_correcta(x0, y0, x1, y1, x, y, primera_sentencia):
    if primera_sentencia:
        # Secuencia correcta: x0, y0, x, y
        return [x0, y0, x, y]
    else:
        # Secuencia correcta: x, y, x1, y1
        return [x, y, x1, y1]

# --- MODULOS PARA CASO TRES
def calcular_x_i_y_partes(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion3, tline, puntos_interseccion):
    if 0 <= tline <= 1:
        # Calcula las coordenadas x e y utilizando la función proporcionada
        x = calcular_x(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion3)
        y = calcular_y(x0, y0, x1, y1, xmin, ymin, xmax, ymax, funcion3)
        # Agrega las coordenadas de intersección a la lista
        puntos_interseccion.append(x)
        puntos_interseccion.append(y)


# --- MODULOS PARA GRAFICAR UTILIZANDO OPENGL
#
def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("LINEAS ANTES DEL RECORTE")
    glutDisplayFunc(display1)
    myinit()

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(550, 0)
    glutCreateWindow("LINEAS DESPUES DEL RECORTE")
    glutDisplayFunc(display2)
    myinit()

    glutMainLoop()

# displays
def display1():
    glClear(GL_COLOR_BUFFER_BIT)
    global lista_rectas
    graficar_rectas_iniciales(lista_rectas)
    graficar_rectangulo()
    glFlush()

def display2():
    glClear(GL_COLOR_BUFFER_BIT)
    graficar_rectas_cortadas()
    graficar_rectangulo()
    glFlush()

#
def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)
    
# --- PROGRAMA PRINCIPAL
lista_rectas = leer_rectas()
lista_coordenadas_rectangulo = leer_coordenadas_rectangulo()
if __name__ == "__main__":
    main()