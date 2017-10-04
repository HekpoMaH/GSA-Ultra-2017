import math
def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")
def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def solution(cost,starting_tokens):
    #this is an approximation
    #hope it works
    sz=starting_tokens
    A=[[0 for j in range(2*sz+2)] for i in range(2*sz+1)]
    for i in range(2*sz+1):
        if i<cost:
            A[i][i]=1.0
            A[i][2*sz+1]=1.0
            continue
        pw=1
        benefit=i-cost+pw
        coef=0.5
        A[i][i]=1.0
        A[i][2*sz+1]=0.0
        while benefit<=2*sz:
            A[i][benefit]-=coef
            coef/=2.0
            pw*=2
            benefit=i-cost+pw
    #pprint(A)

    print "G=",gauss(A)[sz]

        
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
    print solution(10,100);
    A = [[2.0,3.0,13.8],[4.0,8.0,17.5]]
    print gauss(A)
    print 2*6.8416666666+3*(-1.233333333333)
