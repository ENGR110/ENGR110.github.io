# TESTS
a = 'onetwothree'
b = 'one asdf three'
c = 'one two three'
d = 'onexxthree'
# want:
# ['one', 'three']

e = 'hello there, world'
f = 'helloxworld'
g = 'helloworld'
# want:
# ['hello', 'world']

def spl(a, splitter):
    if type(splitter) == int:
        i = splitter
    else:
        i = a.index(splitter)

    i_end = i + len(splitter)
    # first_part = a[0:i]
    # last_part = a[i_end:]

    first_part = ''
    j = 0
    while j != i:
        if a[j] not in [' ', ',']:
        # if a[j] != ' ' and a[j] != ',':
            first_part += a[j]
        j = j + 1

    last_part = ''
    j = i_end
    while j != len(a):
        if a[j] not in [' ', ',']:
            last_part += a[j]
        j += 1

    return [first_part, last_part]

