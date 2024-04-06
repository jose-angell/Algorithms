# Función para determinar si existe un `target` en la lista ordenada `nums`
# o no usando un algoritmo de búsqueda binaria
def binarySearch(nums, target):
 
    # El espacio de búsqueda # es nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # Bucle # hasta que se agote el espacio de búsqueda
    while left <= right:
 
        # encuentra el valor medio en el espacio de búsqueda y
        # lo compara con el objetivo
 
        mid = (left + right) // 2
 
        # Puede ocurrir un desbordamiento de #. Usar:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2
 
        # Se encuentra el objetivo
        if target == nums[mid]:
            return mid
 
        # descartar todos los elementos en el espacio de búsqueda correcto,
        # incluido el elemento central
        elif target < nums[mid]:
            right = mid - 1
 
        # descartar todos los elementos en el espacio de búsqueda de la izquierda,
        # incluido el elemento central
        else:
            left = mid + 1
 
    # `target` no existe en la lista
    return -1
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 6
 
    index = binarySearch(nums, target)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')