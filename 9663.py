N = int(input())
flag_a = [0 for _ in range(N)]
flag_b = [0 for _ in range(2 * N - 1)]
flag_c = [0 for _ in range(2 * N - 1)]

def NQueen(i):
  if i is N:
    return 1
  count = 0
  for j in range(N):
    if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j]:
      flag_a[j] = flag_b[i + j] = flag_c[i - j] = 1
      count += NQueen(i + 1)
      flag_a[j] = flag_b[i + j] = flag_c[i - j] = 0
  return count

ans = NQueen(0)
print(ans)