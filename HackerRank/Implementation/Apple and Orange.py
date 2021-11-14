def countApplesAndOranges(s, t, a, b, apples, oranges):
    countapple=0
    countorange=0
    
    for i in apples:
        location=i+a
        if s<=location<=t:
            countapple=countapple+1
            
    for i in oranges:
        location=i+b
        if s<=location<=t:
            countorange=countorange+1
    print(countapple)
    print(countorange)
    
