# Importamos las librerias
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

# -- Modulos matematicas
# Modulo para calcular la ecuacion general de una recta
def generar_ecuacion_recta(coordenadasPunto):
    # Con coordenadasPunto = [x0, y0, x1, y1]
    x0 = coordenadasPunto[0] 
    y0 = coordenadasPunto[1]
    x1 = coordenadasPunto[2]
    y1 = coordenadasPunto[3]
    # Retormamos la forma general de la recta Ax + By + C = 0
    A = y1 - y0
    B = x0 - x1
    C = y0 * x1 - x0 * y1
    # Devolvemos los elementos en una lista
    return [A, B, C]
    
# Modulo para calcular los puntos de interseccion de dos rectas
def generar_interseccion_dos_rectas(coordenadasPunto_A, coordenadasPunto_B):
    # Con coordenadasPunto = [x0, y0, x1, y1] 
    ecuacionRecta_A = generar_ecuacion_recta(coordenadasPunto_A) # Calculamos la ecuacion de la recta A
    # Recuperamos los puntos iniciales de la recta A
    x0_A, y0_A, x1_A, y1_A = coordenadasPunto_A[0], coordenadasPunto_A[1], coordenadasPunto_A[2], coordenadasPunto_A[3]
    ecuacionRecta_B = generar_ecuacion_recta(coordenadasPunto_B) # Calculamos la ecuacion de la recta B
    # Recuperamos los puntos iniciales de la recta B
    x0_B, y0_B, x1_B, y1_B = coordenadasPunto_B[0], coordenadasPunto_B[1], coordenadasPunto_B[2], coordenadasPunto_B[3]
    # Recuperamos los parametros de la ecuacino general de la recta
    a, b = ecuacionRecta_A[0], ecuacionRecta_A[1], 
    c = -1 * ecuacionRecta_A[2] # Negativizamos el termino independiente
    d, e = ecuacionRecta_B[0], ecuacionRecta_B[1]
    f = -1 * ecuacionRecta_B[2] # Negativizamos el termino independiente
    # Hallamos la determinante
    determinante = (a * e - d * b)
    # Verificamos la existencia de una solucion con (Det != 0)
    if determinante != 0:
        # Si existe una solucion, calculamos
        x = (e *  c - b * f) / determinante
        y = (a *  f - d * c) / determinante
        # Verificamos que los puntos de interseccion existan y no sean teoricos
        # Para eso verificamos que [x, y] se encuentren dentro de los puntos iniciales
        if (x0_A <= x <= x1_A and x0_B <= x <= x1_A) and ((y0_A <= y <= y1_A or y1_A <= y <= y0_A) and (y0_B <= y <= y1_B or y1_B <= y <= y0_B)):
            # Devolvemos [x, y]
            return [x, y]

# Modulo para calculos los puntos de interseccion ENTEROS de dos rectas
def generar_interseccion_entera_dos_rectas(coordenadasPunto_A, coordenadasPunto_B):
    # Calculamos los puntos de interseccion
    lista_coordenadas_interseccion = generar_interseccion_dos_rectas(coordenadasPunto_A, coordenadasPunto_B)
    # Verificamos que estos puntos existan
    if lista_coordenadas_interseccion != None:
        # Caso existan, redondeamos al inmediato inferior
        x = int(lista_coordenadas_interseccion[0])
        y = int(lista_coordenadas_interseccion[1])
        # Devolvemos los puntos enteros
        return [x, y]

# Modulo para calcular los puntos de interseccion de N rectas
def generar_interseccion_n_rectas(lista_coordenadas_rectas):
    # Inicializamos la lista que contendra los puntos de interseccion
    lista_intersecciones = []
    # Iteramos para cada elemento de lista_coordenads_rectas
    for elem1 in lista_coordenadas_rectas:
        # Volvemos a iterar para cada elemento        
        for elem2 in lista_coordenadas_rectas:
            # Calculamos los puntos de interseccion de elem1 y elem2
            coordenadas_interseccion = generar_interseccion_entera_dos_rectas(elem1,elem2)
            # Verificamos que exista la interseccion && Verificamos que los puntos de interseccion no se repitan
            if ((coordenadas_interseccion != None) and (coordenadas_interseccion not in lista_intersecciones)):
                # Caso cumplan las condiciones agregamos los puntos de interseccion a lista_interseccion
                lista_intersecciones.append(coordenadas_interseccion)
    # Devolvemos la lista de todos los puntos de interseccion
    return lista_intersecciones

