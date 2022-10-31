
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def to_list(self):
        items = []
        cur_node = self
        while (cur_node):
            items.append(cur_node.value)
            cur_node = cur_node.next
        return items

    
    @classmethod
    def from_list(cls, items):
        root = Node(items[0])
        cur_node = root
        for item in items[1:]:
            cur_node.next = Node(item)
            cur_node = cur_node.next
        return root