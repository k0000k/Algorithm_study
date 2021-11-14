def divisibleSumPairs(n, k, ar):
    count=0
    
    for i in range(n):
        for m in range(i+1,n):
            if (ar[i]+ar[m])%k==0:
                count=count+1
    return count
