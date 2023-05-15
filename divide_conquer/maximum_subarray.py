def find_maximum_subarray(array, low, high):
	"""
	最大子数组问题：
	给定一个数组，寻找和最大的子数组
	分治思想，二分后最大子数组只可能出现三种情况：
	1、完全在左半部分
	2、完全在右半部分
	3、跨越了中点
	返回值：最大子数组的左右下标及元素和
	"""
	if low == high:
		return (low, high, array[low])
	mid = (low + high) // 2
	(left_low, left_high, left_sum) = find_maximum_subarray(array, low, mid)
	(right_low, right_high, right_sum) = find_maximum_subarray(array, mid+1, high)
	(cross_left, cross_high, cross_sum) = find_max_crossing_subarray(array, low, mid, high)
	if left_sum >= right_sum and left_sum >= cross_sum:
		return (left_low, left_high, left_sum)
	elif right_sum >= left_sum and right_sum >= cross_sum:
		return (right_low, right_high, right_sum)
	else:
		return (cross_left, cross_high, cross_sum)

def find_max_crossing_subarray(array, low, mid, high):
	left_sum = -float("inf")
	lsum = 0
	max_left = mid
	for i in range(mid, -1, -1):
		lsum += array[i]
		if left_sum < lsum:
			left_sum = lsum
			max_left = i
	right_sum = -float("inf")
	rsum = 0
	max_right = mid + 1
	for i in range(mid+1, high+1):
		rsum += array[i]
		if right_sum < rsum:
			right_sum = rsum
			max_right = i
	return (max_left, max_right, left_sum + right_sum)

if __name__ == "__main__":
	array=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print(find_maximum_subarray(array,0,len(array)-1))