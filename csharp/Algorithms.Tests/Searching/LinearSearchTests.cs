using Xunit;
using Algorithms.Core.Searhcing;

namespace Algorithms.Tests.Searching {
    public class LinaerSearchingTest {
        [Fact]
        public void Search_FindsExistingElement()
        {
            // Given
            int[] input = {1,2,5,8,9,16};
            // When
            int target = 2;
            int expected = 1;
            int result = LinearSearch.Search(input, target);
            // Then
            Assert.Equal(expected, result);
        }
        [Fact]
        public void Search_ReturnsMinusOne_WhenElementNotFound(){
            int[] input = {1,2,5,8,9,16};
            int target = 12;
            int expected = -1;
            int result = LinearSearch.Search(input, target);
            Assert.Equal(expected, result);
        }
    }
}