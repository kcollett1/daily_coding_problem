class order_log:
    def __init__(self):
        self.orders  = {} # dict/hash-table
        self.num_ord = 0  # O(1) lookup time for ith last element
                          # O(2N + 1) memory requirement

    def record(order_id): # add order_id to the log
        self.orders[self.num_ord] = order_id
        self.num_ord += 1

    def get_last(i): # get "ith last" element from log
        if self.num_ord < i or self.num_ord == 0:
            return 'ERROR'
        return self.orders[self.num_ord - i]

# I think using a list as the data structure wastes memory, though time lookup is also constant
# not completely sure though
