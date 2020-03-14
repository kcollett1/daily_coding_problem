sum_pairs = {}

def find_pair(nums, k):
    global sum_pairs
    seen = set()
    for i in nums:
        if i in seen:
            sum_pairs[k] = [i, k - i]
            return True
        seen.add(k - i)
    return False

def display_results(a, n):
    if find_pair(a, n): print('found sum pair for', n, ':', sum_pairs[n])
    else: print('no sum pair found for', n)


arr = [1,2,3,4,5,6]
print('checking list', arr, 'for sum pairs')

display_results(arr, 9)
display_results(arr, 3)
display_results(arr, 12)
display_results(arr, -2)

arr = [10,15,3,7]
print('checking list', arr, 'for sum pairs')

display_results(arr, 17)
