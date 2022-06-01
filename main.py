def validar_configuracion(asignados, maximos, disponibles):
    finalizados = []
    i = 0


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
                break

print(arreglo_maximo)
print(asignados)
print(disponibles)

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
                continue
            else:
                for k in range(5):
                    disponibles[k] = disponibles[k] + asignados[i][k]
                    asignados[i][k] = 0
                realizado = True
                break

print(arreglo_maximo)
print(asignados)
print(disponibles)

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
        if len(arreglo_maximo) >= 5:
            if sum(arreglo_maximo) == 0:
                arreglo_maximo = []
                continue
            else:
                for k in range(5):
                    disponibles[k] = disponibles[k] + asignados[i][k]
                    asignados[i][k] = 0
                realizado = True
                break

print(arreglo_maximo)
print(asignados)
print(disponibles)

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
        if len(arreglo_maximo) >= 5:
            if sum(arreglo_maximo) == 0:
                arreglo_maximo = []
                continue
            else:
                for k in range(5):
                    disponibles[k] = disponibles[k] + asignados[i][k]
                    asignados[i][k] = 0
                realizado = True
                break

print(arreglo_maximo)
print(asignados)
print(disponibles)