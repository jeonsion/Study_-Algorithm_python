from collections import deque


def BFS(graph, start, visited):
    #큐 선언시 iterable object가 파라미터로 전달되어야한다 따라서 정수 1은 안됨 -> [1]
    queue = deque([start])
    visited[start] = True   #방문 시 True 할당

    while queue :           #큐에 남아 있을 때까지 시행
        v = queue.popleft() #큐에 맨 왼쪽 을 뺀다.
        print(v, end = ' ') #빼고 출력
        for i in graph[v]:  #해당 노드에 이웃노드들을 조사
            if not visited[i]:
                queue.append(i) #방문하지 않았다면 큐에 넣고
                visited[i] = True        #True 할당

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
BFS(graph, 1, visited)