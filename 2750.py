N = int(input())

arr = []

for _ in range(N):
  arr.append(int(input()))

for i in range(N - 1):
  for j in range(N - 1):
    if arr[j] > arr[j + 1]:
      temp = arr[j]
      arr[j] = arr[j + 1]
      arr[j + 1] = temp

for i in range(N):
  print(arr[i])