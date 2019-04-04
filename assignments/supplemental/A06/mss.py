# maximum subsequence sum
# given a list as input, write a function that:
# returns the [start, end, sum] of the sub-list whose sum is highest
# out of all possible in-order sub-lists in the original list.
def mss(ls):
    start = 0
    end = 0
    s = 0
    if len(ls) == 0: return [start, end, s]
    if len(ls) == 1: return [start, end, ls[0]]

    for i in range(start, len(ls)):
        temp_sum = 0
        for j in range(i, len(ls)):
            temp_sum += ls[j]
            if temp_sum >= s:
                s = temp_sum
                start = i
                end = j

    return [start, end, s]

if __name__ == "__main__":
    print(mss([-10, 8, -2, 4, -7, 0, 0, 3, 2, -4, 5]))
    print(mss([]))
    print(mss([1]))

