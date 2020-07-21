N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))

sum_cards = 0

for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            temp = (cards[i] + cards[j] + cards[k])
            if M >= temp and ((M - sum_cards) > (M - temp)):
                sum_cards = cards[i] + cards[j] + cards[k]
            else:
                continue
print(sum_cards)
