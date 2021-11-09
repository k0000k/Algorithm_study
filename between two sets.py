'''
우리가 찾아야 하는 수의 조건:
    (1) a의 공배수
    (2) b의 공약수
    두가지 조건을 동시에 만족하는 수들을 찾아야 함.
    따라서, 우리가 찾는 수의 범위는 a의 최댓값과 b의 최솟값 사이임.
'''

def getTotalX(a, b):
    a_ready=[]
    result=0
    min_b=min(b)
    max_a=max(a)
    for i in range(max_a,min_b+1):      #범위 안의 모든 수를 검사함.
        for m in a:                     #a의 모든 수로 나누어지는지 체크
            if i%m!=0:                  #a의 숫자중 하나라도 나누어지지 않으면 그 수는 버림
                break
        else:                           #모든 a로 나누어지는것이 확인되면 리스트에 추가
            a_ready.append(i)
                                        #여기까지 진행시, (1)조건을 만족하는 수들이 a_ready에 들어있음
    for i in a_ready:                   #이제 a_ready에 있는 수 중에서 (2)도 만족하는것들을 result에 추가
        for m in b:
            if m%i!=0:
                break
        else:
            result=result+1             #최종적으로 result에 있는 원소의 갯수를 return함.
    return result
