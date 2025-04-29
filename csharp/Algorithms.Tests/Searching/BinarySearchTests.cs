using Xunit;
using Algorithms.Core.Searching;

namespace Algorithms.Tests.Searching {
    public class SearchingTest {
        [Fact]
        public void search_BinaryTest_success()
        {
            // Given
            int[] input = {1,2,5,8,9,16};
            // When
            int target = 2;
            int expected = 1;
            int result = BinarySearch.Search(input, target);
            // Then
            Assert.Equal(expected, result);
        }
        [Fact]
        public void search_BinaryTest_dontFind(){
            int[] input = {1,2,5,8,9,16};
            int target = 12;
            int expected = -1;
            int result = BinarySearch.Search(input, target);
            Assert.Equal(expected, result);
        }
    }
}