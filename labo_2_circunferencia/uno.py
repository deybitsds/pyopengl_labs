# Importamos las librerias a usar ------------------------------------
import random
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# MODULOS MATETICA ------------------------------------

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

# Modulo para calcular un radio a partir de su angulo
def calcular_un_radio(h, k, r, angulo):
    seno = calcular_seno_angulo(angulo) # Calculamos el seno del angulo
    coseno = calcular_coseno_angulo(angulo) # Calculamos el coseno del angulo
    # Calculamos las variaciones en los ejes
    dx = r * coseno
    dy = r * seno
    # Calculamos el nuevo punto con las variaciones
    x = h + dx 
    y = k + dy 
    # Devolvemos los parametros del radio
    return [x, y, h, k]

# Modulo para calcular radios
def calcular_radios(h, k, r, lista_angulos):
    # Inicializamos la lista donde se almacenaran los radios
    lista_radios = []
    # Iteramos para cada elemento de la lista de angulos
    for angulo in lista_angulos:
        # Calculamos el radio del angulo en turno
        radio_nuevo = calcular_un_radio(h, k, r, angulo)
        # Agregamos el radio a la lista de radios
        lista_radios.append(radio_nuevo)
    # Devolvemos la lista de radios
    return lista_radios

# Modulo para calcular parametros aleatorios de una circunferencia
def generar_una_circunferencia_aleatoria(xi, xf, yi, yf):
    # Establecemos un numero minimo
    minimo = xf / 100
    # Generamos la circunferencia aleatoria tomando como punto minimo -> "minimo"
    r = random.randint(int(minimo), int(xf/4))
    h = random.randint(int(xi + r + minimo), int(xf - r - minimo))
    k = random.randint(int(xi + r + minimo), int(xf - r - minimo))
    return [h, k, r]

# Modulos para mostrar graficos ------------------------------------
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
    x0 = lista_parametros[0]
    y0 = lista_parametros[1]
    x1 = lista_parametros[2]
    y1 = lista_parametros[3]
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(x0, y0, x1, y1)

# Modulo para graficar las cuerdas
def graficar_cuerdas(h, k, r, lista_angulos):
    # Calculamos los puntos de la circunferencia
    lista_puntos_circunferencia = calcular_radios(h, k, r, lista_angulos) 
    # Calculamos la longitud de la lista
    longitud = len(lista_puntos_circunferencia) 
    glColor3f(1.0, 1.0, 1.0) # Establecemos el color a blanco
    # Recorremos la lista
    for i in range(0, longitud - 1):
        # Recuperamos el punto inicial -> PI
        x0 = int(lista_puntos_circunferencia[i][0] + 0.49)
        y0 = int(lista_puntos_circunferencia[i][1] + 0.49)
        # Recuperamos el punto final -> PF
        x1 = int(lista_puntos_circunferencia[i + 1][0] + 0.49)
        y1 = int(lista_puntos_circunferencia[i + 1][1] + 0.49)
        # Graficamos la recta que pasa por PI y PF
        graficar_una_recta_DDA([x0, y0, x1, y1])

# Modulo para graficar los radios
def graficar_radios(h, k, r, lista_angulos):
    # Recuperamos los radios solicitados en una lista 
    lista_radios = calcular_radios(h, k, r, lista_angulos) 
    # Iteramos para cada elemento de la lista de radios
    for elem in lista_radios: 
        color_aleatorio() # Establecemos un color aleatorio
        # Recuperamos el punto inicial -> PI
        x0 = int(elem[0] + 0.49) 
        y0 = int(elem[1] + 0.49)
        # Recuperamos el punto inicial -> PF
        x1 = elem[2]
        y1 = elem[3]
        # Graficamos la recta que pasa por PI y PF
        graficar_una_recta_DDA([x0, y0, x1, y1])

# --- Funcion para dibujar circunferencias
# Algoritmo de 8 vias
def circulo8vias(x0, y0, r):
    glColor3f(0.0, 1.0, 0.0)
    color_aleatorio()
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

# -- Funciones adicionales
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

# Modulo par establecer el tamaño del plano cartesiano
def definir_tamaño_plano(xi, xf, yi, yf):
    return xi, xf, yi, yf

# -- Funciones para graficar
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # GENERAR CIRCUNFERENCIA ALEATORIA
    [h, k, r] = generar_una_circunferencia_aleatoria(xi, xf, yi, xf)
    # GENERAR RADIOS DEPENDIENDO DE SU GRADO Y GRAFICAR RADIOS GENERADOS
    grados = [e for e in range(0,361, 30)]
    graficar_radios(h, k, r, grados)
    # GRAFICAR CIRCUNFERENCIA
    circulo8vias(h, k, r)
    # GENERAR Y GRAFICAR CUERDAS 
    graficar_cuerdas(h, k, r, grados)
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
    glutCreateWindow(b"Circunferencia con cuerdas")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()


# Programa Principal
if __name__ == "__main__":
    xi, xf, yi, yf = definir_tamaño_plano(0, 999, 0, 999)
    main()

