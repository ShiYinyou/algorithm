def inversion_merge(nums):
	def merge(l,r):
		if r - l <= 1:
			return 0
		m = (l + r) // 2
		ln = merge(l,m)
		rn = merge(m,r)
		i = j = 0
		left = nums[l:m]
		right = nums[m:r]
		ll, lr = len(left), len(right)
		count = ln + rn
		while i<ll and j<lr:
			if left[i] <= right[j]:
				nums[l+i+j] = left[i]
				i += 1
			else:
				nums[l+i+j] = right[j]
				j += 1
				count += (ll-i)
		if i==ll:
			while j<lr:
				nums[l+i+j] = right[j]
				j += 1
		else:
			while i<ll:
				nums[l+i+j] = left[i]
				i += 1
		return count
	return merge(0,len(nums))


if __name__ == "__main__":
	print(inversion_merge([2,3,8,6,1]))
	print(inversion_merge([10,9,8,7,6,5,4,3,2,1]))