namespace Algorithms.Core.Searching {
    public static class BinarySearch{
        public static int Search(int[] arr, int target){
            int mid = 0;
            int left = 0;
            int right = arr.Length;
            while (left <= right){
                mid = left + (right - left) / 2;
                if(arr[mid] == target){
                    return mid;
                }else if(target > arr[mid]){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            }
            return -1;
        }
    }
}