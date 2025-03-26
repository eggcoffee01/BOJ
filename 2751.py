import sys

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

input = sys.stdin.read

data = input().split()

array = list(map(int, data[1:]))

array = divide(array)

for num in array:
  print(num)