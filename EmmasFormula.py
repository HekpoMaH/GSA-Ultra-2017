import math
def check(bottles, substances, days):
    cnt=0L
    div=2L**bottles
    if div==1L and substances!=1:
        return False
    while substances>1:
        rem=substances/div
        if substances%div != 0 :
            rem+=1L
        substances=rem
        cnt+=1L
    return cnt<=days

def solution(t):
    ans=""
    for tup in t:
        substances=tup[0]
        days=tup[1]
        l=-1L;r=63L
        while l+1L<r:
            mid=(l+r)/2L
            if check(mid,substances,days):
                r=mid
            else:
                l=mid;
        print l,r
        ans+=str(r)
        print ans
    return ans


if __name__ == "__main__":
    solution(
        [(100000,2),
        (12345,4),
        (121212,3),
        (643125,7),
        (1000000,10),
        (1,1),
        (123123,4),
        (432765,2),
        (10000,9),
        (1,10)]
    );
    #solution([(9,2)]); # 10 -> 3 -> DONE 
    check(316,100000,2)
    print "s=",solution([(1024,1)])
