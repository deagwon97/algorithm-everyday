class Node():
    node_number = None
    parent_node = None 
    children_list = []

    def __init__(self, node_number):
        self.node_number = node_number

    def set_parent_node(self,
                 parent_node):
        self.parent_node = parent_node

    def set_children_list(self,
                 children_list):
        self.children_list = children_list

def find_children(linked_list, parent):
    children_list = []
    del_list = []

    linked_index = 0
    while(linked_index < len(linked_list)):
        if parent == linked_list[linked_index][0]:
            children_list.append(linked_list[linked_index][1])   
            del linked_list[linked_index]
        elif parent == linked_list[linked_index][1]:
            children_list.append(linked_list[linked_index][1]) 
            del linked_list[linked_index]
        else:
            linked_index += 1
    return linked_list, children_list

def set_node(linked_list, now_node, parent_node):
    node_classes[now_node].set_parent_node(parent_node)

    linked_list, children_list = find_children(linked_list, now_node)
    node_classes[now_node].set_children_list(children_list)

    if children_list == []:
        pass
        #return None
    else:
        for children in children_list:
            set_node(linked_list, children, now_node)
        #return node_list


N = 8
linked_list = [[7,4],[2,3],[8,1],[1,4],[6,5],[1,3],[6,4]]

node_classes = [None]
for node in range(1, N):
    node_classes.append(Node(node))




set_node(linked_list, 1, None)

for node in range(1, N):
    print(node_classes[node].node_number)
    print(node_classes[node].parent_node)
    print(node_classes[node].children_list)