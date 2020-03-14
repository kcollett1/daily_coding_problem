def climb_1or2(n):
    if n < 1: return 0

    prev = 0
    curr = 1
    for _ in range(n): prev, curr = curr, prev + curr

    return curr

def climb_variable(climb, n):
    steps = [1]
    for s in range(1, n + 1):
        tot = 0
        for j in climb:
            p = s - j
            if p < 0: break
            tot += steps[p]
        steps.append(tot)

    return steps[-1]

print('ans should be 5 for N = 4:', climb_1or2(4))
print('ans should be 1 for N = 1:', climb_1or2(1))
print('ans should be 2 for N = 2:', climb_1or2(2))
print('ans should be 3 for N = 3:', climb_1or2(3))

print('ans should be 3 for climbing [1,3,5] steps at a time for N = 4:', climb_variable([1,3,5], 4))
print('ans should be 5 for climbing [1,3,5] steps at a time for N = 5:', climb_variable([1,3,5], 5))
