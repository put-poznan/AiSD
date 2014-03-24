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
	f = raw_input('File to analyse: ')

	x, mean, errors = analyse(f)


	plt.errorbar(x, mean, errors)
	plt.savefig(f + '.png')
	plt.show()



