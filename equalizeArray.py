from collections import Counter

def equalizeArray(arr):
    data = Counter(arr)
    mode = [k for k, v in data.items() if v == data.most_common(1)[0][1]]
    counter = arr.count(mode[0])
    leftover = len(arr) - counter

    if len(mode) == 1:
        return leftover
    elif len(mode) > 1:
        return leftover
    elif len(mode) == len(arr):
        return len(arr) - 1


w = [1,2,3,4,5,6]
print(equalizeArray(w))
