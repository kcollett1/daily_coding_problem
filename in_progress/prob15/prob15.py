import random

# not sure exactly what question is asking for, so this is a baseline I guess...
def from_stream(st):
    return st[int(random.uniform(0, len(st)))]

s = [0,1,2,3,4,5,6,7,8,9,10]
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
print(from_stream(s))
