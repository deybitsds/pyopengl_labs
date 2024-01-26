#ingresar datos
def leer_datos(nombre):
    a = int(input("Ingrese " + nombre + " : "))
    return a

#calcular
def calcular_tline1(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    num = ymin - y0
    den = y1 - y0
    return num/den

def calcular_tedge1(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    tline = calcular_tline1(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    num = (x0 - xmin + tline * (x1 - x0))
    den = xmax - xmin
    return num / den

def calcular_tline2(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    num = ymax - y0
    den = y1 - y0
    return num/den

def calcular_tedge2(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    tline = calcular_tline2(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    num = (x0 - xmin + tline * (x1 - x0))
    den = xmax - xmin
    return num / den

def calcular_tline3(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    num = xmin - x0
    den = x1 - x0
    return num/den

def calcular_tedge3(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    tline = calcular_tline3(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    num = (y0 - ymin + tline * (x1 - x0))
    den = (ymax - ymin)
    return num / den

def calcular_tline4(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    num = xmax - x0
    den = x1 - x0
    return num/den

def calcular_tedge4(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    tline = calcular_tline4(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    num = (y0 - ymin + tline * (x1 - x0))
    den = (ymax - ymin)
    return num / den

def calcular_x(x0,y0,x1,y1,xmin,ymin,xmax,ymax,funcion1):
    tline = funcion1(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    x = x0 + tline * (x1 - x0)
    return x

def calcular_y(x0,y0,x1,y1,xmin,ymin,xmax,ymax,funcion1):
    tline = funcion1(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
    y = y0 + tline * (y1 - y0)
    return y

def calcular_todos(x0,y0,x1,y1,xmin,ymin,xmax,ymax):
    print("UNO")
    print("tline 1: " + str(calcular_tline1(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("tedge 1: " + str(calcular_tedge1(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("DOS")
    print("tline 2: " + str(calcular_tline2(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("tedge 2: " + str(calcular_tedge2(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("TRES")
    print("tline 3: " + str(calcular_tline3(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("tedge 3: " + str(calcular_tedge3(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("CUATRO")
    print("tline 4: " + str(calcular_tline4(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print("tedge 4: " + str(calcular_tedge4(x0,y0,x1,y1,xmin,ymin,xmax,ymax)))
    print()

x0 = leer_datos("x0")
y0 = leer_datos("y0")
x1 = leer_datos("x1")
y1 = leer_datos("y1")

xmin = 3  #leer_datos("xmin")
ymin = 3  # leer_datos("ymin")
xmax = 15 #leer_datos("xmax")
ymax = 12 #leer_datos("ymax")

calcular_todos(x0,y0,x1,y1,xmin,ymin,xmax,ymax)
print("X: " + str(calcular_x(x0,y0,x1,y1,xmin,ymin,xmax,ymax,calcular_tline1)))
print("Y: " + str(calcular_y(x0,y0,x1,y1,xmin,ymin,xmax,ymax,calcular_tline1)))