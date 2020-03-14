#a_c = pi
#a_s = 4
#a_c/a_s = n_c/n_s

import random

def estimate_pi(dig_precision):
    n     = 0.11
    c     = 0
    pi    = 0
    pidig = 0

    while pidig <= dig_precision:
        n = int(n * 10)
        for i in range(n//10, int(n)):
            rand_x = random.uniform(-1, 1)
            rand_y = random.uniform(-1, 1)
            d = rand_x ** 2 + rand_y ** 2
            if d <= 1: c += 1
        pi = 4.0 * c / n
        pidig = len(str(pi).split('.')[-1])

    #print(n)
    return round(pi, dig_precision)

d = 1
print('pi to', d, 'places ~', estimate_pi(d))
d = 2
print('pi to', d, 'places ~', estimate_pi(d))
d = 3
print('pi to', d, 'places ~', estimate_pi(d))
d = 4
print('pi to', d, 'places ~', estimate_pi(d))
d = 5
print('pi to', d, 'places ~', estimate_pi(d))
