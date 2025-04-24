
def countingSort(arr):
   #De la lista se obtinen el valor maximo y minimo para tener el rango de valores que se 
   #encuentran en la lista
   maxNum = max(arr) + 1  
   minNum = min(arr) 
   output = [0 for i in range(len(arr))] #se crea una lista de 0 del mismo tamaño que la lista original
   count = [0 for i in range(minNum,maxNum)] #esta lista almacenara el conteo de las repetisiones de cada elemento dentro del rango del minimo valor y maximo
   aux = [i for i in range(minNum,maxNum)] #esta lista me permite conextar la lista count con arr 
   #la lista aux contiene todos los numeros entre minNum y maxNum

   #cuenta la catidad de veces que un numero se repite y lo almaciena en la lista count
   #cada elemento dentro de arr funciona como el indice dentro de aux, y al conocer el indice en aux
   #puedo saber la posicion en count y sumar a la posicion correspondiente
   for i in arr:
      count[aux.index(i)] += 1
   
   print(count)
   #se crea una suma acumulativa empesando en el segundo elemento hasta el ultimo
   #el valor actual es igual a la suma del valor actual mas el anterior
   for i in range(1, len(count)):
      count[i] += count[i - 1]

   print(count)
   #para guardar los valores de arr en output (la salida) 
   #cada elemento de arr se toma como el indice utilizado para conocer el valor de el contador de ese valor
   #a ese valor se le resta uno y esa es la posicion en output
   #despues se actualiza el valor del contador para ese elemento en -1
   for i in arr:
      output[count[aux.index(i)] - 1] = i
      count[aux.index(i)] -= 1
   
   return output

if __name__ == '__main__':
   arr = [25,21,23,26,24,22,27,23,29]
   sortArr = countingSort(arr)
   print('counting sort:',sortArr )
