
def mergeSort(arr):
    if len(arr) == 1: #Caso base 
        return arr
    midIndex = len(arr)//2
    midLeft = arr[:midIndex]
    midRight = arr[midIndex:]
    midLeft = mergeSort(midLeft)
    midRight = mergeSort(midRight)
    return merge(midLeft, midRight)

def merge(midLeft, midRight):
    print(f"Recibo {midLeft} y {midRight}")
    listSort= []
    while len(midLeft) > 0 and len(midRight) > 0 :
      if midLeft[0] < midRight[0]:
         listSort.append(midLeft[0])
         midLeft.pop(0)
      else:
         listSort.append(midRight[0])
         midRight.pop(0)

    while len(midLeft) > 0 :
      listSort.append(midLeft[0])
      midLeft.pop(0)

    while len(midRight) > 0:
      listSort.append(midRight[0])
      midRight.pop(0)
    print(f"Los ordeno y combino. Resultado: {listSort}.")
    return listSort

if __name__ == '__main__':

    arreglo = [9,6, 5, 3, 1, 8, 7, 2, 4]
    print(f"Arreglo original: {arreglo}")
    print("Ordenando con merge sort y recursividad...")
    arreglo_ordenado = mergeSort(arreglo)
    print(f"Arreglo ordenado: {arreglo_ordenado}")