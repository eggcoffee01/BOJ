def TSP(now, visited):
    if visited == (1 << N) - 1:
        if cities[now][0]:
            return cities[now][0]
        else:
            return int(1e9)
    
    if (now, visited) in dp:
        return dp[(now,visited)]
    
    min_cost = int(1e9)
    for next in range(1 , N):
        if visited & 1 << next or cities[now][next] == 0:
            continue
        cost = TSP(next, visited | 1 << next) + cities[now][next]
        min_cost = min(cost,min_cost)
    
    dp[(now, visited)] = min_cost
    print(dp)
    return min_cost

## 비트마스킹, dp로 바꿔야됨!
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    cities = []
    dp = {}

    for _ in range(N):
        cities.append(list(map(int, input().split())))
        
    print(TSP(0, 1))