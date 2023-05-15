def insertion_sort(nums):
"""
插入排序：
将数组视为已排序和未排序的两部分
取出未排序粗粉的的一个元素
将其插入到已排序部分的正确位置
"""
	for i in range(1,len(nums)):
		key = nums[i]
		j = i - 1
		while j >= 0 and nums[j] > key:
			nums[j+1] = nums[j]
			j -= 1
		nums[j+1] = key
	return nums


if __name__ == "__main__":
	print(insertion_sort([5,2,4,6,1,3]))
	print(insertion_sort([31,41,59,26,41,58]))
