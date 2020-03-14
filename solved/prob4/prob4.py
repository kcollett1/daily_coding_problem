def first_missing(arr):
    if arr == []: return 1 # constant

    arr     = list(set(arr)) # linear? but also unnecessary technically, just allows you to do fewer iterations potentially
    len_arr = len(arr) # constant

    for i in range(len_arr): # linear
        if arr[i] <= 0: arr[i] = len_arr + 1 # get rid of 0 and negative values

    for i in range(len_arr): # linear
        if abs(arr[i]) > len_arr: continue
# change arr value with index of current val 1-based to a negative val to indicate it is present
        arr[abs(arr[i]) - 1] *= -1

    for i in range(len_arr): # linear
        if arr[i] > 0: return i + 1 # find fi:rst number (index + 1) that is positive

# all values are present up to len(arr), so answer must be len(arr) + 1
    return len_arr + 1

test_arr = [3,4,-1,1]
print('array:', test_arr)
print('ans should be 2:', first_missing(test_arr))
test_arr = [1,2,0]
print('array:', test_arr)
print('ans should be 3:', first_missing(test_arr))
test_arr = [5,7,8,-10,0,0,7,1,1,3]
print('array:', test_arr)
print('ans should be 2:', first_missing(test_arr))
