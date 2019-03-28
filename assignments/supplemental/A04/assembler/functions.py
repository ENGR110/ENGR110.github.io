# some functions

# repeat
# takes a string s, and an integer i, returns s concatenated with itself i times
# i must be >= 1 and <= 100
# otherwise return s unmodified
def repeat(s, i):
    if ((i <= 0) or (i > 100)):
        return s
    val = (s * i)
    return val

# test where input length is multiplied
print('testing repeat')
for i in [1, 2, 100, 99]:
    if len(repeat('ab', i)) != (2*i):
        print(i + ' failed')
# test where input is returned unaltered
for i in [0, -1, -100, 101]:
    if (len(repeat('ab', i)) != 2):
        print(i + ' failed')

# lookup and merge
d = {
    'a': '123',
    'b': '234',
    'none': '000'
}

d['a'] # '123'
thekey = 'b'
d[thekey]  # '234'

def lam(k, s):
    # insert value which goes with the key k (3 spaces before) the end of the string s
    # v: 'az', s: '12345'
    # returns: '12az345'
    s0 = s[0:-3]
    s1 = s[-3:]
    v = d[k]
    return s0 + v + s1  # TODO

print('testing lam')
for i in ['a', '0', 'b', 'none']:
    try:
        lam(i, 'hello')
    except:
        print('the key ' + i + ' had an exception of some sort')

# null hypothesis testing - in general, avoid this
# for i in ['', 'jajaja', 'none!']:
#     try:
#         print(lam(i, 'hello'))
#     except :
#         print(i + ' is not in the dictionary. As expected.')

