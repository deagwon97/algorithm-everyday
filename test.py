N, M =  list(map(int, input().split()))
no_listens_or_sees = [] # (듣도 못한 사람) or (보도 못한 사람) 중복을 허용하여 모두 추가
no_listens_and_sees = [] # (듣도)와 (보도) 둘 다 중복되는 사람을 추가

for i in range(N + M):
    no_listens_or_sees.append(input())# 일단 중복을 허용하여 다 추가

no_listens_or_sees.sort() # 정렬

i = 0
while(i < len(no_listens_or_sees) - 1):
    if no_listens_or_sees[i] == no_listens_or_sees[i + 1]:
        no_listens_and_sees.append(no_listens_or_sees[i]) # 중복되는 원소를 발견했을 때는 no_listens_and_sees에 추가 하고
        i = i + 2 # 인덱스는 + 2
    else:
        i = i + 1 # 아닐 때는 인덱스 + 1
    
print(len(no_listens_and_sees))
for no_listen_and_see in no_listens_and_sees:
    print(no_listen_and_see)