tree = {1:[2,3,4],
        2:[1,5,6],
        3:[1,7,8],
        4:[1,9,10],
        5:[2],
        6:[2],
        7:[3,11,12,13],
        8:[3],
        9:[4],
        10:[4],
        11:[7],
        12:[7,14],
        13:[7],
        14:[12]}

class Queue:
    def __init__(self):
        self.items = []
    def dequeue(self):
        return self.items.pop(0)
    def queue(self, item):
        self.items.append(item)

Q = Queue()

head = 1
visit_nodes = []
i = 0

Q.queue(head)

while len(Q.items) != 0:
    current_node = Q.dequeue()
    visit_nodes.append(current_node)
    print(current_node)

    child_nodes = tree[current_node]
    for child in child_nodes:
        if child not in visit_nodes:
            Q.queue(child)
