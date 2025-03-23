def is_prime(number):
  if number == 1:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if (number % i == 0):
      return False
  return True

N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):
  if is_prime(numbers[i]):
    count += 1

print(count)