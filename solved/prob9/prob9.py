# return largest sum of non-adjacent numbers
# arr can contain any number of integer elements
# elements can be negative, zero, or positive
# assuming answer must contain at least one element of list if list is not empty
def maxsum_nonadj(arr):
    if not arr: return 0
    len_arr = len(arr) # O(n), const space

    if len_arr == 1: return arr[0]

    max_sum  = [arr[0], 0] # [sum value, index of last element included in sum], const space, O(1)
    prev_max = [0, -1] # initial value to compare for second list value, const space, O(1)

# keep adding one list element onto list and calculate/keep track of new max sum
    for ind, val in zip(range(1, len_arr), arr[1:]): # O(n)
        tmpprev_max = max_sum # const space

        if max_sum == prev_max:
# max sum so far does not contain the preceding element
# so we can check to see if this element can be added
            if val > 0: # it is worth it to add this element onto the sum, if 0 don't bother adding it on
                max_sum = [max_sum[0] + val, ind]
        else:
# max sum so far contains preceding element
# so we want to check if adding current element instead gives a greater sum
            tmp_sum = prev_max[0] + val
            if tmp_sum > max_sum[0]: # if equal just keep it unchanged
                max_sum = [tmp_sum, ind]

# updated maxsum, now need to check if this element alone is greater than maxsum and update accordingly
# (i.e. all preceding elements are negative and this is first positive number in list)
        if val > max_sum[0]:
            max_sum = [val, ind]

# update previous max variable to contain the max sum information before adding this element
        prev_max = tmpprev_max

    return max_sum[0]


test_arr = []
print('test arr:', test_arr, 'ans should be 0:',  maxsum_nonadj(test_arr))

test_arr = [-4]
print('test arr:', test_arr, 'ans should be -4:', maxsum_nonadj(test_arr))

test_arr = [-1, -2, -19]
print('test arr:', test_arr, 'ans should be -1:', maxsum_nonadj(test_arr))

test_arr = [-1, -2, -19, 0]
print('test arr:', test_arr, 'ans should be 0:',  maxsum_nonadj(test_arr))

test_arr = [2, 4, 6, 2, 5]
print('test arr:', test_arr, 'ans should be 13:', maxsum_nonadj(test_arr))

test_arr = [5, 1, 1, 5]
print('test arr:', test_arr, 'ans should be 10:', maxsum_nonadj(test_arr))

test_arr = [-1, -1, -1, -10, 2, 4, 6, 2, 5, -10, -1, -4, 0, -3]
print('test arr:', test_arr, 'ans should be 13:', maxsum_nonadj(test_arr))
