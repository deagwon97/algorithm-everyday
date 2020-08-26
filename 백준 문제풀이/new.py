link_dic = {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
N, M, V = 4, 5, 1
stack = []
head = V
stack.append(head)

dfs_list = []
visit_list = []

while stack != []:

    node = stack.pop()
    dfs_list.append(node)

    visit_list.append(node)
    link_dic[node].sort(reverse = True)
    for near_node in link_dic[node]:
        if near_node not in dfs_list:
            if near_node not in stack
            stack.append(near_node)
print(dfs_list)