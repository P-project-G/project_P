"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.

따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
"""
def BFS(node,visited,n,computers):
    cnt=0
    bfs=[]
    while True:
        if 0 not in visited:
            break
        node=visited.index(0)
        bfs.append(node)
        visited[node]=1
        while bfs:
            node=bfs.pop(0)
            visited[node]=1

            for i in range (n):
                if visited[i]==0 and computers[node][i]==1:
                    visited[i]=1
                    bfs.append(i)
        cnt+=1
    return cnt

def solution(n, computers):
    visited = [0] * n
    answer=BFS(0,visited,n,computers)
    return answer

if __name__ == '__main__':
    n=4
#    computers=[[1,1,0],[1,1,0],[0,0,1]]
    computers=[[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
    print(solution(n,computers))