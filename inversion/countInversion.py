__author__ = 'monica_wang'

def countInversions(array):
    n = len(array)
    if n <= 1:
        return 0, array

    inv1, sorted1 = countInversions(array[:n/2])
    inv2, sorted2 = countInversions(array[n/2:])

    i, j, k = 0, 0, 0
    sorted = [0] * n
    inv = inv1 + inv2
    for k in range(n):
        if j == len(sorted2) or (i < len(sorted1) and sorted1[i] < sorted2[j]):
            sorted[k] = sorted1[i]
            i += 1
        else:
            sorted[k] = sorted2[j]
            inv += len(sorted1) - i
            j += 1
    return inv,
'''
array = []
with open('../text.txt', 'r') as f:
    for line in f.readlines():
        array.append(int(line))

print countInversions(array)
'''
