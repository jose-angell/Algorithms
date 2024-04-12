def insertionSort(array):
    #si el tamano de la lista es 1 o 0 la lista ya esta ordenada
    if len(array) <= 1: return  array
    #recorre la lista completa tomando como inicio el indice 1, el indice 0 se toma como el subarray ordenado inicial
    for i in range(1,len(array)): 
        #j representa el inicio (la posicion del ultimo elemento) del subarray ordenado; el valor de key es el numero que se quiere
        # ordenar en esta iteracion 
        (j, key) = (i-1, array[i])       
        while j>=0 and array[j]>key: #lista hordenada, se recorre la lista ordenada hasta que j sea menor a cero
            # dando a entender que el valor a ordenar es el mas pequeno de la lista ordenada, o si el valor de mi lista ordenada
            # es mayor a mi  valor a ordenar, recoriendolo una posiscion a la derecha
            array[j+1] = array[j] #copia el valor a una posicion a la derecha si el valor es mayor a key
            j-=1 
        array[j+1] = key #coloca el valor en su lugar 
    return array



if __name__ == '__main__':
    array = [70,60,0,90,80,85,-1]
    sortArray = insertionSort(array)
    print(sortArray)