# -- Modulos para graficar
# Modulo para graficar los puntos de interseccion de todas las rectas
def graficar_puntos_interseccion(lista_coordenadas_rectas):
    # Recuperamos la lista de puntos de interseccion de las rectas
    lista_intersecciones = generar_interseccion_n_rectas(lista_coordenadas_rectas)
    # Establecemos el tamaño del punto en 10 pixeles
    glPointSize(10)
    # Iteramos para cada elemento en lista_intersecciones
    for e in lista_intersecciones:
        color_aleatorio() # Establecemos un color aleatorio para el color del punto
        x = e[0] # Recuperamos x
        y = e[1] # Recuperamos y
        plot(x,y) # Graficamos el punto

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

# Modulo para generar una recta con parametros aleatorios
def generar_recta_aleatoria():
    # Establecemos el eje y en aleatorio
    y0 = random.randint(0,499)
    y1 = random.randint(0,499)
    resta = 0
    while (resta <= 0): # Verificamos que se grafique de izquierda a derecha
        x0 = random.randint(0,499)
        x1 = random.randint(0,499)
        # Verificamos que resta no sea negativa
        resta = x1 - x0  
    # Devolvemos los parametros de la recta aleatoria  
    return [x0, y0, x1, y1]

# Modulo para generar "num" rectas aleatorias
def generar_rectas_aleatorias(num):
    # Inicializamos la lista donde se almacenaran
    lista_coordenadas_rectas = []
    # Iteramos "num" veces
    for k in range(0,num):
        # Generamos una recta aleatoria
        Coordenadas_Recta1 = generar_recta_aleatoria()
        # Almacenamos la recta generada en la lista
        lista_coordenadas_rectas.append(Coordenadas_Recta1)
    # Devolvemos la lista con todas las rectas generadas
    return lista_coordenadas_rectas
    
# ALGORITMO DDA
def DDA(x0, y0, x1, y1):
    m = (y1 - y0) / (x1 - x0)
    y = y0
    for x in range(x0, x1 + 1):
        plot(x, int(y))
        y = y + m

# Modulo para graficar rectas mediante el algoritmo de linea DDA
def graficar_rectas_DDA(lista_coordenadas_rectas):
    glClear(GL_COLOR_BUFFER_BIT) # Preparamos la venta de graficos
    glColor3f(1.0, 0.0, 0.0) # Establecemos el color de dibujo a rojo
    # Iteramos para cade elemento de lista_coordenadas_rectas
    for rectaN in lista_coordenadas_rectas:
        # Recuperamos los parametros de la rectaN
        x0 = rectaN[0]
        y0 = rectaN[1]
        x1 = rectaN[2]
        y1 = rectaN[3]
        # Graficamos la recta mediante el algoritmo de linea DDA
        DDA(x0, y0, x1, y1)

# Modulo para dibujar coordenadas
def plot(ix, iy):
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

# Modulo para graficar las rectas y sus respectivas intersecciones
def graficar_rectas_intersecciones():
    graficar_rectas_DDA(lista_coordenadas_rectas_aleatorias) # Graficamos las rectas
    graficar_puntos_interseccion(lista_coordenadas_rectas_aleatorias) # Graficamos sus intersecciones
    glFlush() 

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0) # Establecemos el fondo en blanco
    #glClearColor(0.0, 0.0, 0.0, 0.0) # Establecemos el fondo en negro
    glPointSize(1.0) # Establecemos el tamaño de linea en 1 pixel
    glMatrixMode(GL_PROJECTION) #
    glLoadIdentity() #
    gluOrtho2D(0.0, 499.0, 0.0, 499.0) #

def main():
    glutInit(sys.argv) #
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) #
    glutInitWindowSize(500, 500) #
    glutInitWindowPosition(0, 0) #
    glutCreateWindow(b"Intersecciones de 5 rectas") # Establecemos el titlo
    glutDisplayFunc(graficar_rectas_intersecciones) # 
    myinit() # 
    glutMainLoop() #

# Programa principal
if __name__ == "__main__":
    # Establecemos el Nro de rectas aleatorias que se desea graficar = 10
    lista_coordenadas_rectas_aleatorias = generar_rectas_aleatorias(10)
    main()
