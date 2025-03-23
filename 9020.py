def is_prime(number):
  if number == 1:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if (number % i == 0):
      return False
  return True

T = int(input())

for i in range(T):
  number = int(input())
  for j in range(int(number / 2), 0, -1):
    if (is_prime(j) and is_prime(number - j)):
      print(j, number - j)
      break