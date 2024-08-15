import math

def JumpSearch(arr, target):
   n = len(arr)
   step = int(math.sqrt(n)) #para calcular el tama;o de los saltos se usa la raiz del tama;o del array
   prev = 0
   #bucle para realizar los saltos
   while arr[min(step,n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
             return -1
   #busqueda lienal a partir del prev
   while arr[prev] < target:
        prev += 1
        if prev == min(step, n): # si prev alcansa los limites se termina el proceso
             return -1
   
   #comparacion final
   if arr[prev] == target:
        return prev
   #el target no esta en el arroy
   return -1      

if __name__ == '__main__': 
      arr = [0,1, 1, 2,2, 3, 4, 5, 6, 7, 8, 9]
      result= JumpSearch(arr,3)
      print('jump Search:', result )

