import sys
from sys import stdin, stdout 

def get_input_make_dic():
    linked_dic = {}
    N = int(input())
    for i in range(1, N+1):
        linked_dic[i] = []
    for i in range(N-1):
        link = list(map(int,sys.stdin.readline().rstrip().split()))
        linked_dic[link[0]].append(link[1])
        linked_dic[link[1]].append(link[0])
    return linked_dic

def count_node(now_node, parent_node, count = 0):
    global total
    children_list = linked_dic[now_node]
    if children_list == [parent_node]:
        total = total + count
    else:
        count = count + 1
        for child in children_list:
            if child == parent_node:
                continue
            else:
                count_node(child, now_node, count = count)

linked_dic = get_input_make_dic()
total = 0
count_node(1, None, count = 0)
if total % 2 == 0:
    print('No')
else:
    print('Yes')

    
print('hello')