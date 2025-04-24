def selectionSort(arr):
    if len(arr) <= 1: return
    #inicia el ciclo desde el indice 0 y lo evalua contra el resto de la lista desordenada
    for i in range(len(arr) - 1): 
        min_index = i# i se vuelve el valor de mi elemento mas pequino, hacendo a un lado todos lo elmentos por debajo de estos 
        #dando a ententer que estos ya se encuentran en su posiscion correcta
        for j in range(i,len(arr)):
            #Se crea un ciclo donde se busca encontrar un elemento que sea menor al que se encuentra en el indice min_index (elegido como el minor de la lista)
            #al en contrar alguno se SELECCIONA  su indice y se almacena en la variable min_index y haci hasta terminar de recorrer toda la lista
            if arr[j] < arr[min_index]:
                min_index = j
        #Al final se intercambian ossciones la posicion actual "i" con min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
   arr =  [21, 6, 9, 33, 3]
   selectionSort(arr)
   print('insert sorted:', arr)