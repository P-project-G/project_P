import sys
input = sys.stdin.readline

def correct(a,b): # i휘갈겨쓰기, v휘갈겨쓰기 함수
    if a==b or (a=='i' and (b=='i' or b=='j' or b=='l')) or (a=='v' and (b=='v' or b=='w')):
        return True
    else :
        return False

n,m = map(int,input().split())

result = input()
answer = input()
dp = [[0 for _ in range (m+1)] for _ in range (n+1)]

#편집거리알고리즘 사용
for i in range (1,n+1):
    dp[i][0] = i

for i in range (1,m+1):
    dp[0][i] = i

for i in range (1,n+1):
    for j in range (1,m+1):
        if correct(result[i-1],answer[j-1]):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

print(dp[n][m])


"""
간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	175	68	59	45.385%
문제
세계적인 기업 CTP(Chickens Threaten Programming)에 입사하기 위해서는 영어 받아쓰기 테스트를 통과해야 한다. 영어 받아쓰기는 채용 담당자가 불러주는 단어를 지원자가 받아쓰는 시험이다. CTP에서는 받아쓰기 채점 프로그램을 통해 지원자가 작성한 답안에 점수를 매긴다. 지원자가 작성한 답안을 몇 번이나 수정해야 정답과 같아지는지 확인하는 방법이다. 수정에는 추가, 삭제, 변환 세 가지 방법이 있다. 추가는 한 글자를 추가하는 것이고, 삭제는 한 글자를 삭제하는 것이며, 변환은 한 글자를 다른 글자로 바꾸는 것을 의미한다. 추가, 삭제, 변환은 모두 동일하게 1회의 수정으로 취급한다. 다음은 각 수정 방법의 예를 나타낸 표이다.

 	답안	정답	수정 사항	수정
추가	piza	pizzaa	z,a 추가	2회
삭제	pineapple	apple	p,i,n,e 삭제	4회
변환	johnber	johnson	b->s, e->o, r->n 으로 각각 변환	3회
종합	fishcake	taken	f->t  변환 / i,s,h,c 삭제 / n 추가	6회
받아쓰기 테스트에서의 수정 횟수는 추가, 삭제, 변환 세 가지 수정 횟수의 합이 가장 최소로 일어난 경우를 말한다. 그리고 받아쓰기 테스트 점수는 작성한 답안을 정답으로 바꿀 때 필요한 총 수정 횟수와 같다. 만약 총 세 번의 수정이 일어났다면 3점을 획득하는 것이다. 0점이 제일 좋은 점수이다.

승연이는 CTP에 입사하기 위해 영어 받아쓰기를 공부중이다. 그러던 중 기가막힌 방법을 알게 되었는데, 그것은 바로 i와 v를 휘갈겨 쓰는 것이다. 실제로 CTP의 채점 시스템은 종이에 작성한 답안을 카메라로 인식해 정답과 비교하기 때문에, 휘갈겨 쓴 글자를 잘못 인식하는 에러가 있다. 휘갈겨 쓴 i는 i, j, l 모두와 매칭된다. 예를 들어 정답이 'james'일 때 답안이 'iames'라면 수정 횟수는 0회로 채점된다.대신 답안에 작성한 j와 l은 정확하게 인식한다. 마찬가지로 휘갈겨 쓴 v는 v, w와 매칭된다. 정답이 'warren'일 때 답안이 'varren'이라면 채점 결과는 0점이다. 단, w는 정확히 인식하기 때문에, 정답이 'vaccine'일 때 답안이 'waccine'이라면 점수는 1점으로 채점된다. 다시 한 번 정리하자면 i와 v를 제외한 모든 글자는 정확히 인식한다. 미리 자신의 점수를 확인해보고싶어하는 승연이를 위해 받아쓰기 점수를 계산하는 프로그램을 만들어보자!

입력
첫 번째 줄에 승연이가 작성한 답안의 길이 n, 정답의 길이 m이 공백을 두고 차례로 주어진다.

두 번째 줄에 승연이가 작성한 답안이, 세 번째 줄에 정답이 주어진다.

승연이가 작성한 답안과 정답은 모두 영어 소문자로만 이루어진다.

출력
첫 번째 줄에 승연이의 점수를 출력한다.

제한
1 ≤ n ≤ 1,000,000
1 ≤ m ≤ 1,000,000
1 ≤ n × m ≤ 10,000,000 
---
예제 입력 1 
5 8
taken
fishcake

예제 출력 1 
6

---
예제 입력 2 
4 6
piza
pizzaa

예제 출력 2 
2

---
예제 입력 3 
9 5
pineapple
apple

예제 출력 3 
4

---
예제 입력 4 
7 7
johnber
johnson

예제 출력 4 
3

---
예제 입력 5 
7 5
village
willy

예제 출력 5 
3

---
예제 입력 6 
7 7
waccine
vaccine

예제 출력 6 
1
"""