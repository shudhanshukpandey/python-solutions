# Enter your code here. Read input from STDIN. Print output to STDOUT
def cal():
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print('Error Code:', e)
    

for i in range(int(input())):
    cal()
    

