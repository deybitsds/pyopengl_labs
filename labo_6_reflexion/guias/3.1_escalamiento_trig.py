import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def escalarPunto(x0, y0, x1, y1, Sx, Sy):
    matriz_S = np.array([[Sx, 0],[0, Sy]])
    matriz_p1_p0 = np.array([[x1 - x0] , [y1 - y0]])
    matriz_p0 = np.array([[x0], [y0]])
    matriz_p2 = np.dot(matriz_S, matriz_p1_p0) + matriz_p0    
    [x2, y2] = [matriz_p2[0, 0], matriz_p2[1, 0]]
    return [x2, y2]

def graficar_recta_por_puntos(lista_parametros_punto):
    glVertex2f(lista_parametros_punto[0], lista_parametros_punto[1])

def graficar_triangulo(lista_parametros_punto_A, lista_parametros_punto_B, lista_parametros_punto_C):
    glBegin(GL_LINE_LOOP)
    graficar_recta_por_puntos(lista_parametros_punto_A)    
    graficar_recta_por_puntos(lista_parametros_punto_B) 
    graficar_recta_por_puntos(lista_parametros_punto_C) 
    glEnd()

def escalarTriangulo(x1, y1, x2, y2, x3, y3, Sx, Sy):
    
    # Escalar cada punto manteniendo fijo el punto [x3, y3]
    punto_1_escalado = escalarPunto(x3, y3, x1, y1, Sx, Sy)
    punto_2_escalado = escalarPunto(x3, y3, x2, y2, Sx, Sy)

    # Dibujar el triángulo escalado 
    graficar_triangulo(punto_1_escalado, punto_2_escalado, [x3, y3])

    # Dibujar el triángulo original
    graficar_triangulo([x1, y1],[x2, y2],[x3, y3])

def display():
    x1, y1, x2, y2, x3, y3, Sx, Sy = 120.0, 160.0, 150.0, 300.0, 60.0, 100.0, 0.5, 0.5
    glClear(GL_COLOR_BUFFER_BIT)
    escalarTriangulo(x1, y1, x2, y2, x3, y3, Sx, Sy)
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
    glutCreateWindow("Escalamiento")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()