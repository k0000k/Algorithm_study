def miniMaxSum(arr):
    sum=0
    for i in range(5):
        sum=sum+arr[i]
    value=[]
    for i in range(5):
        value.append(sum-arr[i])
    value.sort()
    print('%d %d'%(value[0],value[4]))
