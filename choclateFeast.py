def chocolateFeast(n,c,m):
    if n < c:
        return 0

    wrappers = int(n/c)
    bars_eaten = wrappers

    if wrappers < m:
        return wrappers

    while wrappers >= m :
        wrapper_trade = int(wrappers/ m)
        wrapper_leftovers = wrappers % m
        wrappers = wrapper_trade + wrapper_leftovers
        bars_eaten += wrapper_trade

    return bars_eaten

print(chocolateFeast(6,2,2))
 
