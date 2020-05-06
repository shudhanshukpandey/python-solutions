
input().split()
a=list(map(int,input().split()))

A=set(map(int,input().split()))
B=set(map(int,input().split()))
hap=0
for i in range(len(a)):
    if a[i] in A:
        hap=hap+1
    if a[i] in B:
        hap=hap-1

print(hap)


