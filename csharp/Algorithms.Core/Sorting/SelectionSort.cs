namespace Algorithms.Core.Sorting {
    public static class SelectionSort {
        public static int[] Sort(int[] arr ){
            int n = arr.Length;
            for(int i = 0; i < n -1; i++){
                int min_index = i; // se toma el elemento actual como e minimo
                for(int j = i + 1; j < n ; j++){
                    if(arr[j] < arr[min_index]){ // busca el valor minimo
                        min_index = j;
                    }
                }
                int temp = arr[i];// intercambia valores entre la posicion actual y el valor minimo
                arr[i] = arr[min_index];
                arr[min_index] = temp;
            }
            return arr;
        }
    }
}