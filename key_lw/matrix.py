import copy
class matrix:
    def __init__(self,rows):
        self.rows=rows
        self.m=len(self.rows)
        self.n=len(self.rows[0])
#    def __str__(self):
#        result=""
#        for row in self.rows:
#            result=result+str(row)+"/n"
#        return result
    def __str__(self):
        return "\n".join(["|"+"\t".join(["%s"%x for x in row])+"|" 
                          for row in self.rows])
    def isSquare(self):
        return self.m==self.n
    def GetDiagonal(self):
        a=self.m
        if(self.m>self.n):
            a=self.n
        return [self.rows[i][i] for i in range(0,a)]
    def GetTranspose(self):
        trans=[[self.rows[i][j] for i in range(0,self.m)] 
        for j in range(0,self.n)]
        return trans
    def __add__(self,other):
        summ=[[self.rows[i][j]+other.rows[i][j] for j in range(self.n)] 
        for i in range(self.m)]
        return matrix(summ)
    def __sub__(self,other):
        summ=[[self.rows[i][j]-other.rows[i][j] for j in range(self.n)] 
        for i in range(self.m)]
        return matrix(summ)
    def __mul__(self,other):
        otherT=matrix(other.GetTranspose())
        e=[[sum([x*y for x,y in list(zip(self.rows[j],otherT.rows[i]))])
                 for i in range(other.n)] for j in range(self.m)]
        return matrix(e)
    def rowOperation(self,row1,num,row2):
        return [self.rows[row1][i]+num*self.rows[row2][i] for i in range(self.n)]
    def ref(self):
        p=0
        a=copy.deepcopy(self.rows)
        while(p<self.m and p<self.n):
            if(self.rows[p][p]==0 and p!=self.m-1):
                c=copy.deepcopy(self.rows[p])
                self.rows[p]=copy.deepcopy(self.rows[p+1])
                self.rows[p+1]=copy.deepcopy(c)
            for i in range(0,p):
                if(self.rows[p][i]!=0):
                    self.rows[p]=self.rowOperation(p,self.rows[p][i]/self.rows[i][i]*(-1),i)
            if(self.rows[p][p]!=0):
                self.rows[p]=self.rowOperation(p,1/self.rows[p][p]-1,p)
            p+=1    
        b=copy.deepcopy(self.rows)
        self.rows=copy.deepcopy(a)
        return b
    def rref(self):
        p=0
        a=copy.deepcopy(self.rows)
        self.rows=copy.deepcopy(self.ref())
        p=0
        while(p<self.m):
            for i in range(p+1,min(self.n,self.m)):
                if(self.rows[p][i]!=0 and self.rows[i][i]):
                    self.rows[p]=self.rowOperation(p,self.rows[p][i]/self.rows[i][i]*(-1),i)
            p+=1
        b=copy.deepcopy(self.rows)
        self.rows=copy.deepcopy(a)
        return b
    def inverse(self):
        a=copy.deepcopy(self.rows)
        for i in range(self.m):
            for j in range(self.m):
                if(i==j):
                    self.rows[i].append(1)
                else:
                    self.rows[i].append(0)
        b=copy.deepcopy(self.rows)
        B=matrix(b)
        b=copy.deepcopy(B.rref())
       # print(b)
        result=[[b[i][j] for j in range(self.n,self.n+self.m)] for i in range(0,self.m)]
        return result
    def nullspace(self):
        b=copy.deepcopy(self.rows)
        B=matrix(b)
        c=copy.deepcopy(B.ref())
        C=matrix(c)
        pivot=[0]*(C.n)
        piI=[]
        f=[]
# =============================================================================
#         print(C)
# =============================================================================
        for  i in range(0,C.m):
            for j in range(0,C.n):
                if(c[i][j]!=0):
                    pivot[j]=1
                    piI.append(j)
                    break
        d=C.GetTranspose()
 #       print(print(pivot))
        for i in piI:
            f.append(d[i])
        for i in range(0,len(pivot)) :
            if(pivot[i]==0):
                e=copy.deepcopy(f)
                e.append(d[i])
                #print(d[i],"\n")
                e.append([0 for i in range(self.m)])
                #print(e)
                Ei=matrix(e)
# =============================================================================
#                 print(Ei.GetTranspose())
# ========================================================================
                F=matrix(Ei.GetTranspose())
# =============================================================================
#                 print(F)
# =============================================================================
                h=copy.deepcopy(F.rref())
                H=matrix(h)
# =============================================================================
#                 print(H)
# =============================================================================
                re=[0]*(self.n)
                re[i]=1
                p=0
                while(p<H.m):
                   re[piI[p]]=-h[p][-2]
                   p=p+1
                print(re)
        #print(d)
       # print(pivot)
    def projection(self,b):
        at=self.GetTranspose()
        AT=matrix(at)
        ata=AT*self
        #print(ata)
        ata_inverse=matrix(ata.inverse())
        #print(ata_inverse,"\n",self,"\n",AT)
        re=self*ata_inverse
        re=re*AT
        re=re*b
        return re
M=matrix([[4,4,7,2,5,2],[6,4,1,3,6,3],[3,9,5,4,9,1]])
M2=matrix([[1,3,5,3,6],[4,5,6,3,7]])
#print(M.GetDiagonal())
#print(M.__str__())
#print(M.GetTranspose())
#print(M+M2)
M3=matrix([[1,2],[2,3],[1,3],[1,4]])
M4=matrix([[1,2],[2,3],[3,4]])
M5=matrix([[1],[1],[1]])
#print(M*M3)
#print(M,"\n")
#print(M.ref())
#print(matrix(M.ref()),"\n")
#print(M.rref())
#M4=matrix([[1,2,3]])
#print(matrix(M2.inverse()))
#print(M5*M4)
#M2.nullspace()
#print(matrix(M3.GetTranspose()))
print(M4.projection(M5))
# =============================================================================
# print(M5)
# print(M4,"\n")
# print(M4*M5)
# =============================================================================
