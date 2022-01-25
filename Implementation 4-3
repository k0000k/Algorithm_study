#113p 구현 예제 시각

#상하좌우 예제에서 배운 리스트를 이용하는 방법을 사용하려고 노력했다..
#여전히 반복이 많아서 예시 답안을 보고 공부해야 한다.

alphabet = ['a','b','c','d','e','f','g','h']
count = 0
move = [1, -1]

location = input()

for i in move:
    for j in move:
        x = alphabet.index(location[0]) + 1
        y = int(location[1])
        x = x + 2 * i
        y = y + j

        if 1<=x<=8 and 1<=y<=8:
            count +=1

for i in move:
    for j in move:
        x = alphabet.index(location[0]) + 1
        y = int(location[1])
        y = y + 2 * i
        x = x + j

        if 1<=x<=8 and 1<=y<=8:
            count +=1
print(count)
