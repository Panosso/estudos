            # buckets_place = buckets[i]
            # if i == 0:
            #     if buckets[i] == '.' and buckets[i+1] == '.':
            #         infos['safe_space'].append(i)

            #     elif buckets[i] == 'B' and buckets[i+1] == 'B':
            #         infos['ball_off'].append(i)

            # elif i == (string_len - 1):
            #     pass

            # elif buckets[i] == '.':

            #     if buckets[i - 1] == '.' \
            #             and buckets[i + 1] == '.' \
            #             and i - 1 not in infos['safe_space']:

            #         if len(infos['ball_off']) > 0:
            #             buckets[i] = 'B'
            #             buckets[infos['safe_space'][-1]] = '.'
            #             moves += 1
            #             infos['ball_off'].pop(0)
            #             infos['safe_space'].pop(-1)

            #         else:
            #             infos['safe_space'].append(i)

            # else:

            #     if buckets[i - 1] == 'B' or buckets[i + 1] == 'B':
            #         if len(infos['safe_space']) > 0:
            #             buckets[i] = '.'
            #             buckets[infos['safe_space'][0]] = 'B'
            #             moves += 1

            #         else:
            #             infos['ball_off'].append(i)
