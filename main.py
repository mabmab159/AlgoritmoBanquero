import numpy as np

asignados = [
    [1, 0, 2, 1, 1],
    [2, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0]
]

maximos = [
    [1, 2, 2, 1, 2],
    [2, 2, 2, 1, 0],
    [2, 1, 3, 1, 0],
    [1, 1, 2, 2, 1]
]

texto = ""
cantidadLineas = 0
disponibles = [0, 0, 2, 1, 1]
pendientes = []
for i in range(len(maximos)):
    auxiliar = []
    for j in range(len(maximos[0])):
        if maximos[i][j] - asignados[i][j] >= 0:
            auxiliar.append(maximos[i][j] - asignados[i][j])
        else:
            auxiliar.append(0)
    pendientes.append(auxiliar)

while np.sum(asignados) != 0:
    arreglo_maximo = []
    realizado = False
    for i in range(len(pendientes)):
        if realizado:
            break
        arreglo_maximo = []
        for j in range(len(pendientes[0])):
            if pendientes[i][j] <= disponibles[j]:
                arreglo_maximo.append(asignados[i][j])
            else:
                arreglo_maximo = []
                break
            if len(arreglo_maximo) == 5:
                if sum(arreglo_maximo) == 0:
                    arreglo_maximo = []
                    break
                else:
                    for k in range(5):
                        disponibles[k] = disponibles[k] + asignados[i][k]
                        asignados[i][k] = 0
                    realizado = True
                    texto = texto + f"Se concluye el proceso {i}\n"
                    break
    texto = texto + f"Se libera los siguientes recursos {arreglo_maximo}\n"
    texto = texto + f"Memoria disponible {disponibles}\n"
    for i in texto:
        if i == "\n":
            cantidadLineas = cantidadLineas + 1

print(texto)
