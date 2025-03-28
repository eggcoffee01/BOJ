def divide(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  left = divide(array[:mid])
  right = divide(array[mid:])
  return conquer(left, right) 
  
def conquer(left, right):
  array = []
  left_index, right_index = 0, 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      array.append(left[left_index])
      left_index += 1
    else:
      array.append(right[right_index])
      right_index += 1
  while left_index < len(left):
    array.append(left[left_index])
    left_index += 1
  while right_index < len(right):
    array.append(right[right_index])
    right_index += 1
  return array

def ft_print(array, i, j):
  for k in range(len(array)):
    if k != i and k != j:
      print(array[k])

def solve(array, sum):
  for i in range(len(array)):
    sum -= array[i]
    for j in range(len(array)):
      if i is not j:
        if (sum - array[j] == 100):
          ft_print(array, i, j)
          return
    sum += array[i]

import sys

input = sys.stdin.read
data = input().split()
array = list(map(int, data))
array = divide(array)
solve(array, sum(array))