if __name__ == '__main__':
    n = int(input())
    marks = {}
    for _ in range(n):
        name = input().split()
         
        marks[name[0]] =sum((list(map(float, name[1:]))))/3
        
    
    query=input() 
  #  print('%.2f'%(sum(marks[query])/3))
    
    print('%.2f'%(marks[query]))
