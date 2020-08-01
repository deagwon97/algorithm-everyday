N, new_score, p = [7, 95,10]
score_list = [95, 80,70,60,50,50,40]

#N, new_score, p = [1, 12,10]
#score_list = [10]

#N, new_score, P = list(map(int, input().split()))
#score_list = list(map(int, input().split()))

if N == 0:
    print(1)

elif N == 1:
    if new_score >= score_list[0]:
        print(1)
    else:
        print(2)
else:
    score_list = sorted(score_list, reverse= True)
    new_score_loc = N + 1
    for i  in range(len(score_list)):
        if i == 0: # i == 0 일 때
            level = 1
            if new_score >= score_list[i]:
                new_score_loc = i + 1
                break
            if (len(score_list) == 1) & (new_score < score_list[i]):
                level = 2
                new_score_loc = i + 1 
                break

        elif i == len(score_list) - 1:
            ## level 설정
            if score_list[i-1] > score_list[i]:
                level = i + 1

            elif score_list[i-1] == score_list[i]:
                level = level

            # new_level 판단
            if new_score < score_list[i]:
                level = N + 1

            elif new_score == score_list[i]:
                level = level
        else:
            if score_list[i -1] > score_list[i]:
                level = i + 1
            elif  score_list[i -1] == score_list[i]:
                pass
            
            if new_score > score_list[i+1]:
                if new_score < score_list[i]:
                    level = i + 2
                elif new_score == score_list[i]:
                    level = level
                new_score_loc = i + 2
                break
    if new_score_loc <= P:
        print(level)
    else:
        print(-1)