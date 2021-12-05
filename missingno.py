a=[2,4,8,12,16]
b=a[1]-a[0]
for i in range(a[0],a[-1],b):
    if i not in a:
        print(i)
