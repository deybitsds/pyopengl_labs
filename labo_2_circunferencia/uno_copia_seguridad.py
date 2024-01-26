

# FUNCIONES PARA CALCULAR LAS RECTAS

def calcular_un_diametro(h, k, r, grado):
    x1 = h

def calcular_seno_grados(grado):
    grado_radianes = math.radians(grado)
    seno = math.sin(grado_radianes)
    return seno

def calcular_tangente_grados(grado):
    grado_radianes = math.radians(grado)
    tangente = math.tan(grado_radianes)
    return tangente

def calcular_coseno_grados(grado):
    grado_radianes = math.radians(grado)
    coseno = math.cos(grado_radianes)
    return coseno

def calcular_un_radio(h, k, r, grado):
    seno = calcular_seno_grados(grado)
    coseno = calcular_coseno_grados(grado)
    x = h + r * coseno
    y = k + r * seno 
    return [x, y]

def calcular_un_diametro(h, k, r, grado):
    return 1

def graficar_radios(h, k, r, lista_grados):

    for grado in lista_grados:
        [x, y] = calcular_un_radio(h, k, r, grado)

def calcular_diametros(h,k,r, lista_grados):
    lista_diametros = []
    for grado in lista_grados:
        diametro_nuevo = calcular_un_diametro(h,k,r,grado)
        lista_diametros.append(diametro_nuevo)

def graficar_una_recta(lista_parametros):
    x0 = lista_parametros[0]
    y0 = lista_parametros[1]
    x1 = lista_parametros[2]
    y1 = lista_parametros[3]
    '''
    ACA GRAFICAR LA RECTA
    '''
    #DDA(x0, y0, x1, y1)

def graficar_rectas(lista_rectas):
    for elem in lista_rectas:
        graficar_una_recta(elem)

a = 30
#y = calcular_seno_grados(30)
z = calcular_un_radio(5,5,3, 360)
print()
print(z)
#print(calcular_tangente(120))