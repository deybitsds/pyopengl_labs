from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variable
angle = 0.0  # Current rotational angle of the shapes

# Initialize OpenGL Graphics
def initGL():
    # Set "clearing" or background color
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black and opaque

# Called back when there is no other event to be handled
def idle():
    glutPostRedisplay()  # Post a re-paint request to activate display()

# Handler for window-repaint event. Call back when the window first
# appears and whenever the window needs to be re-painted.
def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()  # Reset the model-view matrix


    ''' ACA '''
    glPushMatrix()  # Save model-view matrix setting
    glTranslatef(-0.5, 0.4, 0.0)  # Translate
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate by angle in degrees
    glColor3f(0.5, 1.0, 0.7)
    glBegin(GL_QUADS)  # Each set of 4 vertices form a quad
    cero_tres = 0.3
    glVertex2f(-cero_tres, -cero_tres)
    glVertex2f(cero_tres, -cero_tres)
    glVertex2f(cero_tres, cero_tres)
    glVertex2f(-cero_tres, cero_tres)
    glEnd()

    glPopMatrix()  # Restore the model-view matrix


    ''' ACA'''
    glPushMatrix()  # Save model-view matrix setting
    glTranslatef(-0.4, -0.3, 0.0)  # Translate
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate by angle in degrees

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.7)
    glVertex2f(-cero_tres, -cero_tres)
    glVertex2f(cero_tres, -cero_tres)
    glVertex2f(cero_tres, cero_tres)
    glVertex2f(-cero_tres, cero_tres)
    glEnd()

    glPopMatrix()  # Restore the model-view matrix

    glutSwapBuffers()  # Double buffered-swap the front and back buffers
    # Change the rotational angle after each display()
    angle += 0.2

# Main function: GLUT runs as a console application starting at main()
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE)  # Enable double buffered mode
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Animation via Idle Function")
    glutDisplayFunc(display)
    glutIdleFunc(idle)  # Register callback handler if no other event
    initGL()  # Our own OpenGL initialization
    glutMainLoop()  # Enter the infinite event-processing loop

if __name__ == "__main__":
    main()
