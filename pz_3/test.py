a=1
b=5
c=7
print("первое:",a+b,";второе:",a+c,";третье:",c+b)
if a>b>c:
    print(a+b)
elif a>c>b:
    print(a+c)
elif b>a>c:
    print(b+a)
elif b>c>a:
    print(b+c)
elif c>a>b:
    print(a+c)
elif c>b>a:
    print(b+c)
