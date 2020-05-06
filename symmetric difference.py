input()
m=set(map(int,input().split()))
input()
n=set(map(int,input().split()))

fin=[]
 
a=m.union(n)
b=m.intersection(n)

a=list(a-b)
a.sort()


for i in a:
    print(i)
