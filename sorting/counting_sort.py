def counting_sort(A, k):
	"""
	A:原数组，k:数组中元素上限
	用一个数组C保存小于等于该下标的元素的个数
	则最终该个数就是该下标代表元素应处于的位置
	"""
	C = [0] * (k+1)
	B = [0] * len(A)
	for i in A:
		C[i] += 1
	for i in range(1, k+1):
		C[i] = C[i-1] + C[i]
	for i in range(len(A)-1,-1,-1):
		B[C[A[i]]-1] = A[i]
		C[A[i]] -= 1
	return B

if __name__ == "__main__":
	print(counting_sort([2,5,3,0,2,3,0,3],5))
	print(counting_sort([6,0,2,0,1,3,4,6,1,3,2],6))