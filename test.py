
#Imprimee la matriz de forma lineal 
"""
f = open("Matriz.txt", "r")
lineas = f.readlines()

print(lineas)
 
# Imprime la matriz de forma cuadratica
with open('Matriz.txt', 'r') as matriz:
    print(matriz.read())

"""
def mapa(archivo):
    return [x.split(" ") for x in open(archivo).readlines()]


def buscar_en_matriz(matriz, contador, letra):
    if matriz == []:
        return (-1, -1)
    if letra in matriz[0]:
        return (contador, matriz[0].index(letra))
    return buscar_en_matriz(matriz[1:], contador + 1, letra)

def moverDerecha(y,x,matriz,movimientos):
  if (x+1) >= len(matriz[0]) or (x+1) < 0 or matriz[y][x+1] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:  
    moverDerecha(y,x+1,matriz,movimientos+[[y,x]])

def moverArriba(y,x,matriz,movimientos):
  if (y-1) >= len(matriz) or (y-1) < 0 or matriz[y-1][x] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    moverArriba(y-1,x,matriz,movimientos+[[y,x]])
    
def moverIzquierda(y,x,matriz,movimientos):
  if (x-1) >= len(matriz[0]) or (x-1) < 0 or matriz[y][x-1] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    moverIzquierda(y,x-1,matriz,movimientos+[[y,x]])

def moverAbajo(y, x, matriz, movimientos):
  if (y+1) >= len(matriz) or (y+1) < 0 or matriz[y+1][x] == '1'or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    moverAbajo(y+1, x, matriz, movimientos+[[y,x]])    

def mover(y,x,matriz,movimientos):
  if (y,x)== buscar_en_matriz(matriz,0,'Y'):
    print(movimientos)
  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y < buscar_en_matriz(matriz,0,'Y')[0] and matriz[y+1][x] != '1'):
    #Abajo
    moverAbajo(y, x, matriz, movimientos)
  
  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x < buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x+1] != '1') :
    #Derecha
    moverDerecha(y, x, matriz, movimientos)

  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y > buscar_en_matriz(matriz,0,'Y')[0] and matriz[y-1][x] != '1'):
    #moverArriba
    moverArriba(y, x, matriz, movimientos)

  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x > buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x-1] != '1'):
    #Izquierda
    moverIzquierda(y, x, matriz, movimientos)    

print(mapa("matriz.txt"))
print("posición X = ", buscar_en_matriz(mapa("matriz.txt"),0,"X"))
print("posición Y = ", buscar_en_matriz(mapa("matriz.txt"),0,"Y"))



