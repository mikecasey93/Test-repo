import math
import numbers

def squares(a, b):

    count = 0
    for i in range(a, b+1):

        sq_rt = int(math.sqrt(i))
        if sq_rt * sq_rt == i:
            count += 1

    return count

print(squares(17, 24))
