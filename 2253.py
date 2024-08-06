if __name__ == "__main__":
    import sys
    import math
    sys.setrecursionlimit(10**6)

    INF = 100000000
    input = sys.stdin.readline
    ## N은 전체 돌의 개수, M은 못 가는 돌 개수
    n,m = map(int, input().split())
    ## stone 배열은 key값으로 점프력, value값으로는 점프 횟수를 저장한다.
    stone = [{} for _ in range(n+1)]
    stone[1][0] = 0;
    ## cantgo 배열은 가지 못하는 돌을 기억한다.
    cantgo = [0 for _ in range(n+1)]
    for _ in range(m):
        cantgo[int(input())] = 1;



    for i in range(1, n+1):
        if cantgo[i] == 1:
            continue

        for key in stone[i]:
            for j in range(key-1, key + 2):
                ## 점프력이 0보다 크고 점프했을때 n보다 같거나 작다면 실행해라!
                if(0 < j and i+j <= n and not cantgo[i+j]):
                    ## 해당 딕셔너리에 같은 점프력 키값을 가진 밸류가 있다면 비교해서 작은 것을 넣어라
                    if j in stone[i+j]:
                        if stone[i][key]+1 < stone[i+j][j]:
                            stone[i+j][j] = stone[i][key]+1
                    ## 해당 딕셔너리에 해당 점프력을 가진애가 없다면 그냥 추가해라!
                    else:
                        stone[i+j][j] = stone[i][key]+1

    min_value = INF
    for key in stone[n]:
        current_min_value = stone[n][key]
        if current_min_value < min_value:
            min_value = current_min_value

    if min_value != INF:
        print(min_value)
    else:
        print(-1)