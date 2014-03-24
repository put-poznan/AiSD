from utils import *


def heap_sort(A):
	def heapify(A):
		start = (len(A) - 2) / 2
		while start >= 0:
			siftDown(A, start, len(A) - 1)
			start -= 1

	def siftDown(A, start, end):
		root = start
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if child + 1 <= end and A[child] > A[child + 1]:
				child += 1
			if child <= end and A[root] > A[child]:
				A[root], A[child] = A[child], A[root]
				root = child
			else:
				return

	heapify(A)
	end = len(A) - 1
	while end > 0:
		A[end], A[0] = A[0], A[end]
		siftDown(A, 0, end - 1)
		end -= 1


if __name__ == '__main__':
	T = generate_random_sequence(1000, 0, 9999)
	measure_exe_time(HeapSort, T)
	print is_sorted_desc(T)
	print T
