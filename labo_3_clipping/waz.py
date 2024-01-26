'''
def waza(a,b):
    return [a+b,a-b]

[x,y] = waza(3,2)
print(x)
print(y) 

def parametrica():
    global lista_rectas, lista_coordenadas_rectangulo
    lista_rectas_cortadas = []
    for elem in lista_rectas:
        parametrica1(lista_rectas_cortadas)
    print(lista_rectas_cortadas)

def parametrica1(lista_rectas_cortadas):
    lista_rectas_cortadas.append([2])

lista_coordenadas_rectangulo = [8,2,3,4]
lista_rectas = [[1,2,3,4],[5,6,7,8],["hola"]]
parametrica()
'''
def leer_rectas():
    numero_rectas = int(input("Ingrese nro rectas: "))
    lista_rectas_a_devolver = []
    for k in range(0,numero_rectas):
        print("RECTA " + str(k + 1))
        una_recta = leer_una_recta()
        lista_rectas_a_devolver.append(una_recta)
    return lista_rectas_a_devolver

def leer_una_recta():
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    return [x0,y0,x1,y1]

#l = leer_rectas()
def funcion_waza(tline, l):
    x = 1
    y = 5
    l.append(x,)
    l.append(y)

lista = [2,3]
funcion_waza(2,lista)
print(lista)
print(len(lista))