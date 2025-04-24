using Xunit;
using Algorithms.Core.Sorting;

namespace Algorithms.Tests.Sorting;

public class BubbleSortTests
{
    [Fact]
    public void Sort_OrdersArrayCorrectly()
    {
        int[] input = {5,2,8,1};
        int[] expected = {1,2,5,8};
        var result = BubbleSort.Sort(input);
        Assert.Equal(expected, result);
    }
}
