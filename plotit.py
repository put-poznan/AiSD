__author__ = 'Mateusz Bednarski'

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
	raw = np.loadtxt('iqsort_rnd.txt')

	x = raw[0, :]

	dd = raw[1:, :]
	str = np.array_str(dd)
	mean = np.mean(dd, axis=0)
	minima = mean - np.amin(dd, axis=0)
	maxima = np.amax(dd, axis=0) - mean

	errors = [minima, maxima]

	plt.errorbar(x, mean, errors)

	mean2 = 2 * mean
	minima2 = 2 * minima
	maxima2 = 0.5 * maxima

	errors2 = [minima2, maxima2]

	plt.errorbar(x, mean2, errors2, fmt='--s', ecolor='r', barsabove=True, elinewidth=5, capsize=10	)

	plt.show()



