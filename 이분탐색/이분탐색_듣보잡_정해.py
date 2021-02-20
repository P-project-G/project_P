import sys
input = sys.stdin.readline

#def
def binarySearch(list,target,low,high):
    while low<=high:
        mid = (low+high)//2
        if list[mid] == target:
            return True
        if target > list[mid]:
            low = mid+1
        else:
            high = mid-1

    return False


#main

n,m = map(int,input().split())

#듣도못한, 보도못한 명단
dm,bm = [],[]

#듣도못한 명단
for i in range (n):
    dm.append(input().rstrip())

#보도못한 명단
for i in range (m):
    bm.append(input().rstrip())

#듣도못한 명단 정렬 : 이진탐색 위해
dm.sort()

count = 0 # 듣도보도못한 명단의 수
answer = [] # 듣도보도못한 명단
for i in bm:
    if binarySearch(dm,i,0,n-1):
        answer.append(i)

print(len(answer))
for i in sorted(answer):
    print(i)

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	24477	9902	7076	39.582%
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

 

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

예제 입력 1 
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

예제 출력 1 
2
baesangwook
ohhenrie
"""