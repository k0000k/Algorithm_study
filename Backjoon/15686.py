# 백준 15686번 치킨배달

from itertools import combinations

n,m=input().split()

n=int(n)
m=int(m)

houses=[[0,0]]
chickens=[[0,0]]

distances=[]
mins=[]

# 인덱스를 1부터 사용하기 위해 0을 삽입
dosi = [[0 for k in range(n+1)]]

for i in range(n):
    dosi.append([0])

# 도시 정보 입력받기
for i in range(1,n+1):
    temp=map(int, input().split())
    dosi[i].extend(temp)

# 치킨집과 집들의 좌표 따로 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        if (dosi[i][j]==1):
            houses.append([i,j])
            
        elif (dosi[i][j]==2):
            chickens.append([i,j])

# m개의 치킨집을 뽑는 모든 경우의 수 생성
numbers=list(range(1,len(chickens)))

# 각각의 집들에 대해 모든 치킨집과의 거리를 계산하여 저장
for i in houses:
    temp=[]
    for j in chickens:
        distance=abs(j[0]-i[0])+abs(j[1]-i[1])
        temp.append(distance)
    distances.append(temp)

# 도시의 인덱스가 1부터 시작하므로,
# distances의 0번 인덱스들의 값은 필요없는 값이 들어감
# 이를 0으로 초기화
distances[0]=[0 for k in range(len(chickens))]
for i in range(len(houses)):
    distances[i][0]=0

# 현재 치킨집의 갯수 = 최대 치킨집의 갯수
# 즉, 하나도 폐업하지 않아도 되는 경우
if(len(chickens)-1==m):
    chick_sum=0
    for i in distances:
        chick_sum += min(i[1:])
    print(chick_sum)

# 그 외 일반적인 경우
else:
    indexs=list(combinations(numbers, m))

    # 치킨집 m개를 뽑는 모든 경우의 수를 불러옴
    for i in indexs:
        after_distances=[]
        chick_sum=0
        for k in distances:
            temp=[]
            # 뽑힌 m개의 치킨집에 해당하는 집-치킨집 거리 정보만 따로 저장
            for j in i:
                temp.append(k[j])
            after_distances.append(temp)

        # m개의 치킨집만 남은 상태
        # 치킨거리 계산
        for t in after_distances:
            chick_sum += min(t)
        mins.append(chick_sum)

    # 모든 경우의 수 중에서 최소의 치킨거리 출력
    print(min(mins))
            
