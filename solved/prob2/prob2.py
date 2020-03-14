def prod_except_brute(arr, i):
    prod = 1
    for j in range(len(arr)):
        if i == j: continue
        prod *= arr[j]
    return prod

def prod_except_iter(arr):
    return [prod_except_brute(arr, i) for i in range(len(arr))]

def prod_except_for_whole_arr(arr):
    if arr == []: return arr

    res = [1]
    l_a = len(arr)

    for i in range(l_a - 1, 0, -1):
        res.append(res[-1] * arr[i])
    res = res[::-1]

    p = 1
    for i in range(l_a):
        p_tmp  = p * arr[i]
        res[i] *= p
        p = p_tmp

    return res


input_arr = [1,2,3,4,5]
print('for input array:',input_arr)
print(prod_except_iter(input_arr))
print(prod_except_for_whole_arr(input_arr))

input_arr = [3,2,1]
print('for input array:',input_arr)
print(prod_except_iter(input_arr))
print(prod_except_for_whole_arr(input_arr))
