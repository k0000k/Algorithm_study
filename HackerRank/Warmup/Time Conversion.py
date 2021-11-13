def timeConversion(s):
    PMAM=s[8:10]
    if PMAM=='AM':
        if s[0:2]=='12':
            time='00'+s[2:8]
            return time
        return s[0:8]
    else:
        if s[0:2]=='12':
            time=s[0:8]
            return time
        hour=int(s[0:2])
        hour=str(hour+12)
        time=hour+s[2:8]
        return time
