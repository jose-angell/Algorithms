def bucketSor(arr):
    #El criterio para determinar la cantidad de cubetas y la forma en la que la informacion se distribuye
    #depende del tipo de informacion a ordenar, este puede ajustar se a las necesidades de cada caso
    buckets = [[] for _ in range(10)]
    sortedArr = []
    for num in arr:
        index = num // 10
        buckets[index].append(num)
    # se ordena cada cubeta por separado y despues se agrega a la salida final
    for bucket in buckets:
        # la funcion de ordenamiento se puede ajustar a cada caso dependiendo del tipo de informacion a guardar
        sortedArr.extend(sorted(bucket))
    return sortedArr


if __name__ == "__main__":
    arr  = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(arr)
    print(bucketSor(arr))