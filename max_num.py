"""
0 또는 양의 정수가 주어졌을 때,
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
"""
def solution(numbers):
    numbers=list(map(str,numbers))
    numbers=sorted(numbers,key=lambda x: x*4,reverse=True)
    answer = "".join(numbers)
    return str(int(answer))

if __name__ == '__main__':
    #numbers=[6,10,2]
    numbers=[3,30,34,5,9]
    print(solution(numbers))