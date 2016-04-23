__author__ = 'monica_wang'

import heap

def readDataStream(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [ int(s) for s in lines]


stream = readDataStream("Median.txt")
#stream = [11 ,3 ,6 ,9 ,2 ,8 ,4 ,10 ,1 ,12 ,7 ,5]
small = [min(stream[0], stream[1])]
large = [max(stream[0], stream[1])]
medians = [stream[0], small[0]]

for a in stream[2:]:
    # if k is odd, then mk is ((k+1)/2)th smallest number
    if len(small) == len(large):
        if a < max(small):
            medians.append(max(small))
            heap._heappush_max(small, a)
        elif a > min(large):
            medians.append(min(large))
            largemin = heap.heappushpop(large, a)
            heap._heappush_max(small, largemin)
        else:
            medians.append(a)
            heap._heappush_max(small, a)

    # if k is even, then mk is the (k/2)th
    else:
        if a < max(small):
            m1 = heap._heappushpop_max(small, a)
            heap.heappush(large, m1)
            medians.append(max(small))
        elif a > min(large):
            medians.append(max(small))
            heap.heappush(large, a)
        else:
            medians.append(max(small))
            heap.heappush(large, a)

print "result: ", sum(medians)




