a=int(input("Ыывывфыфы:"))
f=10
v=1

while a>0:
    b = a%f
    c= b//v
    v=v*10
    f=f*10
    if (((c/2)*10)%10) != 0:
        print("True")
        break
    if c == 0:
        break

if (((c/2)*10)%10) ==0:
    print("false")






