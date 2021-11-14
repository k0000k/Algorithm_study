def birthday(s, d, m):
    count=0
    for i in range(n-m+1):
        sum=0
        for k in range(m):
            sum=sum+s[i]
            i=i+1
        if sum==d:
            count=count+1
    return count
