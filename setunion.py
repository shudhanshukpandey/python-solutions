# Enter your code here. Read input from STDIN. Print output to STDOUT
int(input())
e=list(map(int,input().split()))
int(input())
f=list(map(int,input().split()))

e.extend(f)
print(len(set(e)))

