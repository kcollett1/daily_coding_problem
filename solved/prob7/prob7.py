def num_decodings(valid_encoding):
    ans  = 1
    prev = 1
    valid_encoding = [int(i) for i in valid_encoding]

    for i,n in enumerate(valid_encoding[:-1]):
        if n == 1 or (n == 2 and valid_encoding[i + 1] < 7):
            valid_encoding[i] = 1
        else: valid_encoding[i] = 0

    for n in valid_encoding[-2::-1]:
        if n: ans, prev = ans + prev, ans
        else: prev = ans

    return ans

test_encoding = '111'
print('num ways', test_encoding, 'can be decoded:', num_decodings(test_encoding))

test_encoding = '1111'
print('num ways', test_encoding, 'can be decoded:', num_decodings(test_encoding))

test_encoding = '345627564782'
print('num ways', test_encoding, 'can be decoded:', num_decodings(test_encoding))

test_encoding = '3456375359311'
print('num ways', test_encoding, 'can be decoded:', num_decodings(test_encoding))

test_encoding = '32456275164782'
print('num ways', test_encoding, 'can be decoded:', num_decodings(test_encoding))
