def get_input():
    linked_list = []
    N = int(input())
    for i in range(N-1):
        linked_list.append(list(map(int, input().split())))
    return N, linked_list

def make_tree_dic(linked_list, N):
    linked_dic = {}
    for i in range(1, N+1):
        linked_dic[i] = []
    for link in linked_list:
        linked_dic[link[0]].append(link[1])
        linked_dic[link[1]].append(link[0])
        
    return linked_dic

N, linked_list= get_input()
linked_dic = make_tree_dic(linked_list, N)


total_count = 0

def count_step(del_node, parent_node, linked_dic, count):
    global total_count


    children_list = linked_dic[parent_node]

    if (len(children_list) == 1) and (children_list[0] == del_node):
        total_count += count
    else:
        for child in children_list:
            if child == del_node:
                pass
            else:
                count_step(parent_node, child, linked_dic, count + 1)
count_step(None, 1, linked_dic, 0)

if total_count %2 == 0:
    print('No')
else:
    print('Yes')
