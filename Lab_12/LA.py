import math
class Matrix:
    def __init__(self,rows):
        self.rows=rows
        self.m=len(rows)
        self.n=len(rows[0])
        self.T=[[]]
    
    def __str__(self):
        return "\n".join(["|"+"\t".join(["%s"%(x*(abs(x)>1e-10))
            for x in row])+"|" for row in self.rows])+"\n"
    
    def __add__(self,other):
        result=[[self.rows[i][j]+other.rows[i][j] for j in range(self.n)] for i in range(self.m)]
        return Matrix(result)

    def __sub__(self,other):
        result=[[self.rows[i][j]-other.rows[i][j] for j in range(self.n)] for i in range(self.m)]
        return Matrix(result)
    
    def getT(self):
        result=[[self.rows[j][i] for j in range(self.m)] for i in range(self.n)]
        return Matrix(result)
    
    def scalar_mul(self,s):
        result=[[self.rows[i][j]*s for j in range(self.n)] for i in range(self.m)]
        return Matrix(result)
    
    def __mul__(self,other):
        otherT=other.getT()
        result=[[sum([x*y for x,y in zip(self.rows[i],otherT.rows[j])]) for j in range(other.n)] for i in range(self.m)]
        return Matrix(result)
    
    def cofactor(self,m,n):
        sign=(-1)**(m+n)
        smaller_matrix=[]
        for j in range(self.m):
            if j!=m:
                smaller_matrix.append(self.rows[j][0:n]+self.rows[j][n+1:])
        sm=Matrix(smaller_matrix)
        return sign*sm.determinant()
    
    def determinant(self):
        if self.m!=self.n:
            return False
        else:
            if self.m==1:
                return self.rows[0][0]
            else:
                result=sum([self.rows[0][i]*self.cofactor(0,i) for i in range(self.n)])
                return result
            
    def inverse(self):#use cramer's law
        c_matrix=[[self.cofactor(i,j) for j in range(self.n)] for i in range(self.m)]
        return Matrix(c_matrix).getT().scalar_mul(1/self.determinant())

    def least_square(self,b): #solve Ax=b ATAx=ATb
        return (self.getT()*self).inverse()*(self.getT())*b

#    def gram_schmidt(self):# A=QR
#        self_T=self.getT()
#        Q_T=[]
#        for column in self_T.rows:
#            column_vector=Matrix([column]).getT()
#            for j in Q_T:
#                ort_vector=Matrix([j]).getT()
#                column_vector=column_vector-ort_vector.scalar_mul(((ort_vector.getT()*column_vector).rows[0][0]/(ort_vector.getT()*ort_vector).rows[0][0]))
#            column_vector=column_vector.scalar_mul(1/((sum(column_vector.rows[i][0]**2 for i in range(column_vector.m))**0.5)))
#            Q_T.append(column_vector.getT().rows[0])
#        R=Matrix([[(Matrix([Q_T[i]])*(Matrix([self.getT().rows[j]]).getT())).rows[0][0] for j in range(self.n)] for i in range(self.m)])
#        Q=Matrix(Q_T).getT()
#        return Q,R

    
#M1=Matrix([[1,2,3],[4,5,6],[7,8,9]])
#M2=Matrix([[1,2,3],[4,5,6],[7,8,10]])
#M3=Matrix([[1,0,0],[0,1,0],[0,0,1]])
#M4=Matrix([[1,2],[3,4]])
#M5=Matrix([[10,14],[14,20]])
#b=Matrix([[1],[2]])
##print(M4.determinant())
#print(M5.inverse())
#print(M4.gram_schmidt()[0])
#

M1=matrix([[1,2],[3,4]])
M2=matrix([[1,2,3,4],[4,5,6,7]])
print(M1*M2)
