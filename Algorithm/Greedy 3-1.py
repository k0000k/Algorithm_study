#89p 그리디 예제 3-1 거스름돈

N = int(input())

count_500 = int(N/500)
N = N-count_500*500

count_100 = int(N/100)
N = N-count_100*100

count_50 = int(N/50)
N = N-count_50*50

count_10 = int(N/10)
N = N-count_10*10

coin = count_500 + count_100 + count_50 + count_10

print(coin)


#아래는 예시답안
#리스트와 for문 이용하기
#나머지, 몫 연산자 쓰기! 알고리즘이랑 파이썬 넘 오랜만에 만져서...

'''
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin
  
 print(count)
 '''
 
