__author__ = 'Mateusz Bednarski'


def find_max_crossing_subarray(data, low, mid, high):
	"""

	:param data: Collection to analyse
	:param low: lowest index (inclusive)
	:param mid: Midpoint
	:param high: Highest index (inclusive)
	"""
	max_right = max_left = 0
	left_sum = -9223372036854775807
	summ = 0
	for i in reversed(range(low, mid + 1)):
		summ += data[i]
		if summ > left_sum:
			left_sum = summ
			max_left = i
	right_sum = -9223372036854775807
	summ = 0
	for j in range(mid + 1, high + 1):
		summ += data[j]
		if summ > right_sum:
			right_sum = summ
			max_right = j
	return max_left, max_right, left_sum + right_sum


def maximum_subarray(data, low, high):
	"""

	:param data: data to analyse
	:param low: lowest index
	:param high: highest index
	"""

	if high == low:
		return low, high, data[low]
	else:
		mid = (low + high) / 2
		leftlow, lefthigh, leftsum = maximum_subarray(data, low, mid)
		rightlow, righthigh, rightsum = maximum_subarray(data, mid + 1, high)
		crosslow, crosshigh, crosssum = find_max_crossing_subarray(data, low, mid, high)
		if leftsum >= rightsum and leftsum > crosssum:
			return leftlow, lefthigh, leftsum
		elif rightsum >= leftsum and rightsum > crosssum:
			return rightlow, righthigh, rightsum
		else:
			return crosslow, crosshigh, crosssum


dd = [1, 2, 3, -4, 5, 6, 7, -8, -9]
print maximum_subarray(dd, 0, len(dd) - 1)






