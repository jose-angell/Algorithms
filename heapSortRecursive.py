def heapify(arr, n, i):
    largest = i
    #calculo las posisciones de los hijos l(hijo izquierdo) r(hijo derecho)
    l = 2 * i + 1 #posicion del hijo izquierdo 
    r = 2 * i + 2 #posicion del hijoo derecho
    #en las siguientes condicionales se busca al hijo que sea mayor al padre para intercambiarlo con este
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:# si el padre no es el mayor de ambos hijos se intercambia con elmayor
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # con esta recursividad se cubre en el caso de que este l o r tengan hijos

def heapSort(arr):
    n = len(arr)
    # Construir un montículo máximo
    for i in range((n-1) // 2, -1, -1):
        heapify(arr, n, i)
    # Extraer elementos uno por uno

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == '__main__':

    arr = [5,8,6,1,4,7,3,9,2,0]
    heapSort(arr)
    print("Arreglo ordenado:")
    print(arr)
