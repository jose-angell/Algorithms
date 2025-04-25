from sorting.bubbleSort import bubbleSort

def test_bubble_sort():
    assert bubbleSort([5, 2, 1]) == [1, 2, 5]
    assert bubbleSort([]) == []
    assert bubbleSort([1]) == [1]
    assert bubbleSort([3, 3, 2]) == [2, 3, 3]

    