# Run-length encoding is a fast and simple method of
# encoding strings. The basic idea is to represent
# repeated successive characters as a single count
# and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can
# assume the string to be encoded have no digits and
# consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

def runlen_encode(dec_str):
    enc_str = ''

    if dec_str == '': # empty string to encode, return empty string
        return enc_str

    prev_ct = 1
    prev_char = dec_str[0]

    for c in dec_str[1:]:
        if prev_char != c: # add previous char and char count to encoded str, reset prev vars
            enc_str += str(prev_ct) + prev_char
            prev_ct = 1
            prev_char = c
        else: # increment prev counter
            prev_ct += 1

    # add last char/char ct pair
    enc_str += str(prev_ct) + prev_char

    return enc_str

def runlen_decode(enc_str):
    dec_str = ''

    if enc_str == '': # empty string to decode, return empty string
        return dec_str

    char_ct = ''

    for c in enc_str:
        if c.isdigit(): # record num of times to add following char to decoded string
            char_ct += c
        else: # add char to decoded string the appropriate number of times and reset vals
            dec_str += c * int(char_ct) # assuming a valid input string, so this should always be an int value
            char_ct = ''

    return dec_str

test_encode_str = 'AAAABBBCCDAA'
print('should be 4A3B2C1D2A:', runlen_encode(test_encode_str), '(', runlen_encode(test_encode_str) == '4A3B2C1D2A', ')')
print('check if decoded encoded string matches original string:', runlen_decode(runlen_encode(test_encode_str)), '(', test_encode_str == runlen_decode(runlen_encode(test_encode_str)), ')')

test_encode_str = ''
print('should be (blank):', runlen_encode(test_encode_str), '(', runlen_encode(test_encode_str) == '', ')')
print('check if decoded encoded string matches original string:', runlen_decode(runlen_encode(test_encode_str)) == '', '(', test_encode_str == runlen_decode(runlen_encode(test_encode_str)), ')')
