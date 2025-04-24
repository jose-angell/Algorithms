# Implementación recursivo del algoritmo de búsqueda binaria para devolver
# la posición de `target` en el subarray nums[left…right]
def binarySearch(nums, left, right, target):
 
    # Condición base (el espacio de búsqueda está agotado)
    if left > right:
        return -1
 
    # encuentra el valor medio en el espacio de búsqueda y
    # lo compara con el objetivo
 
    mid = (left + right) // 2
 
    # Puede ocurrir un desbordamiento de #. Usar a continuación
    # mid = left + (right - left) / 2
 
    # Condición base (se encuentra un objetivo)
    if target == nums[mid]:
        return mid
 
    # descartar todos los elementos en el espacio de búsqueda correcto,
    # incluido el elemento central
    elif target < nums[mid]:
        return binarySearch(nums, left, mid - 1, target)
 
    # descartar todos los elementos en el espacio de búsqueda de la izquierda,
    # incluido el elemento central
    else:
        return binarySearch(nums, mid + 1, right, target)
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 5
 
    (left, right) = (0, len(nums) - 1)
    index = binarySearch(nums, left, right, target)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')