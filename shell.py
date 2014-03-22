
def ShellSort(a):

	N = len(a)
	j = 0
	p = 0
	gap = 1
	tmp = 0
	k = 1

	gap = 1
	while 0 < gap < N:
		for p in range(gap, N):
			tmp = a[p]
			j = p
			while j >= gap and tmp < a[j - gap]:
				a[j] = a[j - gap]

				j -= gap

			a[j] = tmp
		k += 1
		gap = ((3 ** k) - 1) / 2




dd = [4, 3, 6, 5, 4, -10, 15, -45, 3, 8]
ShellSort(dd)
print dd