
def DFS(graph, v, visited):
    #첫번째 노드(1) 방문
    visited[v] = True   #방문 시, True 할당
    print(v, end = ' ')    #방문후 출력
    for i in graph[v]:      #이웃 노드를 순차적으로 확인하는 for문
        if not visited[i]:  
            DFS(graph, i, visited)
            

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
DFS(graph, 1, visited)