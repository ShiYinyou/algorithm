def radix_sort(A):
	"""
	基数排序
	将待排序数组元素的每一位视为一列
	从低位到高位按列排序
	最终即可得到有序序列
	[329,457,657,839,436,720,355]
	个位排序：[720,355,436,457,657,329,839]
	十位排序：[720,329,436,839,355,457,657]
	百位排序：[329,355,436,457,657,720,839]
	"""
	def maxBit(A):
		"""
		求数组A的最大位数
		"""
		maxnum = 0
		for i in A:
			maxnum = max(maxnum,i)
		count = 0
		while maxnum!=0:
			count += 1
			maxnum //= 10
		return count

	d = maxBit(A)
	div = 1
	record = []
	for i in range(10):
		record.append([])
	for i in range(d):
		for r in record:
			r.clear()
		for num in A:
			record[(num//div)%10].append(num)
		A = []
		for r in record:
			A += r
		div *= 10
	return A

if __name__ == "__main__":
	print(radix_sort([329,457,657,839,436,720,355]))
