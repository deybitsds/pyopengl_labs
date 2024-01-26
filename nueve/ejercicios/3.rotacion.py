from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

WIDTH, HEIGHT = 800, 800
C = [[0] * 1 for _ in range(8)]


def multiplicacion(A, FA, CA, B, FB, CB, C):
    if CA == FB:
        for i in range(FA):
            for j in range(CB):
                C[i][j] = 0
                for k in range(CA):
                    C[i][j] += A[i][k] * B[k][j]


def ejes():
    glBegin(GL_LINES)
    glVertex3i(0, 0, 0)  # eje Y
    glVertex3i(0, 50, 0)
    glVertex3i(0, 0, 0)  # eje X
    glVertex3i(50, 0, 0)
    glVertex3i(0, 0, 0)  # eje Z
    glVertex3i(0, 0, 50)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  # color amarillo
    ejes()  # dibuja los ejes
    glColor3f(1.0, 0.0, 0.0)  # color rojo

    # Definir los puntos del tercer cubo
    cubo = [
    [-2.0, -2.0, -2.0, 1.0],
    [0.0, -2.0, -2.0, 1.0],
    [0.0, 0.0, -2.0, 1.0],
    [-2.0, 0.0, -2.0, 1.0],
    [-2.0, -2.0, 0.0, 1.0],
    [0.0, -2.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 1.0],
    [-2.0, 0.0, 0.0, 1.0]
]

    # Calcular el vector de la línea de rotación para el tercer cubo
    vector_rotacion = [1, 2, 1]

    # Normalizar el vector de rotación
    norma = np.linalg.norm(vector_rotacion)
    vector_rotacion = [v / norma for v in vector_rotacion]

    # Construir la matriz de rotación 3D para el tercer cubo
    angulo = np.radians(30)
    cos_theta = np.cos(angulo)
    sin_theta = np.sin(angulo)
    u, v, w = vector_rotacion
    mat_rotacion = [
        [cos_theta + u**2 * (1 - cos_theta), u * v * (1 - cos_theta) - w * sin_theta, u * w * (1 - cos_theta) + v * sin_theta, 0],
        [v * u * (1 - cos_theta) + w * sin_theta, cos_theta + v**2 * (1 - cos_theta), v * w * (1 - cos_theta) - u * sin_theta, 0],
        [w * u * (1 - cos_theta) - v * sin_theta, w * v * (1 - cos_theta) + u * sin_theta, cos_theta + w**2 * (1 - cos_theta), 0],
        [0, 0, 0, 1]
    ]

    # Realizar la transformación para el tercer cubo
    cubo_rotado = [np.dot(mat_rotacion, np.array(p)).tolist() for p in cubo]

    # Dibujar el tercer cubo original
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    for i in range(0, 4):
        glVertex3f(cubo[i][0], cubo[i][1], cubo[i][2])
    glEnd()

    glBegin(GL_QUADS)
    for i in range(4, 8):
        glVertex3f(cubo[i][0], cubo[i][1], cubo[i][2])
    glEnd()

    for i in range(4):
        glBegin(GL_LINES)
        glVertex3f(cubo[i][0], cubo[i][1], cubo[i][2])
        glVertex3f(cubo[i + 4][0], cubo[i + 4][1], cubo[i + 4][2])
        glEnd()

    # Dibujar el tercer cubo rotado
    glColor3f(0.0, 1.0, 0.0)  # color verde
    glBegin(GL_QUADS)
    for i in range(0, 4):
        glVertex3f(cubo_rotado[i][0], cubo_rotado[i][1], cubo_rotado[i][2])
    glEnd()

    glBegin(GL_QUADS)
    for i in range(4, 8):
        glVertex3f(cubo_rotado[i][0], cubo_rotado[i][1], cubo_rotado[i][2])
    glEnd()

    for i in range(4):
        glBegin(GL_LINES)
        glVertex3f(cubo_rotado[i][0], cubo_rotado[i][1], cubo_rotado[i][2])
        glVertex3f(cubo_rotado[i + 4][0], cubo_rotado[i + 4][1], cubo_rotado[i + 4][2])
        glEnd()

    glutSwapBuffers()


def ini():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -3, 3, -3, 3)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Rotación Tercer Cubo 3D")
    glutDisplayFunc(display)
    ini()
    glutMainLoop()


if __name__ == "__main__":
    main()
