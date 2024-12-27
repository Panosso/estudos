# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(buckets):
    
    buckets = list(buckets)
    bucket_len = len(buckets)
    ball_count = buckets.count("B")
    moves = 0
    infos = {'ball_off': {}, 'safe_space': {}}

    if bucket_len % 2 == 0:
        is_possible = -1 if ball_count > int(bucket_len / 2) else 0

    else:
        is_possible = -1 if ball_count > int((bucket_len + 1) / 2) else 0

    if is_possible == -1:
        return is_possible
    
    else:
        for i in range(len(buckets)):
            actual_pos = buckets[i]
            if i == 0:
                if buckets[i] == '.' and buckets[i+1] == '.':
                    infos['safe_space'].append(i)

                elif buckets[i] == 'B' and buckets[i+1] == 'B':
                    infos['ball_off'].append(i+1)

            elif i == (bucket_len - 1):
                pass

            elif buckets[i] == '.':

                if buckets[i - 1] == '.' \
                        and buckets[i + 1] == '.' \
                        and i - 1 not in infos['safe_space']:

                    if len(infos['ball_off']) > 0:
                        buckets[i] = 'B'
                        buckets[infos['safe_space'][-1]] = '.'
                        moves += 1
                        infos['ball_off'].pop(0)
                        infos['safe_space'].pop(-1)

                    else:
                        infos['safe_space'].append(i)

            else:

                #That mean i'm a 'B' and in a wrong place
                if buckets[i - 1] == 'B' or buckets[i + 1] == 'B':
                    if buckets[i + 1] == '.':
                        buckets[i] = '.'
                        buckets[i+1] = 'B'
                        moves += 1

                    elif len(infos['safe_space']) > 0:
                        buckets[i] = '.'
                        buckets[infos['safe_space'][0]] = 'B'
                        moves += 1

                    else:
                        if i not in infos['ball_off']:
                            infos['ball_off'].append(i)

    return moves

print(solution('BB.B.BBB...'))
# print(solution('.B.B.B'))
# print(solution('B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.B.'))
# print(solution('B.B.BB.'))
# print(solution('BB..BBB....'))

# print(solution('B.BBB.B......BBBBBBBBBBBBBBB.................'))
