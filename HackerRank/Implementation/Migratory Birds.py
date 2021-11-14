def migratoryBirds(arr):
    count=[0,0,0,0,0,0]
    for i in arr:
        count[i]=count[i]+1
    return count.index(max(count))v
