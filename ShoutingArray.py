def solution(n):
    n=long(n)
    return long(n*(n-1)*4L)+long(n*(n-1)*(n-2)*(n-3));
if __name__ == "__main__":
    print solution(1)
    print solution(2) # 1,1,1,(2,3) (x8) 
    #2,2,2,(1,3) (x8)
    #3,3,3,(1,2) (x8)
