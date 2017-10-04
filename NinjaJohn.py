def printTable(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table) 
def solve(test_case):
    n=test_case[0]
    n+=2
    jump=test_case[1]
    d=test_case[2]
    print "kek",n,jump,d
    s=[0]*n
    dp=[0]*n
    #leftmostLarger=[[0 for x in range(n)] for y in range(n)]
    #0 1 2 3
    #  4 1 4
    #0 4 5 9
    for i in range(1,n):
        print i
        s[i]=s[i-1]+d[i-1]
        dp[i]=-1
        for j in range(i):
            if s[i]-s[j]>(i-j)*jump:
                continue
            if dp[j] == -1:
                continue
            beta=dp[j]+i-j-1
            if dp[i]==-1:
                dp[i]=beta
            elif dp[i]>beta:
                dp[i]=beta
        print i, dp[i], s[i]

    print dp
    if(dp[n-1]!=-1):
        return str(dp[n-1])
    #printTable(leftmostLarger)
def solution(tuple_of_test_cases):
    ans=""
    for tup in tuple_of_test_cases:
        print tup
        soln=solve(tup)
        if soln is not None:
            ans+=soln
    print ans
    return ans
if __name__ == "__main__":
    tuplet=(7,3,(4,3,3,3,3,3,3,2))
    print tuplet
    tupl=(tuplet,)
    tuplet=(4,3,(1,2,3,4,5))
    tupl=tupl+(tuplet,)
    tuplet=(3,1,(2,2,2,2))
    tupl=tupl+(tuplet,)
    tuplet=(3,2,(2,2,2,2))
    tupl=tupl+(tuplet,)
    tuplet=(7,3,(4,3,3,3,2,2,3,4))
    tupl=tupl+(tuplet,)
    print tupl
    solution(tupl)
#2,3,3,3,4,3,3,2
#1,2,3,4,5
