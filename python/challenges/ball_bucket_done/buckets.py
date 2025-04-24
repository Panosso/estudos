# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(buckets):
    
    string_len = len(buckets)
    ball_count = buckets.count("B")
    moves = 0

    if string_len % 2 == 0:
        is_possible = -1 if ball_count > int(string_len / 2) else 0

    else:
        is_possible = -1 if ball_count > int((string_len + 1) / 2) else 0

    if is_possible == -1:
        return is_possible
    
    else:
        buckets = list(buckets)
        for i in range(1, len(buckets)-1 ):
            before_pos = buckets[i-1]
            actual_pos = buckets[i]

            if before_pos == 'B' and actual_pos == 'B':
                moves += 1
                buckets[i] = '.'

    return moves

print(solution('.B.B.B'))
print(solution('B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.'))
print(solution('B.B.BB.'))
print(solution('....BBBBB..'))

print(solution('B.BBB.B......BBBBBBBBBBBBBBB.................'))
