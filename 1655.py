def mid_value(temp):
    heapq.heappush(min_heap, -temp)
    
    if (len(min_heap)+len(max_heap)) % 2 == 0:
        data = -heapq.heappop(min_heap)    
        heapq.heappush(max_heap, data)
    else:
        if len(min_heap) > 0 and  len(max_heap) > 0:
            if -min_heap[0] > max_heap[0]:
                data1 = -heapq.heappop(min_heap)
                data2 = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, data1)
                heapq.heappush(min_heap, data2)

if __name__ == "__main__":
    import sys
    import heapq
    sys.setrecursionlimit(10**6)

    input = sys.stdin.readline

    ##heapq는 최소힙으로 구현되어 있어 최대힙은 넣고 뺼때 인자에다가 -연산을 해줘야 함.
    min_heap = []
    max_heap = []
    n = int(input())
    for _ in range(n):
        temp = int(input())
        mid_value(temp)
        print(-min_heap[0])