__author__ = 'Mateusz Bednarski'

from counting_sort import counting_sort
from qsort import QuickSort
from qsort_iter import QuickSortIterative
from heap_sort import heap_sort
from shell import shell_sort
from utils import measure_exe_time
from generators import *

import numpy as np

probe_sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 20000, 35000, 50000]

if __name__ == '__main__':
	dd = np.array([
		[10, 100, 500, 1000],
		[1, 10, 100, 1000],
		[2, 20, 200, 2000],
		[3, 30, 300, 3000],
		[4, 40, 400, 4000]])
	np.savetxt('iqsort_rnd.txt', dd, header='IQsort random')
