__author__ = 'monica_wang'

def compare1(job1, job2):
    if job1[0] - job1[1]  > job2[0] - job2[1]:
        return 1
    if job1[0] - job1[1]  < job2[0] - job2[1]:
        return -1
    if job1[0] > job2[0]:
        return 1
    if job1[0] < job2[0]:
        return -1
    return 0

def compare2(job1, job2):
    if job1[0] * job2[1] > job2[0] * job1[1]:
        return 1
    if job1[0] * job2[1] < job2[0] * job1[1]:
        return -1
    return 0

filename = "jobs.txt"
with open(filename, 'r') as f:
    num = int(f.readline())
    jobs = [(0, 0)] * num
    i = 0

    for line in f.readlines():
        weight, length = line.split()
        jobs[i] = (int(weight), int(length))
        i += 1

    result = 0
    jobs.sort(cmp=compare1, reverse=True)


    s = 0
    c = 0
    for j in jobs:
        #print "weight: ",j[0], " length: ",j[1], " diff: ", j[0]/j[1]
        c += j[1]
        s += j[0] * c

    print "result: ", s

