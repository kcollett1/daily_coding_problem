#############################################################################
# Write an algorithm to justify text. Given a sequence of words and
# an integer line length k, return a list of strings which represents
# each line, fully justified.
#                                                                           #
# More specifically, you should have as many words as possible in each
# line. There should be at least one space between each word. Pad extra
# spaces when necessary so that each line has exactly length k. Spaces
# should be distributed as equally as possible, with the extra spaces,
# if any, distributed starting from the left. If you can only fit one
# word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
#                                                                           #
# For example, given the list of words
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly                   #
#############################################################################

def makeline(words: list, currlen: int, k: int)-> str:
    '''input is a list of words to go on a single line, an integer currlen which
       specifies the length of the line given only one space between words, and
       an integer k which is the line's length. words are guaranteed to fit on
       specified line. function returns a string of the line properly formatted
       based on the specifications of this problem. this is a helper function.'''
    if len(words) == 1:
        return words[0] + ' ' * (k - len(words[0]))

    tot_spaces = k - currlen
    all_spaces = tot_spaces // (len(words) - 1)
    ex_spaces = tot_spaces - all_spaces
    print(currlen, k, tot_spaces, all_spaces, ex_spaces)
    for i in range(len(words) - 1):
        words[i] += ' ' * all_spaces
        if ex_spaces > 0:
            words[i] += ' '
            ex_spaces -= 1

    return ' '.join(words)

def justify_textblock(words: list, k: int) -> list:
    '''input is a list of words, and an integer line length k
       output is a list of lines of text of length k containing
       the words fully justified, with extra spaces when needed
       distributed evenly starting from the left, unless there is
       one word per line, in which case the line should be left
       justified. k is guaranteed to be greater than or equal to
       the longest word.'''

    justified_text = []
    linelen = -1
    start = 0
    for ind,wd in enumerate(words):
        wd_len = len(wd) + 1
        linelen += wd_len
        if linelen > k:
            justified_text.append(makeline(words[start:ind], linelen - wd_len, k))
            start = ind
            linelen = wd_len
        elif linelen == k:
            justified_text.append(' '.join(words[start:ind+1]))
            start = ind + 1
        else:
            linelen += wd_len

    # format last line if leftover
    if linelen == k:
        justified_text.append(' '.join(line))
    elif linelen > 0:
        justified_text.append(makeline(line, linelen, k))

    # return answer
    return justified_text


test_text = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

print('result should be:')
print("the  quick brown\nfox  jumps  over\nthe   lazy   dog")
for line in justify_textblock(test_text, k):
    print(line)
