def kangaroo(x1, v1, x2, v2):
    min_location=min(x1,x2)
    max_location=max(x1,x2)
    if x1>=x2:
        min_distance=v2
        max_distance=v1
    else:
        min_distance=v1
        max_distance=v2
    
    if max_distance>=min_distance:
        result='NO'
        return result
        
    while min_location<max_location:
        min_location=min_location+min_distance
        max_location=max_location+max_distance
    if min_location==max_location:
        result='YES'
    else:
        result='NO'
    return result
