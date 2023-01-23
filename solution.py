import sys
a = int(sys.argv[1])
b=1
for i in range(a):
    for j in range(a-1):
        print(" ",end="")
    print("#"*b,end="")
    print()
    a-=1
    b+=1
