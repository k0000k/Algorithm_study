def compareTriplets(a, b):
    score=[0,0]
    for i in range(3):
        if a[i]>b[i]:
            score[0]=score[0]+1
        elif a[i]<b[i]:
            score[1]=score[1]+1
    return score
