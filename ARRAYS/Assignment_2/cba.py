def solution(s): 
    x=[]
    c=''
    for i in s:
        if i not in c :
            c+=i
        else:
            x.append(c)
            c='' 
            c+=i
    x.append(c)
    print(tuple(x))
    print(len(x))


solution('cycle')