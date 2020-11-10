def jumpingOnClouds(c):

    jumps = 0
    current = 0

    while current<len(c):
        if current + 2 < len(c) and c[current+2] == 0:
            jumps+=1
            current+=2
        elif current + 1 < len(c) and c[current+1] == 0:
            jumps+=1
            currnet+=1
        else:
            current+=1

    return jumps



x = [0,1,0,0,0,1,0]
print(jumpingOnClouds(x))
