import math
def solution(cost,starting_tokens):
    #this is an approximation
    #hope it works
    ans=1.0-math.pow(2.0,-1.54*(2.0*starting_tokens)/(2**(2*cost)))
    print 1.0-ans
    ans=round(ans,5)
    print ans
    if ans != 1.0:
        ans*=10**5
        re="0"+str("%05d"%int(ans))
    else:
        ans*=10**5
        re=str("%05d"%int(ans))
    return re

if __name__ == "__main__":
    print solution(6,10000);
