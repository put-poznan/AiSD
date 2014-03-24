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
#probe_sizes = [10, 100, 500, 1000, 2500, 5000]

repeats = 5


if __name__ == '__main__':
	dd = np.zeros((1 + repeats, len(probe_sizes)))
	dd[0, :] = probe_sizes

	#to fill
	algo = QuickSortIterative
	gen = generate_ascending_sequence

	probeIndex = 0
	for probe in probe_sizes:
		print 'Probe size ', probe, '(Index ', probeIndex, ')...'
		for row in range(1, repeats + 1):
			print 'Repeat ', row, '...'
			data = gen(probe)
			perf = measure_exe_time(algo, data)
			dd[row, probeIndex] = perf
		probeIndex += 1


	#to fill
	np.savetxt('iqsort_rnd.txt', dd, header='IQsort random')
