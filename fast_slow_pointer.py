
from structs import Node

def middle_element(root:Node):
    slow = root
    fast = root.next
    while fast and fast.next:
        print(slow.value, fast.value)
        slow = slow.next
        fast = fast.next.next
    return slow


def detect_cycle(root: Node):
    slow = root
    fast = root.next

    while slow!= fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True





# ll = Node.from_list([1,2,3,4,5])
# print(middle_element(ll).value)
# print(detect_cycle(ll))

