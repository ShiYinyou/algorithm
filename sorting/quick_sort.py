def quick_sort(nums, begin, end):
	"""
	快速排序
	选取一个元素作为基准，将大于其的元素放在右边，小于其的元素放在左边
	使用双指针进行实现：右指针先行动
	"""
	if begin >= end:
		return
	left, right = begin, end
	base = nums[begin]
	while left<right:
		while left<right and nums[right]>=base:
			right -= 1
		while left<right and nums[left]<=base:
			left += 1
		if left==right:
			break
		else:
			nums[left], nums[right] = nums[right], nums[left]
	nums[begin], nums[left] = nums[left], nums[begin]
	quick_sort(nums, begin, left-1)
	quick_sort(nums, left+1, end)


if __name__ == "__main__":
	nums = [2,8,7,1,3,5,6,4]
	quick_sort(nums,0,len(nums)-1)
	print(nums)