if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
  
    arr=set(arr)
    arr=list(arr)
    arr.sort()
    print(arr[len(arr)-2])
