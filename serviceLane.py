def serviceLane(n, cases):
    result = []

    for i,j in cases:
        result.append(min(width[i : j+1]))

    return result
