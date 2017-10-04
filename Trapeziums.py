#import pprint
import math
class Fraction:
    x=None
    y=None
    def __init__(self,x,y):
        div=gcd(x,y)
        self.x=x/div
        self.y=y/div
    #def __str__(self):
    #    return str(self.x)+'/'+str(self.y)
    def __repr__(self):
        return Fraction.__str__(self)
    def __add__(self,other):
        nwx=self.x*other.y+other.x*self.y
        nwy=self.y*other.y
        return Fraction(nwx,nwy)
    def __neg__(self):
        return Fraction(-self.x,self.y)
    def __sub__(self,other):
        return Fraction.__add__(self,-other)
    def __mul__(self,other):
        nwx=self.x*other.x
        nwy=self.y*other.y
        return Fraction(nwx,nwy)
    def __invert__(self):
        return Fraction(self.y,self.x)
    def __div__(self,other):
        return Fraction.__mul__(self,~other)
    def __lt__(self,other):
        f1=self.x*other.y
        f2=self.y*other.x
        return f1<f2
    def __le__(self,other):
        f1=self.x*other.y
        f2=self.y*other.x
        return f1<=f2
    def __ge__(self,other):
        f1=self.x*other.y
        f2=self.y*other.x
        return f1>=f2
    def __gt__(self,other):
        f1=self.x*other.y
        f2=self.y*other.x
        return f1>f2
    def __eq__(self,other):
        f1=self.x*other.y
        f2=self.y*other.x
        return f1==f2
    def __hash__(self):
        return hash((self.x,self.y))
    def __abs__(self):
        return Fraction(abs(self.x),self.y)
    def toFloat(self):
        return float(self.x)/self.y

# Ascending y, then ascending x
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
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def FromLines(line1,line2,set1,set2):
    distBetweenLines=-1.0
    m=line1[0]
    b1=line1[1]
    b2=line2[1]
    if m==Fraction(1,0):
       distBetweenLines=abs((b1-b2).toFloat())
    else:
        hel1=(b1*m-b2*m)/(m*m+Fraction(1,1))
        hel2=(b2-b1)/(m*m+Fraction(1,1))
        distBetweenLines=hel1*hel1+hel2*hel2
        distBetweenLines=math.sqrt(distBetweenLines.toFloat())
    list1=sorted(set1,cmpPoints)
    list2=sorted(set2,cmpPoints)
    print list1
    print list2
    c2nSet1=len(list1)*(len(list1)-1)/2
    c2nSet2=len(list2)*(len(list2)-1)/2
    area=0.0
    for i in range(len(list1)-1):
        pos=i+1
        onTheLeft=(pos)*(pos-1)/2
        print "left=",onTheLeft
        pos=len(list1)-i-1
        onTheRight=pos*(pos-1)/2
        print "right=",onTheRight
        withCurrent=c2nSet1-(onTheLeft+onTheRight)
        print "combinations=",(list1[i],list1[i+1]),withCurrent
        area+=withCurrent*distPoints(list1[i],list1[i+1])
    print "-------------__"
    for i in range(len(list2)-1):
        pos=i+1
        onTheLeft=(pos)*(pos-1)/2
        print "left=",onTheLeft
        pos=len(list2)-i-1
        onTheRight=pos*(pos-1)/2
        print "right=",onTheRight
        withCurrent=c2nSet2-(onTheLeft+onTheRight)
        print "combinations=",(list2[i],list2[i+1]),withCurrent
        area+=withCurrent*distPoints(list2[i],list2[i+1])
    return area*distBetweenLines

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
            m=Fraction(long(ym),long(xm))
            b=Fraction(long(p1[1]),1L)-m*Fraction(long(p1[0]),1L)
            #print p1,p2,m,b
            if m == Fraction(-1L,0L):
                m=abs(m)
            if m == Fraction(1L,0L):
                b=Fraction(long(p1[0]),1L)
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
    for m in lines:
        for b1 in lines[m]:
            if len(lines[m][b1]) == 1:
                continue
            for b2 in lines[m]:
                if len(lines[m][b2]) == 1:
                    continue
                if not b1<b2:
                    continue
                #print m,b1,b2
                area=area+FromLines((m,b1),(m,b2),lines[m][b1],lines[m][b2])
    #pprint.pprint(lines)
    print area
    return area;
    pass
if __name__ == "__main__":
    solution((
        (1,1),
        (2,0),
        (3,1),
        (2,2),
        (3,3),
        (12,100)))

