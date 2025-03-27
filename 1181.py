def strcmp(str1, str2):
  if len(str1) == len(str2):
    return str1 > str2
  else:
    return len(str1) - len(str2)

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
    if strcmp(left[left_index], right[right_index]) >= 1:
      array.append(right[right_index])
      right_index += 1
    else:
      array.append(left[left_index])
      left_index += 1
  while left_index < len(left):
    array.append(left[left_index])
    left_index += 1
  while right_index < len(right):
    array.append(right[right_index])
    right_index += 1
  return array

import sys

input = sys.stdin.read

data = input().split()

my_set = set(data[1:])  
my_list = list(my_set)
my_list = divide(my_list)
for word in my_list:
  print(word)