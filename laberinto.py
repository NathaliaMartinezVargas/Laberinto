def camino(archivo):
    return [x.split(" ") for x in open(archivo).readlines()]

def buscar_en_matriz(matriz, cont, valor):
    if matriz == []:
      return (-1, -1)
    if valor in matriz[0]:
      return (cont, matriz[0].index(valor))
    return buscar_en_matriz(matriz[1:], cont + 1, valor)

def movRight(y,x,matriz,movimientos):
  if (x+1) >= len(matriz[0]) or (x+1) < 0 or matriz[y][x+1] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    movRight(y,x+1,matriz,movimientos+[[y,x]])

def movUp(y,x,matriz,movimientos):
  if (y-1) >= len(matriz) or (y-1) < 0 or matriz[y-1][x] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    movUp(y-1,x,matriz,movimientos+[[y,x]])

def movLeft(y,x,matriz,movimientos):
  if (x-1) >= len(matriz[0]) or (x-1) < 0 or matriz[y][x-1] == '1' or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    movLeft(y,x-1,matriz,movimientos+[[y,x]])

def movDown(y, x, matriz, movimientos):
  if (y+1) >= len(matriz) or (y+1) < 0 or matriz[y+1][x] == '1'or matriz[y][x] == 'Y':
    mover(y,x,matriz,movimientos+[[y,x]])
    pass
  else:
    movDown(y+1, x, matriz, movimientos+[[y,x]])

def mover(y,x,matriz,movimientos):
  if (y,x)== buscar_en_matriz(matriz,0,'Y'):
    print(movimientos)
  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y < buscar_en_matriz(matriz,0,'Y')[0] and matriz[y+1][x] != '1'):
    movDown(y, x, matriz, movimientos)
  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x < buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x+1] != '1') :
    movRight(y, x, matriz, movimientos)

  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y > buscar_en_matriz(matriz,0,'Y')[0] and matriz[y-1][x] != '1'):
    movUp(y, x, matriz, movimientos)

  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x > buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x-1] != '1'):
    movLeft(y, x, matriz, movimientos)

print("Posición X =", buscar_en_matriz(camino('matriz.txt'), 0, "X"))
print("Posición Y =", buscar_en_matriz(camino('matriz.txt'), 0, "Y"))
print(mover(buscar_en_matriz(camino('matriz.txt'), 0, "X")[0],buscar_en_matriz(camino('matriz.txt'), 0, "X")[1], camino('matriz.txt'), []))
