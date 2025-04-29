
namespace Algorithms.Core.Searhcing {
    public static class LinearSearch {// Busqueda lineal
        public static int Search(int[] arr, int target){
            //Recorre todo el array y compara cada elemento con el valor objetivo 
            
            for(int i = 0; i < arr.Length; i++){
                if(arr[i] == target){
                    return i; //Retorna el indice si lo encuentra
                }
            }
            return -1; // en caso de no encontrar el valor objetivo devuelve -1
        }
    }
}