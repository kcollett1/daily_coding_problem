import re

def autocomplete_brute(query, all_queries):
    len_quer     = len(query)
    poss_queries = []

    for q in all_queries:
        if q[:len_quer] == query:
            poss_queries.append(q)

    return poss_queries

def autocomplete(q, all_q):
    pat = '^' + q + '.*$'
    matches = re.match(pat, all_q[1])
    for i in matches: print(i)
    return 1

test_quer = 'de'
test_all  = ['dog', 'deer', 'deal']
print('ans should be ["deer", "deal"]:', autocomplete_brute(test_quer, test_all))
#print('ans should be ["deer", "deal"]:', autocomplete(test_quer, test_all))
