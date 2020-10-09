V = 6
inf = 100000 # 충분히 큰 숫자

graph = [[0,  2,   5, 1,   inf, inf],
         [2,  0,   3, 2,   inf, inf],
         [5,  3,   0, 3,   1,   5  ],
         [1,  2,   3, 0,   1,   inf],
         [inf,inf, 1, 1,   0,   2  ],
         [inf,inf, 5, inf, 2,   0  ]]

visit = [False for i in range(V)] # node의 방문 여부를 확인 True/False
dis = [inf for i in range(V)] # start에서 node 까지의 최단 거리를 기록

def getSmallIndex():
    # 거리가 최소인 정점을 반환
    # 현재까지 업데이트된 dis를 기준으로 start에서 가장 가까운 노드의 인덱스 찾기
    min = inf
    index = 0
    for i in range(V):
        if(dis[i]<min) and (not visit[i]):
        # 이전에 방문하지 않았으면서 dis속 가장 작은 수의 인덱스 찾기
            min = dis[i]
            index = i
    return index

def dijkstra(start):
    # 1. start에서 특정 노드까지의 거리를 업데이트
    for i in range(V):
        dis[i] = graph[start][i]
    visit[start] = True # start를 방문 처리


    # 2. 
    for i in range (V - 1): # V-1번 반복 # 자기 자신과 마지막 인덱스 제외
        current = getSmallIndex() # start에서 가장가까운 노드 반환
        visit[current] = True # 반환된 노드는 방문처리
        
        # current노드에서 j노드로 가는 경로의 거리 비교
        for j in range(V):
            if not visit[j]:
                if dis[current] + graph[current][j] < dis[j]:
                    dis[j] = dis[current] + graph[current][j]

dijkstra(0)
for i in range(V):
    print(dis[i])