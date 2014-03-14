from cStringIO import StringIO
import math

__author__ = 'Mateusz Bednarski'


def heapsort(lst):
	''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

	# in pseudo-code, heapify only called once, so inline it here
	for start in range((len(lst) - 2) / 2, -1, -1):
		siftdown(lst, start, len(lst) - 1)

	for end in range(len(lst) - 1, 0, -1):
		lst[end], lst[0] = lst[0], lst[end]
		siftdown(lst, 0, end - 1)
	return lst


def siftdown(lst, start, end):
	root = start
	while True:
		child = root * 2 + 1
		if child > end: break
		if child + 1 <= end and lst[child] < lst[child + 1]:
			child += 1
		if lst[root] < lst[child]:
			lst[root], lst[child] = lst[child], lst[root]
			root = child
		else:
			break


def show_tree(tree, total_width=64, fill=' '):
	"""Pretty-print a tree."""
	output = StringIO()
	last_row = -1
	for i, n in enumerate(tree):
		if i:
			row = int(math.floor(math.log(i + 1, 2)))
		else:
			row = 0
		if row != last_row:
			output.write('\n')
		columns = 2 ** row
		col_width = int(math.floor((total_width * 1.0) / columns))
		output.write(str(n).center(col_width, fill))
		last_row = row
	print output.getvalue()
	print '-' * total_width
	print
	return


dd = [1, 2, 3, 4, 5, 9, 6, 5, 4, 1, 6, 8, 9, 1, 3, 3]
heapsort(dd)
show_tree(dd)
print dd

