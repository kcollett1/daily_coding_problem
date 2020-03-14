#########################################################
#       Daily Coding Problem #47                        #
#
# Given a array of numbers representing the stock
# prices of a company in chronological order, write
# a function that calculates the maximum profit you
# could have made from buying and selling that stock
# once. You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should
# return 5, since you could buy the stock at 5 dollars
# and sell it at 10 dollars.
#########################################################

def max_prof(prices: list)-> int:
    '''O(n) time, O(n) space. calculate the maximum profit
       that could have been made based on stock prices over time'''
    if not prices: # prices list must have at least one price in it
        return 0

    l = len(prices)
    max_prof = 0
    max_after = [prices[-1]]
    min_sofar = [prices[0]]

    for p in range(1, l):  # O(n)
        maxadd = max_after[-1]
        minadd = min_sofar[-1]

        if prices[l - 1 - p] > max_after[-1]:
            maxadd = prices[p]
        elif prices[p] < min_sofar[-1]:
            minadd = prices[p]

        max_after.append(maxadd)
        min_sofar.append(minadd)

    max_after = max_after[::-1]  # O(n)

    for mi,ma in zip(min_sofar, max_after):  # O(n)
        prof = ma - mi
        if prof > max_prof:
            max_prof = prof

    return max_prof

test_prices = [9,11,8,5,7,10]
print('ans should be 5:', max_prof(test_prices))
