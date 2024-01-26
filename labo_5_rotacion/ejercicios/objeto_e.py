from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# FUNCIONES MATEMATICAS

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

# Modulo para graficar DDA cuando el parametro es una lista
def graficar_una_recta_DDA(lista_parametros):
 # Recuperamos los parametros de la rectaN
    [x0,y0] = lista_parametros[0]
    [x1,y1] = lista_parametros[1]
    # Graficamos la recta mediante el algoritmo de linea DDA
    DDA_mejorado(int(x0), int(y0), int(x1), int(y1))

def graficar_objeto_e(lista_de_lista_de_rectas):
    # Para cada recta A de la lista de listas graficar la recta A
    for e in lista_de_lista_de_rectas:
        # Graficamos la recta mediante el algoritmo DDA
        graficar_una_recta_DDA(e)

''' xdxd '''
# --- Modulos para calcular
def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

def calcular_rotacion_recta(lista_coordenadas_recta, angulo):
    punto_a_inicial = lista_coordenadas_recta[0]
    punto_a_final = lista_coordenadas_recta[1]
    
    punto_b_inicial = calcular_rotacion_punto(punto_a_inicial, angulo)
    punto_b_final = calcular_rotacion_punto(punto_a_final, angulo)

    return [punto_b_inicial, punto_b_final]

# Funcion para
def rotar_objeto_e(lista_puntos_objeto_e, angulo):
    lista_parametros_objeto_e_rotado = []
    for elem in lista_puntos_objeto_e:
        lista_parametros_objeto_e_rotado.append(calcular_rotacion_recta(elem, angulo))
    return lista_parametros_objeto_e_rotado

def calcular_rotacion_punto(lista_coordenadas_punto, angulo):
    [x, y] = lista_coordenadas_punto
    seno = calcular_seno_angulo(angulo)
    coseno = calcular_coseno_angulo(angulo)
    x1 = x * coseno - y * seno
    y1 = y * coseno + x * seno
    return [x1, y1]

# Funcion para generar automaticamente un objeto e
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
    return [x0,y0,k]

def generar_puntos_objeto_e(lista_parametros_iniciales):
    # Recuperar paramatros iniciales
    [x, y, k] = lista_parametros_iniciales
    lista_de_lista_de_rectas = []
    # Generar puntos
    lista_de_lista_de_rectas.append([[x,y], [x + 4 * k, y]])
    lista_de_lista_de_rectas.append([[x + 4 * k, y], [x + 4 * k, y  + k]])
    lista_de_lista_de_rectas.append([[x + 4 * k, y  + k], [x + k, y + k]])
    lista_de_lista_de_rectas.append([[x + k, y + k], [x + k, y + 2 * k]])
    lista_de_lista_de_rectas.append([[x + k, y + 2 * k], [x + 2 * k, y + 2 * k]])
    lista_de_lista_de_rectas.append([[x + 2 * k, y + 2 * k], [x + 2 * k, y + 3 * k]])
    lista_de_lista_de_rectas.append([[x + 2 * k, y + 3 * k], [x + k, y + 3 * k]])
    lista_de_lista_de_rectas.append([[x + k, y + 3 * k], [x + k, y + 4 * k]])
    lista_de_lista_de_rectas.append([[x + k, y + 4 * k], [x + 4 * k, y + 4 * k]])
    lista_de_lista_de_rectas.append([[x + 4 * k, y + 4 * k], [x + 4 * k, y + 5 * k]])
    lista_de_lista_de_rectas.append([[x + 4 * k, y + 5 * k], [x, y + 5 * k]])
    lista_de_lista_de_rectas.append([[x, y + 5 * k], [x, y]])
    # Devolver lista con las rectas
    return lista_de_lista_de_rectas
    
def generar_y_graficar_objeto_e_aleatorio():
    # Generar parametros iniciales aleatorios para el objeto E
    lista_parametros_iniciales_e_aleatorio = generar_parametros_iniciales_objeto_e_aleatorio()
    # Generar rectas del objeto E con los parametros inciales aleatorios
    parametros_objeto_e_aleatorio = generar_puntos_objeto_e(lista_parametros_iniciales_e_aleatorio)
    # Graficar objeto E
    graficar_objeto_e(parametros_objeto_e_aleatorio)
    # Devolvemos la lista de rectas (Objeto E)
    return parametros_objeto_e_aleatorio

# Despliega el gráfico
def display():

    glClear(GL_COLOR_BUFFER_BIT)  # Establece el color de la ventana
    glColor3f(0.0, 1.0, 0.0)
    objeto_e_aleatorio = generar_y_graficar_objeto_e_aleatorio()  # Traslada objeto E
    grado_minimo, grado_maximo = 0, 360
    angulo = generar_nro_aleatorio(grado_minimo, grado_maximo)
    angulo = 10
    nuevo_objeto_e = rotar_objeto_e(objeto_e_aleatorio, angulo)
    glColor3f(1.0, 0.0, 0.0)
    graficar_objeto_e(nuevo_objeto_e)
    
    glFlush()  # Fuerza la ejecución de los comandos de OpenGL

# Inicializa OpenGL
def myinit():
    global xmin, xmax, ymin, ymax
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glPointSize(1.0)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)  # Activa la matriz de transformación
    glLoadIdentity()  # Carga la identidad para poder hacer transformaciones
    gluOrtho2D(xmin, xmax, ymin, ymax)  # Establece una ventana de dibujo 2D

# Función principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)  # Ventana 500x500 píxeles
    glutInitWindowPosition(0, 0)  # Coloca la ventana de despliegue en esq. sup. izq
    glutCreateWindow("Rotacion de Objeto E")  # Título de la ventana
    glutDisplayFunc(display)  # Llama a la función display cuando se abre la ventana
    myinit()  # Fija o establece los atributos
    glutMainLoop()  # Entra a un ciclo de evento

if __name__ == "__main__":
    xmin, xmax, ymin, ymax = 0, 699, 0, 699
    main()