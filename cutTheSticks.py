def cutTheSticks(arr):

    sticks_cut = []
    size = 0

    while len(arr) != 0:

        short = min(arr)
        for i in range(0, len(arr)):
            arr[i] -= short

        size = len(arr)
        sticks_cut.append(size)
        while 0 in arr:
            arr.remove(0)

    return sticks_cut

x = [5,4,4,2,2,8]
print(cutTheSticks(x))
