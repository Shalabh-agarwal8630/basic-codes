a='abcd'
if len(a)%2==0:
    s1=' '
    p=0
    for i in range(len(a)):
        s1=s1+a[p:p+2][: : -1]
        p=p+2
print(s1)        
