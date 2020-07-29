import sys

N, K = list(map(int, input().split()))
one_two_list = list(map(int, sys.stdin.readline().split()))

ones_index = []
min_length = N
count_one = 0
app_K = False

for i in range(len(one_two_list)):
    if one_two_list[i] == 1:
        ones_index.append(i)
        count_one += 1
        if count_one == K:
            app_K= True
            new_length = i - ones_index[0] + 1
            count_one = count_one - 1
            del ones_index[0]
            if new_length <= min_length:
                min_length = new_length
            else:
                pass
        else:
            pass
    else:
        pass

if app_K == False:
    min_length = -1

print(min_length)