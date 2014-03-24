from matplotlib import legend

__author__ = 'Mateusz Bednarski'

import matplotlib.pyplot as plt
import numpy as np

def analyse(f):
	raw = np.loadtxt(f)
	x = raw[0, :]
	dd = raw[1:, :]
	str = np.array_str(dd)
	mean = np.mean(dd, axis=0)
	minima = mean - np.amin(dd, axis=0)
	maxima = np.amax(dd, axis=0) - mean

	errors = [minima, maxima]

	return x, mean, errors

if __name__ == '__main__':
	#f = raw_input('File to analyse: ')
	x, mean, errors = analyse   ('ssort_rnd')
	x1, mean1, errors1 = analyse('ssort_asc')
	x2, mean2, errors2 = analyse('ssort_desc')
	x3, mean3, errors3 = analyse('ssort_v')


	p, h ,d= plt.errorbar(x, mean, errors,    fmt='r-')
	p1, h,d = plt.errorbar(x1, mean1, errors1, fmt='g-')
	p2, h,d = plt.errorbar(x2, mean2, errors2, fmt='b-')
	p3, h, d= plt.errorbar(x3, mean3, errors3, fmt='orange')

	plt.legend([p,p1,p2,p3], ['random', 'ascending', 'descending', 'v-shaped'], loc=2)
	#plt.axis('equal')
	plt.ylabel('Execution time [s]')
	plt.xlabel('Input size')
	plt.xlabel('Shell sort')

	plt.savefig('ss' + '.png')
	plt.show()


