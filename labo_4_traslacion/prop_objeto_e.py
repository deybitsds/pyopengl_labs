from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

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

def generar_nro_aleatorio(min,max):
    nro_aleatorio = random.randint(min,max)
    return nro_aleatorio

# Funcion para generar automaticamente un objeto e
def generar_parametros_iniciales_objeto_e_aleatorio():
    # Establecemos el tamaño de la pantalla
    xmax = 499
    ymax = 499
    # Generamos numeros aleatorios que quepan en la mitad de la pantalla
    k = generar_nro_aleatorio(1,30)
    x0 = generar_nro_aleatorio(10,120)
    y0 = generar_nro_aleatorio(10,120)
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
    
def graficar_objeto_e(lista_de_lista_de_rectas):
    # Para cada recta A de la lista de listas graficar la recta A
    for e in lista_de_lista_de_rectas:
        # Graficamos la recta mediante el algoritmo DDA
        graficar_una_recta_DDA(e)
    
def trasladar_objeto_e(lista_rectas_objeto_e, vector_de_traslacion):
    # Para cada recta del Objeto E
    for e in lista_rectas_objeto_e:
        # Incrementamos Tx y Ty a los puntos de la recta
        e[0][0] += vector_de_traslacion[0]
        e[0][1] += vector_de_traslacion[1]
        e[1][0] += vector_de_traslacion[0]
        e[1][1] += vector_de_traslacion[1]
    # Devolvemos las nuevas rectas del Objeto E
    return lista_rectas_objeto_e

def generar_y_graficar_objeto_e_aleatorio():
    # Generar parametros iniciales aleatorios para el objeto E
    lista_parametros_iniciales_e_aleatorio = generar_parametros_iniciales_objeto_e_aleatorio()
    # Generar rectas del objeto E con los parametros inciales aleatorios
    objeto_e_aleatorio = generar_puntos_objeto_e(lista_parametros_iniciales_e_aleatorio)
    # Graficar objeto E
    graficar_objeto_e(objeto_e_aleatorio)
    # Devolvemos la lista de rectas (Objeto E)
    return objeto_e_aleatorio

# Funcion para
def trasladaObjetoE():
    # graficar objeto E inicial
    objeto_e_aleatorio = generar_y_graficar_objeto_e_aleatorio()
    T = [250, 150]  # Vector de traslación
    # calcular traslacion
    nuevo_objeto_e = trasladar_objeto_e(objeto_e_aleatorio,T)
    # graficar objeto e final
    graficar_objeto_e(nuevo_objeto_e)

# Despliega el gráfico
def display():

    glClear(GL_COLOR_BUFFER_BIT)  # Establece el color de la ventana
    trasladaObjetoE()  # Traslada objeto E
    glFlush()  # Fuerza la ejecución de los comandos de OpenGL

# Inicializa OpenGL
def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)  # Activa la matriz de transformación
    glLoadIdentity()  # Carga la identidad para poder hacer transformaciones
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)  # Establece una ventana de dibujo 2D

# Función principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  # Ventana 500x500 píxeles
    glutInitWindowPosition(0, 0)  # Coloca la ventana de despliegue en esq. sup. izq
    glutCreateWindow("Traslacion de Objeto E")  # Título de la ventana
    glutDisplayFunc(display)  # Llama a la función display cuando se abre la ventana
    myinit()  # Fija o establece los atributos
    glutMainLoop()  # Entra a un ciclo de evento

if __name__ == "__main__":
    main()