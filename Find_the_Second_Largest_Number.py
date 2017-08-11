if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())    
    max_sec=-999
    arr=list(arr)
    arr.sort()
    while n!=0:
        if max_sec==-999:
            max_sec=arr.pop(-1)
        elif arr[-1]<max_sec:
            print(arr[-1]) 
            break
        else:
            max_sec=arr.pop(-1) 
        n-=1
