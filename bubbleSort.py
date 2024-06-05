def bubbleSort(arr):
    for i in range(len(arr)):
        #Por cada elemento se recorre toda la lista descartando los ya ordenados
        #los elementos mas grandes son movidos al final de la lista y ya no es necesario vorver a compararlos
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
if __name__ == '__main__':
    arr = [4,3,2,12,5,6,3,6,23]
    result = bubbleSort(arr)
    print(result)