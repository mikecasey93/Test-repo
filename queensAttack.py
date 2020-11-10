def queensAttack(n, k, r_q, c_q, obstacles):

    left = c_q - 1
    right = n - c_q
    up = n - r_q
    down = r_q - 1
    up_left = left if up >= left else up
    up_right = right if up >= right else up
    down_left = left if down >= left else down
    down_right = right if down >= right else down

    for obst in obstacles:
        row = obst[0]
        col = obst[1]

        if row == r_q and col < c_q:
            if c_q - col - 1 < left:
                left = c_q - col - 1

        elif row == r_q and col > c_q:
            if col - c_q - 1 < right:
                right = col - c_q - 1

        elif row > r_q and col == c_q:
            if row - r_q - 1 < up:
                up = row - r_q - 1

        elif row < r_q and col == c_q:
            if r_q - row - 1 < down:
                down = r_q - row - 1

        elif row > r_q and col < c_q:
            if row - r_q == c_q - col:
                if row - r_q - 1 < up_left:
                    up_left = row - r_q - 1

        elif row > r_q and col > c_q:
            if row - r_q == col - c_q:
                if row - r_q - 1 < up_right:
                    up_right = row - r_q - 1

        elif row < r_q and col < c_q:
            if r_q - row == c_q - col:
                if r_q - row - 1 < down_left:
                    down_left = r_q - row - 1

        elif row < r_q and col > c_q:
            if r_q - row == col - c_q:
                if r_q - row - 1 < down_right:
                    down_right = r_q - row - 1

    attack = left + right + up + down + up_left + up_right + down_left + down_right
    return attack
