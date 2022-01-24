#93p 그리디 실전 문제 큰수의 법칙

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
result = 0

num.sort()

'''
사용되는 숫자는 가장 큰 수와 그 다음으로 큰 수 두 개 뿐이다.
이걸 눈치 못채서 헤매다가 예시 답안 보고 공부했다...
앞 뒤 숫자가 같은 경우와 다른 경우를 구분할 필요가 없는거였다.
가장 큰 수를 k번 더하고, 두번째 큰 수를 한번 더하는 과정을 m번 반복하면 된다.
'''
first = num[n-1]
second = num[n-2]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
