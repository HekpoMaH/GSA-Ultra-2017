# Please write your code inside the function stub below.

#n - with e.g. n=5
#^_*_*_*_*_^
#0 1 2 3 4 5
#m - nails hit
#d (m sized tuple) - nail positions
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def solution(n, m, d):
    nailList=[]
    nailList.append(0L)
    nailList.extend(sorted(d))
    nailList.append(long(n));
    currStrength=1L
    for i in range(1,len(nailList)):
        currStrength*=nailList[i]-nailList[i-1]
    #0 1 2 4
    #0 1 2 5
    mxStrength=currStrength
    for i in range(1,len(nailList)-1):
        space=nailList[i+1]-nailList[i-1]
        if space/2>nailList[i]-nailList[i-1]:
            newStrength=currStrength/( (nailList[i+1]-nailList[i]) * (nailList[i]-nailList[i-1]) )
            newPos=nailList[i-1]+space/2
            newStrength*=(nailList[i+1]-newPos)*(newPos-nailList[i-1])
            mxStrength=max(mxStrength,newStrength)
    div=gcd(mxStrength,currStrength)
    print div,mxStrength,currStrength
    print str(mxStrength/div)+str(currStrength/div)
    return str(mxStrength/div)+str(currStrength/div)

if __name__ == "__main__":
    with open('test_builder.txt') as f:
        n,m = [int(x) for x in next(f).split()]
        nails = []
        for line in f: # read rest of lines
            nails.extend([long(x) for x in line.split()])
    print n,m
    #solution(n,m,tuple(nails))
    solution(4,2,(1,2))
