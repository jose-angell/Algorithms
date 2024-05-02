def InsertSort(arr):
    #Valida que el array no este valico o que sea igual a 1
    if len(arr) <= 1: return 
    for i in range(1,len(arr)):#Recorre todo el array tomando el valor del indice 0 como la sublista ordenada y el resto la sublista desordenada
        j=i #Posicion inicial de la clave
        while j > 0 and arr[j-1] > arr[j]:#valida si es necesario cambiar la posicio de la clave, si lo es se intercambia el valor
            #de la clave por el de una posicio anterrior
            #!intercambio de posiciones
            aux = arr[j -1]
            arr[j - 1] = arr[j]
            arr[j] = aux
            j-=1


if __name__ == '__main__':
   arr = [5, 3, 4, 2, 1]
   InsertSort(arr)
   print('insert sorted:', arr)