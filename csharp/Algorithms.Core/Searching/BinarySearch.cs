namespace Algorithms.Core.Searching {
    public static class BinarySearch{// Busqueda binaria
        public static int Search(int[] arr, int target){
            int mid = 0; // Punto medio
            int left = 0;//extremo izquierdo del array
            int right = arr.Length;// extremo derecho del array
            while (left <= right){// el ciclo se repite hasta que el espacio de busquda se termine
                mid = left + (right - left) / 2;
                if(arr[mid] == target){// tambien se termina el ciclo si se encuentra el alor objetivo
                    return mid;
                }else if(target > arr[mid]){
                    left = mid + 1;// se desplaza el limite izquierdo hasta el punto medio mas uno 
                }else{
                    right = mid - 1;// se desplaza el limite derecho hasta el punto medio menos uno 
                }
            }
            return -1;
        }
    }
}