import numpy as np
A1=np.matrix([[1.,2.,3.],[4.,5.,6.],[7.,8.,10.]])
A2=np.matrix([[4,7,3],[1,7,0],[9,2,4]])
#print(A1.dot(A2))
A1_inverse=np.linalg.inv(A1)
#print(A1.dot(A1_inverse))
def check_orthogonal(A,B):
    product=np.round(A.dot(B),decimals=10)
    return np.array_equal(product,np.zeros_like(product))
def Gram_Schmidt(A): 
    vectors_A=[v for v in A] 
    orthogonal_v=[] 
    for v in vectors_A: 
        v_copy = np.copy(v) 
        for i in range(0,len(orthogonal_v)):
            norm_product=np.linalg.norm(orthogonal_v[i])* np.linalg.norm(orthogonal_v[i]) 
            v_copy -= float(np.dot(orthogonal_v[i],v.T))/ norm_product*orthogonal_v[i] 
        e = v_copy / np.linalg.norm(v_copy) 
        orthogonal_v.append(np.round(e,decimals=5)) 
#    print(orthogonal_v)
    new_v=[list(list(v)[0]) for v in orthogonal_v] 
    Q=np.matrix(new_v) 
    return (Q)
#print(Gram_Schmidt(A1))
B1=np.matrix([[1.],[2.],[1.]])
#print(np.linalg.lstsq(A1,B1))
#print(np.round(np.linalg.det(A1),decimals=5))
#print(np.linalg.eig(A1))
print(np.linalg.matrix_power(A1,2))