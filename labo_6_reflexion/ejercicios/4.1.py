from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *

def circuloPtoMedio(x0, y0, r):
    hm, x,y = 5 / 4 - r, 0, -r
    plot(x0, y0 + r)
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)
    while x < -(y + 1):
        if hm < 0:
            hm = hm + 2 * x + 3
        else:
            hm = hm + 2 * x + 2 * y + 5
            y = y + 1
        x = x + 1
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)


def graficar_circunferencia(lista_parametros):
    [x, y, r] = lista_parametros
    circuloPtoMedio(x, y, r)

def escalar_circunferencia(lista_parametros_circunferencia_inicial, variacion):
    [x, y, r] = lista_parametros_circunferencia_inicial
    return [x, y, r * variacion]

# Función para mostrar el grafico ------------------------------------

# Función para dibujar un punto
def plot(ix, iy):
    ix = int(ix)
    iy = int(iy)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Graficar Circunferencia Inicial
    parametros_circunferencia_inicial = [200, 200, 50] # (Cx, Cy) ; R
    glColor3f(1.0, 0.0, 0.0)    
    graficar_circunferencia(parametros_circunferencia_inicial)

    # Escalar
    variacion = 2
    parametros_circunferencia_escalada = escalar_circunferencia(parametros_circunferencia_inicial,variacion)
    
    # Graficar Circunferencia Final
    glColor3f(0.0, 1.0, 0.0) 
    graficar_circunferencia(parametros_circunferencia_escalada)
    glFlush()

def myinit():
    global xmin, ymin, xmax, ymax
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Escalamiento de una circunferencia")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

# Programa Principal
if __name__ == "__main__":
    [xmin, ymin, xmax, ymax] = 0.0, 0.0, 400.0,400.0
    main()