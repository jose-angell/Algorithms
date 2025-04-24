namespace Algorithms.Core.Sorting {

    public static class BubbleSort
    {
        public static int[] Sort(int[] arr){
             var result = (int[])arr.Clone();
            for (int i = 0; i < result.Length - 1; i++) {
                for (int j = 0; j < result.Length - i - 1; j++) {
                    if (result[j] > result[j + 1]) {
                        (result[j], result[j + 1]) = (result[j + 1], result[j]);
                    }
                }
            }
            return result;
        }
    }
}