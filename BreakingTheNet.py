import sys;
def solution(n):
    MOD = 10L**9+7L
    dp = [ [0L for i in range(1,n+5)] for j in range(1,6)]
    #print len(dp), len(dp[0])
    for i in range(1,5):
        dp[i][0]=1L
    for i in range(1,5):
        for j in range(1,n+1):
            #print i,j
            dp[i][j]=0L
            if j-i>0:
                for k in range (1,i+1):
                    #print "dp["+str(i)+"]["+str(j)+"] = (dp["+str(i)+"][" +str(j)+ "] + dp[" + str(i) +"]["+str(j)+"-"+str(i)+"])%MOD"
                    dp[i][j] = (dp[i][j] + dp[k][j-i])%MOD
            if j==i:
                dp[i][j] = 1
            #print dp[i][j],
        #print '\n'
    ans=0L
    print "done"
    for i in range(1,5):
        ans = (ans + dp[i][n])%MOD
    print ans
    return ans
if __name__ == "__main__":
    solution(100000);
    

