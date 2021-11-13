def diagonalDifference(arr):
    sum1=0
    sum2=0
    for i in range(n):
        sum1=sum1+arr[i][i]
    for i in range(n):
        arr[i].reverse()
    for i in range(n):
        sum2=sum2+arr[i][i]
    dif=abs(sum1-sum2)
    return dif
