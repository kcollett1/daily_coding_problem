# given a func rand5() that returns an int from 1 to 5 inclusive with uniform distribution
# make a func rand7() that returns an int from 1 to 7 inclusive with uniform distribution

import random
import time
import matplotlib.pyplot as plt

random.seed(time.time())

samplesize = 100000
randnums = []

def rand5()-> int:
    '''function to generate uniformally distributed
       random number from 1 to 5 inclusive'''
    return random.randint(1,5)

def randn(n: int)-> int:
    '''generate uniformally distributed random number
       from 1 to n inclusive, with n < 26.
       We map the values 1..25 to the values 1..n modularly
       i.e. for n = 7 {1:1, 2:2:, 3:3, 4:4, 5:5, 6:6, 7:7, 8:1,
       9:2, ... 21:7, 22:1, 23:2, 24:3, 25:4}
       We only use numbers generated for 'complete sets' to keep
       distribution uniform, i.e. for n=7, 21 is the last valid number'''
    if n > 25:
        raise ValueError('n must be less than 26')

    # adding rand num from (0, 5, 10, 15, 20) to rand num
    # from (1..5) to get rand num from (1..25)
    num1to25 = (rand5() - 1) * 5 + rand5()

    # discard nums after the complete sets otherwise
    # distribution of rand nums will not be uniform
    if num1to25 > (25 // n) * n:
        return 0

    return num1to25 % n + 1

def gen_data(n, samplesize):
    '''generate rand num from 1..n inclusive samplesize times
       and visualize data with matplotlib histogram.
       n must be less than 26 since we are using the rand5()
       function as the basis of our random number generation'''
    if n > 25:
        raise ValueError('n must be less than 26')

    global randnums

    # reset generated data before each run
    randnums = []

    # generate random numbers until desired sample size is reached
    while len(randnums) < samplesize:
        randnum = randn(n)
        if randnum == 0:
            continue
        randnums.append(randnum)

    plt.clf()
    plt.hist(randnums, bins=n)
    plt.show(block=False) # just to visualize data, see if it is indeed uniformally distributed

#gen_data(32, samplesize) # throws correct ValueError
gen_data(7, samplesize)
#gen_data(9, samplesize)
plt.show()
