'''Designer Door Mat
   The Python program to design the door mat pattern,Its a problem in Hackerrank platform'''

val = list(map(int,input().split()))
lines = val[0]
total = val[1]
su = 0
for i in range(0,lines):
    if i!=((lines/2)-1) and i<((lines/2)-1):
        add = 6*i
        j = int((total - (3+add))/2)
        for m in range(0,j):
            print("-",end='')
        for k in range(0,3+add):
            if (k -1 ) % 3 == 0:
                print("|",end='')
            else:
                print(".",end='')
        for m in range(0,j):
            print("-",end='')
        su = su + 1
    elif i == int((lines/2)):
        j = int((total-7)/2)
        for m in range(0,j):
            print("-",end='')
        for k in "WELCOME":
            print(k,end='')
        for m in range(0,j):
            print("-",end='')
    else:
        add = 6*(su-1)
        j = int((total-(3+add))/2)
        for m in range(0,j):
            print("-",end='')
        for k in range(0,3+add):
            if (k -1) % 3 ==0:
                print("|",end='')
            else:
                print(".",end='')
        for m in range(0,j):
            print("-",end='')
        su = su - 1
    print()        
