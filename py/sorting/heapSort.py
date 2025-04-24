def swap(arr, i, j):#intercambia valores
   arr[i], arr[j] = arr[j], arr[i]

def heapif(arr, n):
   lastFather = (n - 1) //2 #calculo de la posicion del ultimo padre
   for i in range(lastFather, -1, -1):#partiendo el ultimo padre hasta el primero
      l = (2 * i) + 1 #posicion del hijo izquierdo  
      r = (2 * i) + 2 #posicion del hijo derecho
      largest = i
      if l < n and arr[i] < arr[l]: #valida si el hijo izquierdo es mayor que el padre
        largest = l
      if r < n and arr[largest] < arr[r]: #valida si el hijo derecho es mayor que el padre
        largest = r
      if largest != i:# solo si alguno de los hijos es mayor se realiza el intercambio de valores
        swap(arr, i, largest) 
            
       

def heapSort(arr):
   n = len(arr) 
   if n <= 1: return
   heapif(arr, n) #se crea el primer monticulo llevando el valor mayor a la primera posicion
   for i in range(n-1, 0, -1):
      swap(arr,0 , i) 
      heapif(arr, i)

   
   

if __name__ == '__main__':
   arr = [5,1,8,6,1,4,2,23,7,3,9,11,2,0,10]
   heapSort(arr)
   print('heap sorted:',arr )
