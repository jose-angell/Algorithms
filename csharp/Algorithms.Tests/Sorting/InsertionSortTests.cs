using Xunit;
using Algorithms.Core.Sorting;

namespace Algorithms.Tests.Sorting;

public class InsertionSortTests
{
    [Fact]
    public void Sort_OrdersArrayCorrectly()
    {
        int[] input = {5,2,8,1};
        int[] expected = {1,2,5,8};
        var result = InsertionSort.Sort(input);
        Assert.Equal(expected, result);
    }
}  
