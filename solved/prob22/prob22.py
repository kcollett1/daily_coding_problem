def get_sentence(poss_words, sentence):
    # poss_words is a set {} of words
    # sentence is string of letters with no spaces
    def check_sentence(curr_word, remaining_sentence, ans):
        for c in remaining_sentence:
            w += c
        if w in poss_words:
            
