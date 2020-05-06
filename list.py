if __name__ == '__main__':
    a=[]
    N = int(input())
    for i in range(N):
        task=input().split()
        value=list(map(int,task[1:]))
        if task[0]=='insert':
            a.insert(value[0],value[1])
        if task[0]=='remove':
            a.remove(value[0])
        if task[0]=='append':
            a.append(value[0])
        if task[0]=='pop':
            a.pop()
        if task[0]=='reverse':
            a.reverse()
        if task[0]=='sort':
            a.sort()
        if task[0]=='print':
            print(a)

