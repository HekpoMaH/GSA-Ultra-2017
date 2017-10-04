def solution(n, m, k, v):
    # n - size
    # at least m
    # of length k
    # larger than v
    dp = [ [ [0 for i in range(2**k)] for j in range(1,m+2)] for kk in range(1,n+3)]
    print len(dp), len(dp[0]),len(dp[0][0])
    for i in range(2**k):
        dp[0][0][0]=1
    print dp
    for i in range(0,n+1):
        for j in range(0,m+1):
            for mask in range(2**k):
                for msk in range(v+1,2**k):
                    dp[i][j][msk]=1
    pass
if __name__ == "__main__":
    solution(5,3,3,5);
