# I got 99 problems...
# Please write your code inside the function stub below.

def solution(tuple_of_integers):
    MOD=10**9+7
    #print "MOD is ",MOD
    cntM1=[0L]*len(tuple_of_integers)
    for i,x in enumerate(tuple_of_integers):
        cntM1[i]=cntM1[i-1]
        if x == -1:
            cntM1[i]+=1L
    dp=[0L]*(len(tuple_of_integers)+1)
    dp[len(tuple_of_integers)]=1L
    #print len(dp)
    for i in range(len(tuple_of_integers)-1,-1,-1):
        x=tuple_of_integers[i]
        #print "x=",x
        if x==-1:
            #print len(tuple_of_integers)-i
            for sz in range(0,len(tuple_of_integers)-i):
                fromM1=(cntM1[i+sz]-cntM1[i])
                #print " ",fromM1
                prod=1L
                for p in range(0,fromM1):
                    prod=(prod*1001L)%MOD
                #print " i=",i,"sz=",sz,"i+sz+1=",i+sz+1,"dp[i]=",dp[i],"dp[i+sz+1]=", dp[i+sz+1], prod,
                dp[i]=(dp[i]+(dp[i+sz+1]*prod)%MOD)%MOD
                #print "dp[i] after= ",dp[i]
        else:
            if x+i>=len(tuple_of_integers):
                dp[i]=0L
            else:
                fromM1=(cntM1[i+x]-cntM1[i])
                prod=1L
                for p in range(0,fromM1):
                    prod=(prod*1001L)%MOD
                dp[i]=(dp[x+i+1]*prod)%MOD
        #print i,x,dp[i]
    return dp[0]
    
if __name__ == "__main__":
    print solution((
        -1,
        2,
        3,
        -1,
        4,
        5,
        -1,
        6,
        7,
        -1))
    print solution((
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1))
    print solution((
        -1,
        -1,
        -1))
    #2, 1001, 1001 = 1001^2
    #1, 1001, 0 = 1001
    #0, 1, 1001 = 1001
    #0, 0, 0 = 
