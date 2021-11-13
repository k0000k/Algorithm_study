def plusMinus(arr):
    value=[0,0,0]
    for i in arr:
        if i>0:
            value[0]=value[0]+1
        elif i<0:
            value[1]=value[1]+1
        else:
            value[2]=value[2]+1
    print('%.6f'%(value[0]/n))
    print('%.6f'%(value[1]/n))
    print('%.6f'%(value[2]/n))
