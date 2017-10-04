#import pprint
import math
def sqrtt(a):
    x=a/2.0
    for i in range(15):
        xn=x-(2*(x**3)-2*a*x)/(3*(x**2+a))
        x=xn
    return x
def cmpPoints(p1,p2):
    if p1[1]<p2[1]:
        return -1
    if p1[1]>p2[1]:
        return 1
    if p1[0]<p2[0]:
        return -1
    if p1[0]>p2[0]:
        return 1
    return 0

def distPoints(p1,p2):
    return ((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))**0.5

counted=set()
helperDict={}
def fromLine(point1,point2,m,b,bl,sett):
    listt=list(sett)
    distBetweenLines=-1.0
    if m==float("inf"):
       distBetweenLines=abs(b-bl)
    else:
        hel1=(b*m-bl*m)/(m*m+1.0)
        hel2=(bl-b)/(m*m+1.0)
        distBetweenLines=hel1*hel1+hel2*hel2
        distBetweenLines=math.sqrt(distBetweenLines)
    ar=0.0
    distP=distPoints(point1,point2)
    for i in range(len(listt)):
        #smallSet=frozenset([point1,point2,listt[i],listt[j]])
        #if smallSet in counted:
        #    #print distPoints(listt[i],listt[j]),distP, helperDict[(distP,distPline)]
        #    continue
        #counted.add(smallSet)
        ##print "added", smallSet
        ##print "p1=",point1,"p2=",point2,"p3=",listt[i],"p4=",listt[j]
        #distPLine=distPoints(listt[i],listt[j])
        ar+=1
        #if(distP==distPLine):
        #    ar+=(distPLine+distP)*0.5
    return ar*distBetweenLines*0.5


def gcd(a,b):
    return a if b==0L else gcd(b,a%b)
def solution(tuple_of_points):
    lines={}
    # dict is like m (Fraction) b (offset,Fraction) -> dict[m][b]
    for i in range(len(tuple_of_points)):
        for j in range(i+1,len(tuple_of_points)):
            p1=tuple_of_points[i]
            p2=tuple_of_points[j]
            if(p1==p2):
                continue
            ym=p2[1]-p1[1]
            xm=p2[0]-p1[0]
            #print ym,xm
            #m=Fraction(long(ym),long(xm))
            if(xm != 0):
                m=float(ym)/float(xm)
                b=(p1[1]-m*p1[0])
            else:
                m=float("inf")
                b=p1[0]
            #b=Fraction(long(p1[1]),1L)-m*Fraction(long(p1[0]),1L)
            #print p1,p2,m,b
            #if m == Fraction(-1L,0L):
            #    m=abs(m)
            #if m == Fraction(1L,0L):
            #    b=Fraction(long(p1[0]),1L)
            if lines.get(m) == None:
                #print "NO M"
                lines[m]={}
            if lines[m].get(b) == None:
                #print "NO B"
                lines[m][b]=set()
            lines[m][b].add(p1)
            lines[m][b].add(p2)
            #pprint.pprint(lines)
            #print '\n'
    area=0.0
    mx=0;
    for i in range(len(tuple_of_points)):
        for j in range(i+1,len(tuple_of_points)):
            p1=tuple_of_points[i]
            p2=tuple_of_points[j]
            if(p1==p2):
                continue
            ym=p2[1]-p1[1]
            xm=p2[0]-p1[0]
            #print ym,xm
            #m=Fraction(long(ym),long(xm))
            if(xm != 0):
                m=float(ym)/float(xm)
                b=(p1[1]-m*p1[0])
            else:
                m=float("inf")
                b=p1[0]
            mx=max(mx,len(lines[m]))
            for bl in lines[m]:
                if b>=bl:
                    continue
                #area+=fromLine(p1,p2,m,b,bl,lines[m][bl])
            #print len(lines[m])
    #print mx
    #print area
    #pprint.pprint(counted)
    #pprint.pprint(helperDict)
    re=""
    re+=str(int(area))
    area-=int(area)
    area*=10**3
    re+=str("%03d"%int(area))
    return re;
if __name__ == "__main__":
    points=[]
    with open('test_trap.txt') as f:
        points = [tuple(map(int, i.split(' '))) for i in f]
    print solution(points)
    print solution((
        (1,1),
        (2,2),
        (3,5),
        (4,6),
        (19,3),
        (12,100)))

