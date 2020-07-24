def get_input():
    N = int(input())
    linked_list = []
    for i in range(N-1):
        linked_list.append(list(map(int, input().split())))
    return N, linked_list

class Node():
    node_number = None
    parent_node = None 
    children_list = []
    step = 0

    def __init__(self, node_number):
        self.node_number = node_number

    def set_parent_node(self, parent_node):
        self.parent_node = parent_node

    def set_children_list(self, children_list):
        self.children_list = children_list

    def del_child(self, child):
        for i in range(len(self.children_list)):
            if self.children_list[i] == child:
                del self.children_list[i]
                break

    def puls_step(self, plus):
        self.step += plus

class make_tree():
    node_classes = [None]
    linked_list = []

    def __init__(self, linked_list):
        self.linked_list = linked_list

        for node in range(1, N+1):
            self.node_classes.append(Node(node))
        self.make_tree(1, None)


    def find_children(linked_list, parent):
        children_list = []
        #del_list = []

        linked_index = 0
        while(linked_index < len(linked_list)):
            if parent == linked_list[linked_index][0]:
                children_list.append(linked_list[linked_index][1])   
                del linked_list[linked_index]
            elif parent == linked_list[linked_index][1]:
                children_list.append(linked_list[linked_index][0]) 
                del linked_list[linked_index]
            else:
                linked_index += 1
        return linked_list, children_list


    def make_tree_(self, now_node, parent_node):
        self.node_classes[now_node].set_parent_node(parent_node)
        self.linked_list, children_list = self.find_children(self.linked_list, now_node)
        self.node_classes[now_node].set_children_list(children_list)
        if children_list == []:
            pass
        else:
            for children in children_list:
                self.make_tree_(children, now_node)



def find_ancestral(leaf, node_classes):
    count = 1
    if node_classes[leaf].parent_node == None:
        return 0
    else:
        return count + find_ancestral(node_classes[leaf].parent_node, node_classes)


def find_leaf_list(node_classes):
    leaf_list = []
    for node in range(1, N + 1):
        if node_classes[node].children_list == []:
            leaf_list.append(node)
    return leaf_list

def count_total_step(leaf_list, node_classes):
    total_count = 0
    for leaf in leaf_list:
        total_count = find_ancestral(leaf, node_classes) + total_count
    return total_count


# 

#N = 8
#linked_list = [[7,4],[2,3],[8,1],[1,4],[6,5],[1,3],[6,4]]
N, linked_list= get_input()
# 트리 만들기
tree = make_tree(linked_list = linked_list)
node_classes = tree.node_classes


leaf_list = find_leaf_list(node_classes)

if count_total_step(leaf_list, node_classes) % 2 ==0:
    print('No')
else:
    print('Yes')

