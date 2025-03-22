numbers = []

for i in range(9):
  numbers.append(int(input()))

max = numbers[0]
index = 1

for i in range(1 , 9):
  if max < numbers[i]:
    max = numbers[i]
    index = i + 1

print(max)
print(index) 