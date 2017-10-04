# Please write your code inside the function stub below.
def solution(s, x, y):
    cnt={'A':[0L]*len(s),'G':[0L]*len(s),'C':[0L]*len(s),'T':[0L]*len(s)}
    letters=['A','T','C','G']
    for i,c in enumerate(s):
        for l in letters:
            if(i>0):
                cnt[l][i]=cnt[l][i-1]
        cnt[c][i]+=1
    #print x,len(s),x%len(s)
    start=long(x)%len(s)
    end=long(y)%len(s)
    startOfBlock=(long(x)/len(s)+1L)*len(s)
    endOfBlock=(long(y)/len(s))*len(s)
    timesBlock=max(endOfBlock-startOfBlock,0L)
    timesBlock/=len(s)
    #print (timesBlock)
    #print start,end,startOfBlock,endOfBlock,timesBlock
    #print "y/s ", y/len(s), x/len(s)
    cntAns={'A':0L,'G':0L,'C':0L,'T':0L}
    if y/len(s)==x/len(s):
        for l in letters:
            if(start>0):
                cntAns[l]+=cnt[l][end]-cnt[l][start-1]
            else:
                cntAns[l]+=cnt[l][end]
    else:
        for l in letters:
            cntAns[l]+=cnt[l][len(s)-1]*timesBlock
            cntAns[l]+=cnt[l][end]
            if start>0:
                cntAns[l]+=cnt[l][len(s)-1]-cnt[l][start-1]
            else:
                cntAns[l]+=cnt[l][len(s)-1]
    if(cntAns['A']>cntAns['C'] and cntAns['A']>cntAns['T'] and cntAns['A']>cntAns['G']):
        return cntAns['A']
    if(cntAns['C']>cntAns['A'] and cntAns['C']>cntAns['T'] and cntAns['C']>cntAns['G']):
        return cntAns['C']
    if(cntAns['G']>cntAns['A'] and cntAns['G']>cntAns['T'] and cntAns['G']>cntAns['C']):
        return cntAns['G']
    if(cntAns['T']>cntAns['A'] and cntAns['T']>cntAns['G'] and cntAns['T']>cntAns['C']):
        return cntAns['T']
    return 0
if __name__ == "__main__":
    print solution("AATT",4,6);
