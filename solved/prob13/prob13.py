def long_substr_kdistinct(k, s):
    if len(set(s)) <= k: return [s]

    substr  = s[0]
    last    = 1
    max_len = 0
    ans     = []
    len_s   = len(s)

    while last < len_s:
        while len(set(substr)) <= k and last < len_s:
            substr += s[last]
            last   += 1

        if len(substr) - 1 > max_len:
            max_len = len(substr) - 1
            ans     = [substr[:-1]]
        elif len(substr) - 1 == max_len:
            if substr[:-1] not in ans: ans.append(substr[:-1])

        while len(set(substr)) > k:
            substr = substr[1:]

        if len(substr) > max_len:
            max_len = len(substr)
            ans     = [substr]
        elif len(substr) == max_len:
            ans.append(substr)

    return ans

print(long_substr_kdistinct(2, "abcba"))
print(long_substr_kdistinct(1, "abcba"))
print(long_substr_kdistinct(5, "abcba"))
print(long_substr_kdistinct(6, "abcba"))
print(long_substr_kdistinct(3, "abcba"))
print(long_substr_kdistinct(1, "aaaaaab"))
print(long_substr_kdistinct(2, "aaaaaaabc"))
