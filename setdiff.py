# Enter your code here. Read input from STDIN. Print output to STDOUT
_,a=input(),set(map(int,input().split()))

_,b=input(),set(map(int,input().split()))

print(len(a.difference(b)))

