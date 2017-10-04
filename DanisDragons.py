import math
eps=1e-12
def size(vec):
    return math.sqrt(vec[0]*vec[0]+vec[1]*vec[1])
#| v0 v1 |
#| w0 w1 |
def cross(v,w):
    return (v[0]*w[1]-v[1]*w[0])
def cmp(v,w):
    if ang(v)<ang(w):
        return 1
    if ang(v)>ang(w):
        return -1
    return 0

def ang(point):
    return math.atan2(point[1],point[0])

def intersect(ray,segment):
    #(startx0,starty1,endx2,endy3)
    q=(segment[0],segment[1])
    s=(segment[2]-segment[0],segment[3]-segment[1])
    p=(ray[0],ray[1])
    r=(ray[2],ray[3])
    crossRS=float(cross(r,s));
    if crossRS==0:
        return -1.0
    diff=(q[0]-p[0],q[1]-p[1])
    u=(cross(diff,r)/crossRS)
    t=(cross(diff,s)/crossRS)
    if t>=0.0 and 0.0<=u and u<=1.0 :
        return t*size(r)
    return -1.0
def findClosest(ray,setOfSegments):
    minDist=float("inf")
    minIdx=-1
    for seg in setOfSegments:
        dist=intersect(ray,seg)
        if dist==-1.0:
            continue
        if dist<minDist:
            minDist=dist
            minIdx=seg[4]
    return minIdx

def solution(tuple_of_painting_coords):
    hit=[False]*len(tuple_of_painting_coords)
    listPoints=[]
    for i,tup in enumerate(tuple_of_painting_coords):
        start=0
        if ang((tup[2],tup[3]))<ang((tup[0],tup[1])):
            start=1
        listPoints.append((tup[0],tup[1],start,i))
        listPoints.append((tup[2],tup[3],1-start,i))
    listPoints=sortAngle(listPoints)
    #list is (x,y,start 0 / end 1, index of segment)
    segmSet=set()
    for point in listPoints:
        ray=(0,0,point[0],point[1])
        if point[2]==0 :
            segmSet.add(tuple_of_painting_coords[point[3]]+(point[3],))
        if point[2]==1 :
            segmSet.remove(tuple_of_painting_coords[point[3]]+(point[3],))
        #print findClosest(ray,segmSet)
        hit[findClosest(ray,segmSet)]=True
    cnt=0
    for i in hit:
        if i == True:
            cnt+=1
    return cnt

#sort points by angle with Ox
def sortAngle(points):
    points.sort(cmp,reverse= True)
    return points


if __name__ == "__main__":
    with open('test.txt') as f:
        inp = [tuple(map(int, i.split(' '))) for i in f]
    print solution(inp)

    
