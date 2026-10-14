def lCP(s1,s2):
    i=0
    while 1 < len(s1) and i < len(s2) and s1[i] == s2:
        i+= 1
    return s1[:1]