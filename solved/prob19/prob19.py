def opt_paint_houses(cost_mat): # n X k, nth row, kth col = cost to build nth house with kth color
    # start from any in (row 0), end at any in (row 0)
    # from col i in curr row, can go to any in next row EXCEPT FOR i
    # ans will be min cost from last row

    for house in range(1, len(cost_mat)):
        for color in range(len(cost_mat[0])):
            cost_mat[house][color] += min(cost_mat[house - 1][:color] + cost_mat[house - 1][color + 1:])

    return min(cost_mat[-1])

cm = [[1 for _ in range(7)] for _ in range(7)]
print('ans should be 7:', opt_paint_houses(cm))

print('ans should be 28:', opt_paint_houses(cm))

cm = [[1 for _ in range(7)] for _ in range(7)]
cm[0][0] = 0
print('ans should be 6:', opt_paint_houses(cm))
