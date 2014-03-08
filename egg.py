import matplotlib.pyplot as plt

from utils import *
from bubble_sort import bubble

seq = generate_random_sequence(5000)
print(seq)
t = measure_exe_time(bubble, seq)
print(seq)
print(t)

probes = range(0, 501, 100)
r = analyse_random_case(probes, bubble)
print(r)
# print(seq[::-1])

plt.plot(probes, r)
plt.savefig('xd.png')
plt.show()
