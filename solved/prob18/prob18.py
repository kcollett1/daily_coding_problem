# worst case performance is O(n*k) (strictly increasing array)
# not sure if this is good enough though, or if there's a better algo
# uses O(1) space only

def max_subarrs(arr, k):
    if k > len(arr) or k < 1: return -1 # error

    maxval = arr[0]
    lastind = len(arr) - k

    for i,val in enumerate(arr[1:lastind + 1]):
        if val > arr[i]: arr[(i-k+2):(i+1)] = [val]*(k - 1)

    for val in arr[lastind + 1:]:
        if val > arr[lastind]: arr[lastind] = val

    return arr[:-k+1]

testarr = [10,5,2,7,8,7]
testk   = 3
print('ans should be [10, 7, 8, 8]:', max_subarrs(testarr, testk))

testarr = [10,5,2,7,8,7]
testk   = 6
print('ans should be [10]:', max_subarrs(testarr, testk))
