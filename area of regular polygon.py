import math
# n denotes sides
# s denoites length of each side
# area = 1/4ns**2 / tan(pi/n)

#n = 5 #sides
# s = 7 # side length in inches


def find_area(n, s):
    pi = (math.pi)
    tricky = (math.tan(math.pi/4.0)/n)
    area = (n*s)**2.0/4.0//tricky
    print area

find_area(7.0,3.0)
