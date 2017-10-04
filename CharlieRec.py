import math
from decimal import *
dp=[]
def solv(tokens, cost, depth):
    global dp
    print "solving for ", tokens, cost, depth, 
    if tokens < cost:
        return 1.0
    if tokens >= len(dp):
        return 0.0
    print dp[tokens]
    if dp[tokens]+1.0>0.0:
        #assert tokens>cost
        print "returned", dp[tokens]
        return dp[tokens]
    if depth>5:
        return 0.0
    pw=1L
    sum=0.0
    while pw<=tokens:
        nd=depth+1
        print tokens-cost+pw,pw,nd
        x=solv(tokens-cost+pw,cost,nd)
        #assert x!=-1.0
        sum+=x/(pw*2.0)
        #if x/(pw*2.0)<-0.01 :
        #    print "added", x/(pw*2.0), tokens
        assert pw>0
        pw*=2L
    dp[tokens]=sum
    #print sum,"vs",tokens
    return dp[tokens]
def solution(cost,starting_tokens):
    #this is an approximation
    #hope it works
    ans=1.0-math.exp(-1.08*(2.0*starting_tokens)/(2**(2*cost)))
    print ans
    ans=round(ans,5)
    print ans
    global dp
    dp=[-1.0]*(4) # TODO
    basi=solv(starting_tokens,cost,1)
    print "s=",basi
    ans=1-basi
    if ans != 1.0:
        ans*=10**5
        re="0"+str("%05d"%int(ans))
    else:
        ans*=10**5
        re=str("%05d"%int(ans))
    return re

if __name__ == "__main__":
    print solution(2,2);
