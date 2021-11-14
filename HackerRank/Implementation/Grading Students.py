def gradingStudents(grades):
    aftergrade=[]
    for i in grades:
        if i<=37:
            aftergrade.append(i)
        elif i%5==0:
            aftergrade.append(i)
        elif (i+1)%5==0:
            aftergrade.append(i+1)
        elif (i+2)%5==0:
            aftergrade.append(i+2)
        else:
            aftergrade.append(i)
    return aftergrade
