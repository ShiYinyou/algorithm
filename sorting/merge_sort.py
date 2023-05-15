def merge_sort(nums):
"""
归并排序：
递归地将数组分为两部分
取两个部分的第一个元素（两部分的最小值）进行比较
将较小的元素放入合并数组，并取所在部分下一个元素
"""
	##写法一：使用Python列表的append和pop方法
	# 实现简单，但耗时较长（大量使用len方法耗时）
	# def merge1(nums):
	# 	if len(nums) <= 1:
	# 		return nums
	# 	left = merge(nums[:len(nums)//2])
	# 	right = merge(nums[len(nums)//2:])
	# 	nums.clear()
	# 	while len(left) > 0 and len(right) > 0:
	# 		if left[0] <= right[0]:
	# 			nums.append(left.pop(0))
	# 		else:
	# 			nums.append(right.pop(0))
	# 	nums += right if len(left) == 0 else left
	# 	return nums
	# return merge1(nums)


	##写法二：适用于各种编程语言，将列表作为视为定长数组，根据索引赋值
	# 实现过程相对复杂，但运行速度较快
	def merge2(l,r):
		if r - l <= 1:
			return
		m = (l + r) // 2
		merge2(l,m)
		merge2(m,r)
		i = j = 0
		left = nums[l:m]
		right = nums[m:r]
		ll, lr = len(left), len(right)
		while i<ll and j<lr:
			if left[i] <= right[j]:
				nums[l+i+j] = left[i]
				i += 1
			else:
				nums[l+i+j] = right[j]
				j += 1
		if i==ll:
			while j<lr:
				nums[l+i+j] = right[j]
				j += 1
		else:
			while i<ll:
				nums[l+i+j] = left[i]
				i += 1
		return
		
	merge2(0,len(nums))
	return nums


if __name__ == "__main__":
	print(merge_sort([2,4,5,7,1,2,3,6]))
	print(merge_sort([3,41,52,26,38,57,9,49]))