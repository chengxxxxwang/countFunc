#coding=utf-8
import os,sys

f = open('numbers.txt', 'r')
line = f.read().split('\n')
print line


 # -0.000004
 # 0.000307
 # -0.005619
 # -0.056211
 # 1.787093
 # -0.091054
a = -0.000004
b = 0.000307
c = -0.005619
d = -0.056211
e = 1.787093
f = -0.091054

for point in line:
    tmp = point.split(',')
    x = float(tmp[0])
    y = float(tmp[1])
    print 'x = %f'%(x)
    # print y
    # print '\n'
    test = a * x**5 + b * x**4 + c * x**3 + d* x**2 + e* x**1 + f
    print 'result='
    print test
    print 'y = %f' %(y)
    print '------end------'
