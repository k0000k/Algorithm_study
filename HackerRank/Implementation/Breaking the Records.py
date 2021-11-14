def breakingRecords(scores):
    scorevalue=[0,0]
    min_score=scores[0]
    max_score=scores[0]
    for i in range(1,n):
        if scores[i]>max_score:
            scorevalue[0]=scorevalue[0]+1
            max_score=scores[i]
        elif scores[i]<min_score:
            scorevalue[1]=scorevalue[1]+1
            min_score=scores[i]
    return scorevalue
