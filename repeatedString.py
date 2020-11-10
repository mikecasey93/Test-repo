def repeatedString(s, n):

    n1 = (n//len(s))
    x = s.count('a')
    x1 = n1 * x
    x2 = s[:n%(len(s))].count('a')
    return x1 + x2


print(repeatedString("aba", 10))
