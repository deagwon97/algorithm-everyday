V = 6
inf = 100000 # ����� ū ����

graph = [[0,  2,   5, 1,   inf, inf],
         [2,  0,   3, 2,   inf, inf],
         [5,  3,   0, 3,   1,   5  ],
         [1,  2,   3, 0,   1,   inf],
         [inf,inf, 1, 1,   0,   2  ],
         [inf,inf, 5, inf, 2,   0  ]]

visit = [False for i in range(V)] # node�� �湮 ���θ� Ȯ�� True/False
dis = [inf for i in range(V)] # start���� node ������ �ִ� �Ÿ��� ���

def getSmallIndex():
    # �Ÿ��� �ּ��� ������ ��ȯ
    # ������� ������Ʈ�� dis�� �������� start���� ���� ����� ����� �ε��� ã��
    min = inf
    index = 0
    for i in range(V):
        if(dis[i]<min) and (not visit[i]):
        # ������ �湮���� �ʾ����鼭 dis�� ���� ���� ���� �ε��� ã��
            min = dis[i]
            index = i
    return index

def dijkstra(start):
    # 1. start���� Ư�� �������� �Ÿ��� ������Ʈ
    for i in range(V):
        dis[i] = graph[start][i]
    visit[start] = True # start�� �湮 ó��


    # 2. 
    for i in range (V - 1): # V-1�� �ݺ� # �ڱ� �ڽŰ� ������ �ε��� ����
        current = getSmallIndex() # start���� ���尡��� ��� ��ȯ
        visit[current] = True # ��ȯ�� ���� �湮ó��
        
        # current��忡�� j���� ���� ����� �Ÿ� ��
        for j in range(V):
            if not visit[j]:
                if dis[current] + graph[current][j] < dis[j]:
                    dis[j] = dis[current] + graph[current][j]

dijkstra(0)
for i in range(V):
    print(dis[i])