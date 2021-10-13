import math
class Matrix:
    def __init__(self,rows):
        self.rows=rows
        self.m=len(rows)
        self.n=len(rows[0])
        self.T=[[]]
    
    def __str__(self):
        result=""
        for row in self.rows:
            result+=("|"+"\t".join([str(round(i,3)) for i in row])+"|\n")
        return result
    
    def getT(self):
        X=[[self.rows[j][i] for j in range(self.m)] for i in range(self.n)]
        return Matrix(X)
    
    def __mul__(self,other):
        otherT=other.getT()
        X=[[sum([x*y for x,y in zip(self.rows[i],otherT.rows[j])]) for j in range(other.n)] for i in range(self.m)]
        return X
    
    def REF(self,LIMIT=None):
        Mat_ref=[[self.rows[i][j] for j in range(self.n)] for i in range(self.m)]
        i,k=0,0
        while i<self.m and ((LIMIT==None and k<self.n) or (LIMIT!=None and k<LIMIT)):
#        while i<self.m and (k<self.n):
            VAL=0
            select_j=0
            for j in range(i,self.m):
                if abs(Mat_ref[j][k])>abs(VAL):
                    VAL=Mat_ref[j][k]
                    select_j=j
            j=select_j
            if VAL==0:
                k+=1
                continue
            elif VAL!=0 and j!=i:
                row_j=Mat_ref[j]
                Mat_ref[j]=Mat_ref[i]
                Mat_ref[i]=row_j
                
            row_i=list(Mat_ref[i])
            for j in range(self.n):
                row_i[j]/=Mat_ref[i][k]
            Mat_ref[i]=row_i
            
            for i2 in range(i+1,self.m):
                row_i2=list(Mat_ref[i2])
                for j in range(k,self.n):
                    row_i2[j]-=Mat_ref[i][j]*Mat_ref[i2][k]
                Mat_ref[i2]=row_i2
            i+=1
            k+=1
        return Matrix(Mat_ref)
    
    def RREF(self,LIMIT=None):
        Mat_rref=self.REF(LIMIT).rows
        i,k=1,0
        while i<self.m and k<self.n:
            IF_Nonzero=False
            for j in range(i,self.m):
                if Mat_rref[j][k]!=0:
                    IF_Nonzero=True
                    break
                
            if not IF_Nonzero:
                k+=1
                continue
            
            for i2 in range(0,i):
                row_i2=list(Mat_rref[i2])
                for j in range(k,self.n):
                    row_i2[j]-=Mat_rref[i][j]*Mat_rref[i2][k]
                Mat_rref[i2]=row_i2
            i+=1
            k+=1
        return Matrix(Mat_rref)
    
    def Inverse(self):
        if self.m!=self.n:
            return None
        
        Im=[[1 if i==j else 0 for j in range(self.m)] for i in range(self.m)]
        Mat_new=[[self.rows[i][j] for j in range(self.n)]+Im[i] for i in range(self.m)]
        Mat_rref=Matrix(Mat_new).RREF(LIMIT=self.m).rows
        for i in range(self.m):
            if Mat_rref[i][i]!=1:
                return None
        
        return Matrix([Mat_rref[i][self.m:] for i in range(self.m)])
    
    def NullSpace(self):
        Mat_rref=self.RREF().rows
        if self.m==self.n and [Mat_rref[i][i] for i in range(self.m)]==[1 for i in range(self.m)]:
            return "("+",".join(["0" for i in range(self.m)])+")"
        
        Dict_basis={}
        L_basis=[]
        for i in range(self.m):
            Ind_nonzero=[]
            Val_nonzero=[]
            for j in range(self.n):
                if Mat_rref[i][j]!=0:
                    Ind_nonzero.append(j)
                    Val_nonzero.append(Mat_rref[i][j])
            
            if len(Ind_nonzero)<=1:
                continue
            if Ind_nonzero[-1] not in Dict_basis:
                Dict_basis[Ind_nonzero[-1]]=[i]
                L_basis.append([0 for j in range(self.n)])
                L_basis[-1][Ind_nonzero[-1]]=1
            else:
                Dict_basis[Ind_nonzero[-1]].append(i)
            L_basis[-1][Ind_nonzero[0]]=-Val_nonzero[-1]/Val_nonzero[0]
            
            for i2 in range(1,len(Ind_nonzero)-1):
                L_basis.append([0 for j in range(self.n)])
                L_basis[-1][Ind_nonzero[-1]]=1
                L_basis[-1][Ind_nonzero[i2]]=-Val_nonzero[-1]/Val_nonzero[i2]
        
        L_basis=[[str(j) for j in b] for b in L_basis]
        line=""
        for i in range(len(L_basis)):
            line+=("("+",".join(L_basis[i])+")x%d"%i)
            if i!=len(L_basis)-1:
                line+="+"
        return line
    
    def get_line_pro(self,other):   #self=A=[[1,1,1]],other=b=[[0,1,1]]
        self.T=self.getT()
        other.T=other.getT()
        for i in self.__mul__(self.T):
            for j in i:
                denom=j
        for i in self.__mul__(other.T):
            for j in i:
                numer=j
        L=[]
        for row in self.rows:
            for i in range(len(row)):
                L.append(row[i]*numer/denom)
        L=[L]
        return Matrix(L)    #return [[0.67,0.67,0.67]]
    
    def get_minus(self,other):      #self=A=[[1,1,1]],other=b=[[0,1,1]]
        L=[]
        for i in range(len(self.rows[0])):
            L.append(self.rows[0][i]-other.rows[0][i])
        return L
        
    def get_QR(self):    #self=Matrix
        Mat_RREF=self.RREF().rows
        a=min(len(Mat_RREF),len(Mat_RREF[0]))
        pivot=0
        for i in range(a):
            if Mat_RREF[i][i]==1:
                pivot+=1
        if pivot!=self.RREF().n:
            return "No QR!"
        A=self.getT().rows
        Q=A.copy()
        for i in range(1,len(A)):
            #Q[i]=A[i]-P(Q[0],A[i])-P(Q[1],A[i])-...-P(Q[i-1],A[i])
            #Q[i]+A[i]
            for k in range(len(Q[0])):
                Q[i][k]=Q[i][k]+A[i][k]
            for j in range(0,i):
                Q[i]=Matrix([Q[i]]).get_minus(Matrix([Q[j]]).get_line_pro(Matrix([A[i]])))
        #Normal
        for row in Q:
            vector_len=0
            for i in range(len(row)):
                vector_len+=row[i]**2
            vector_len=math.sqrt(vector_len)
            for i in range(len(row)):
                row[i]=row[i]/vector_len
        Q=Matrix(Q).getT()
        QT=Q.getT()
        R=Matrix(QT.__mul__(self))
        print("Q=")
        print(Q)
        print("R=")
        print(R)
        return "A=QR is available"
    
    def det(self,Mat=None,key=True):
        if key is True:
            Mat=self.rows
        if len(Mat)!=len(Mat[0]):
            return "No determinant"
        if len(Mat)==1:
            return Mat[0][0]
        else:
            All_entry=[]
            All_cofactor=[]
            for i in range(len(Mat)):
                if i%2==0:
                    All_entry.append(Mat[0][i])
                else:
                    All_entry.append(-Mat[0][i])
                cofactor=[]
                for j in range(1,len(Mat)):
                    K=Mat[j].copy()
                    del K[i]
                    cofactor.append(K)
                All_cofactor.append(cofactor)
            det=0
            for i in range(len(All_entry)):
                det+=All_entry[i]*self.det(All_cofactor[i],False)
            return det
    
    def eig(self):
        deter=self.det()
        trace=self.rows[0][0]+self.rows[1][1]
        eig_val_1=(trace+math.sqrt(trace**2-4*deter))/2
        eig_val_2=(trace-math.sqrt(trace**2-4*deter))/2
        return eig_val_1,eig_val_2
        
        
"""*****************************************************"""        

A=Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
B=Matrix([[2,2],[2,0]])
C=Matrix([[1,2,3],[-1,0,-3],[0,-2,3]])
D=Matrix([[1,2,3]])

print(B.det())








    
    
