

def countingSort(arr,expl):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)#ahora solo se cuenta del 0 a 9 
    """
    arr[i] = 634, exp = 1
    index = 634 // 1 => 634 % 10 => 4
    arr[i] = 634, exp = 10
    index = 634 // 10 => 63 % 10 => 3
    arr[i] = 634, exp = 100
    index = 634 // 100 => 6 % 10 => 6
    """
    for i in range(n):
        index = arr[i] // expl #extrae el digingo segun el exponente que se este trabajando (unidades, decenas, centenas, etc...)
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i- 1]

    """ i = n - 1
    while i >= 0:
        index = arr[i] // expl
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    """
    for i in range(n-1,-1, -1):
        index = (arr[i] // expl) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for j in range(n):
        arr[j] = output[j]




def radixSort(arr):
    maxl = max(arr)
    expl = 1
    while maxl / expl >= 1:
        countingSort(arr,expl)
        expl *= 10


if __name__ == '__main__':
    arr = [34,634,75,13,7,98,7]
    radixSort(arr)
    print('Radix sort: ', arr)