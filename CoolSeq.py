def solution(n):
    currOdd=1
    totalWays=1
    largestSeq=0
    while currOdd<=n:
        currPower=1
        cnt=0
        while currOdd*(currPower)<=n:
            currPower*=2
            cnt+=1
        print currOdd, currPower, currOdd*(currPower)
        currOdd+=2
        
        if cnt%2==0:
            totalWays*=(cnt/2)+1
        largestSeq+=(cnt+1)/2
        print "added",(cnt+1)/2
    print "ans=",largestSeq,"and",totalWays
    return str(largestSeq)+str(totalWays)


if __name__ == "__main__":
    solution(36);

#1,2,4,8,16,32
