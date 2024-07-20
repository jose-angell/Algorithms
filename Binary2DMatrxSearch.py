def Binary2DMatrxSearch(matrix, target):
   rows, cols = len(matrix), len(matrix[0])
   low, hight = 0, rows * cols - 1    
   while low<= hight:
      mid = (low + hight) // 2
      row, col = divmod(mid, cols)
      mid_val = matrix[row][col]
      if mid_val == target:
         return row, col
      elif mid_val < target:
         low = mid + 1
      else:
         hight = mid - 1
   return None

if __name__ == '__main__':
      matrix = [
      [1, 3, 5],
      [7, 9, 11],
      [13, 15, 17]]
      result= Binary2DMatrxSearch(matrix,3)
      print('2d binary Search:', result )



