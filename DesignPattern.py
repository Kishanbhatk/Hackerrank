'''Designer Door Mat
   The Python program to design the door mat pattern,Its a problem in Hackerrank platform'''

val = list(map(int,input().split()))
lines = val[0]
total = val[1]
su = 0
def dot(num):
    for m in range(0,num):
        print("-",end='')
def pat(num):
    for k in range(0,num):
        if k % 2 == 0:
            print(".",end='')
        else:
            print("|",end='')

for i in range(0,lines):
    if i!=((lines/2)-1) and i<((lines/2)-1):
        add = 6*i
        j = int((total - (3+add))/2)
        dot(j)
        pat(3+add)
        dot(j)
        su = su + 1
    elif i == int((lines/2)):
        j = int((total-7)/2)
        dot(j)
        for k in "WELCOME":
            print(k,end='')
        dot(j)
    else:
        add = 6*(su-1)
        j = int((total-(3+add))/2)
        dot(j)
        pat(3+add)
        dot(j)
        su = su - 1
    print()        
