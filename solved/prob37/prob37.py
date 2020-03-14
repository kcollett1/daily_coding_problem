# The power set of a set is the set of all its subsets.
# Write a function that, given a set, generates its power set.
# Given {1, 2, 3}, it should return
# {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
# You may also use a list or array to represent a set

## I am assuming that order of power sets does not matter in this problem
## as it is not explicitly specified, i.e. in lexicographic order or
## by length of sets, etc

res = [] # result var: power set will be stored here after power_set() func call

def power_set(input_set)-> None:
    global res
    res = [[]] # reset result var each time power_set() is called on a new test set

    def gen_all_sets(remaining: list, curr_set: list) -> None:
        for ind,val in enumerate(remaining):
            res.append(curr_set + [val])
            gen_all_sets(remaining[ind + 1:], curr_set + [val])

        return None

    gen_all_sets(input_set, [])

    return None

test_set = [1,2,3]
power_set(test_set)
print(res)

test_set = [1,3]
power_set(test_set)
print(res)
