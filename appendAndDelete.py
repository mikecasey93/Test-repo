def appendAndDelete(s,t,k):

    num_of_moves = 0
    for i,j in zip(s,t):
        if i == j:
            num_of_moves += 1
        else:
            break

    total_len = len(s) + len(t)

    if total_len <= 2 * num_of_moves + k and total_len % 2 == k % 2 or total_len < k:
        return "Yes"
    else:
        return "No"

a = "y"
b = "yu"
c = 2
print(appendAndDelete(a,b,c))
