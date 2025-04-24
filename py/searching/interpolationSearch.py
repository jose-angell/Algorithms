def interpolationSearch(A, target):
   low, high = 0, len(A) - 1 # establece los puntos conocidos
#continuea el ciclo hasta que se agote el espacion de busqueda 
   while A[high] != A[low] and target >= A[low] and target <= A[high]:
      #formula de interpolacion 
      mid = low + ((target - A[low]) * (high - low))// (A[high] - A[low])
      if A[mid] == target:
         return mid
      elif A[mid] < target:
         low = mid + 1
      else:
         high = mid - 1
   return -1


if __name__ == '__main__':
   arr = [1,2,3,4,5,6,7,8,9]
   index = interpolationSearch(arr,4)
   print('interpolation Search:', index )
