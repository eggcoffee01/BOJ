def hanoi(n, start, end):
  if n == 1:
    print(start, end)
    return
  mid = 6 - (start + end)
  hanoi(n - 1, start , mid)
  print(start, end)
  hanoi(n - 1, mid, end)

N = int(input())

print(2**N - 1)
if (N <= 20):
  hanoi(N, 1, 3)