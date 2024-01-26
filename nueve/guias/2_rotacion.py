from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

WIDTH, HEIGHT = 600, 600
C = [[0] * 1 for _ in range(4)]


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

    A1 = [[0.0], [0.0], [0.0], [1.0]]
    B1 = [[20.0], [0.0], [0.0], [1.0]]
    C1 = [[0.0], [20.0], [0.0], [1.0]]
    D1 = [[0.0], [0.0], [20.0], [1.0]]

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(A1[0][0], A1[1][0], A1[2][0])
    glVertex3f(B1[0][0], B1[1][0], B1[2][0])
    glVertex3f(C1[0][0], C1[1][0], C1[2][0])
    glVertex3f(D1[0][0], D1[1][0], D1[2][0])
    glVertex3f(A1[0][0], A1[1][0], A1[2][0])
    glEnd()

    T = [
        [0.7071, -0.5, 0.5, 0.5],
        [0.5, 0.8536, 0.1464, 0.1464],
        [-0.5, 0.1464, 0.8536, -0.1464],
        [0, 0, 0, 1]
    ]

    multiplicacion(T, 4, 4, A1, 4, 1, C)
    A2 = [[C[0][0]], [C[1][0]], [C[2][0]], [C[3][0]]]

    multiplicacion(T, 4, 4, B1, 4, 1, C)
    B2 = [[C[0][0]], [C[1][0]], [C[2][0]], [C[3][0]]]

    multiplicacion(T, 4, 4, C1, 4, 1, C)
    C2 = [[C[0][0]], [C[1][0]], [C[2][0]], [C[3][0]]]

    multiplicacion(T, 4, 4, D1, 4, 1, C)
    D2 = [[C[0][0]], [C[1][0]], [C[2][0]], [C[3][0]]]

    glColor3f(0.0, 1.0, 0.0)  # color verde
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(A2[0][0], A2[1][0], A2[2][0])
    glVertex3f(B2[0][0], B2[1][0], B2[2][0])
    glVertex3f(C2[0][0], C2[1][0], C2[2][0])
    glVertex3f(D2[0][0], D2[1][0], D2[2][0])
    glVertex3f(A2[0][0], A2[1][0], A2[2][0])
    glEnd()

    glutSwapBuffers()


def ini():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50.0, 50.0, -50.0, 50.0, -50.0, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(45.0, 3.0, 3.0, 3.0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Rotacion 3D")
    glutDisplayFunc(display)
    ini()
    glutMainLoop()


if __name__ == "__main__":
    main()
