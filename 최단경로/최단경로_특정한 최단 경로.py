"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	24165	6172	4015	24.006%

문제
방향성이 없는 그래프가 주어진다.
세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dp = [inf] * (n + 1)
    dp[start] = 0
    queue = deque()
    queue.append( (start,0) )
    while queue:
        vertex,w = queue.popleft()
        for vt,wei in s[vertex]:
            n_wei = wei + w

            if n_wei < dp[vt]:
                dp[vt] = n_wei
                queue.append( (vt,n_wei) )
    return dp
n,e = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range (e) ]
s = [ [] for _ in range (n+1) ]
inf = sys.maxsize

for v,vv,weight in graph:
    s[v].append((vv,weight))
    s[vv].append((v,weight))


v1,v2 = map(int,input().split())
v=bfs(1)
vone=bfs(v1)
vtwo=bfs(v2)


print(v)
print(vone)
print(vtwo)
answer = min( v[v1] + vone[v2] + vtwo[n], v[v2] + vtwo[v1] + vone[n] )
print(answer if answer<inf else -1)
