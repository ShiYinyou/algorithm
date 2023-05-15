def heap_sort(nums):
	"""
	堆排序
	使用最大堆进行升序排序
	首先构造最大堆
	每次将根节点（最大节点）取出与末尾元素交换
	然后对当前根节点进行下沉
	**********
	对于堆的处理，让0索引保存堆元素个数
	对元素下标从1开始
	对元素i，父节点为i//2，左右子节点为2i.2i+1
	叶子节点为n//2+1~n
	"""
	def max_heapify(nums, i):
		"""
		维护堆的性质
		节点逐级下降
		"""
		maxindex = i
		left = i<<1
		if left<=nums[0] and nums[maxindex] < nums[left]:
			maxindex = left
		right = i<<1 + 1
		if right<=nums[0] and nums[maxindex] < nums[right]:
			maxindex = right
		if maxindex != i:
			nums[i], nums[maxindex] = nums[maxindex], nums[i]
			max_heapify(nums, maxindex)
		return nums

	def build_max_heap(nums):
		"""
		建立最大堆
		"""
		nums.insert(0,len(nums))
		for i in range(nums[0]//2,0,-1):
			max_heapify(nums, i)
		return nums

	nums = build_max_heap(nums)
	for i in range(nums[0],1,-1):
		nums[i], nums[1] = nums[1], nums[i]
		nums[0] -= 1
		max_heapify(nums,i)
	return nums[1:]

if __name__ == "__main__":
	print(heap_sort([16,14,10,8,7,9,3,2,4,1]))
	print(heap_sort([5,13,2,25,7,17,20,8,4]))
