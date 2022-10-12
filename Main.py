from typing import List

def selectionSort(array, size) -> List[int]:  
  
  for indexo in range(size-1):
    small_index = indexo
    for index in range(indexo + 1,size):
      if array[index] < array[small_index]:
        small_index = index
    array[indexo], array[small_index] = array[small_index], array[indexo]
  return array     

