def square_matrix_multiply(A,B):
	"""
	朴素矩阵乘法
	依据矩阵乘法的定义进行计算，时间复杂度为O(n^3)
	"""
	l,m,n = len(A),len(B),len(B[0])
	C=[]
	for i in range(l):
		C.append([0]*n)
	for i in range(l):
		for j in range(n):
			for k in range(m):
				C[i][j] += A[i][k] * B[k][j]
	return C

def square_matrix_multiply_resursive(A,B):
	"""
	简单分治算法(仅针对2的幂次的方阵)
	将方阵均分为4个方阵
	********仅伪代码********
	divide方法和combine方法思路简单，但实现复杂
	T(n)=8T(n/2)+O(n^2)
	时间复杂度为O(n^3)
	"""
	n = len(A)
	if n==1:
		return A[0][0] * B[0][0]
	# 将方阵划分为4个子方阵
	# 可以不真实划分，而是使用下标进行分割
	A11,A12,A21,A22 = divide(A)
	B11,B12,B21,B22 = divide(B)
	# 进行递归计算
	C11 = square_matrix_multiply_resursive(A11,B11) 
		+ square_matrix_multiply_resursive(A12,B21)
	C12 = square_matrix_multiply_resursive(A11,B12) 
		+ square_matrix_multiply_resursive(A12,B22)
	C21 = square_matrix_multiply_resursive(A21,B11) 
		+ square_matrix_multiply_resursive(A22,B21)
	C22 = square_matrix_multiply_resursive(A21,B12) 
		+ square_matrix_multiply_resursive(A22,B22)
	C = combine(C11,C12,C21,C22)
	return C

def square_matrix_multiply_strassen(A,B):
	"""
	Strassen算法
	"""
	return

if __name__ == "__main__":
	A=[[1,3],[7,5]]
	B=[[6,8],[4,2]]
	print("朴素方法：")
	print(square_matrix_multiply(A,B))
	print(square_matrix_multiply(B,A))
	print("Strassen算法：")