def find_first_min(number_list):
    return min(number_list)

def find_second_min(number_list):
    second_min = 100 #주사위에 쓰여진 수는 50 이하의 자연수
    for i in range(5):
        for j in range(i + 1, 6):
            temp = number_list[i] + number_list[j]
            if (temp <= second_min) & (i + j != 5):
             # 특이하게도 i와 j를 합하여 5가 되는 경우에는 주사위에서 숫자가 마주보지 못한다.
                second_min = temp
            else:
                pass
    return second_min

def find_third_min(number_list):
    third_min = 150 #주사위에 쓰여진 수는 50 이하의 자연수
    for i in [0, 5]:
        for j, k  in [[2,1], [1,3], [3,4], [4,2]]: # 모서리로 가능한 경우의 수를 모두 구현
                temp = number_list[i] + number_list[j] + number_list[k]
                if (temp <= third_min):
                    third_min = temp
                else:
                    pass
    return third_min


N  = int(input())
dice_numbers = list(map(int, input().split()))


first_min = find_first_min(dice_numbers)
second_min = find_second_min(dice_numbers)
third_min  = find_third_min(dice_numbers)


if N == 1:
    print(sum(dice_numbers[:-1]))
else:
    total_min = first_min * (5*(N **2) - 16*N + 12) \
                    + second_min * (8*N - 12) \
                    + third_min * (4)

    print(total_min)