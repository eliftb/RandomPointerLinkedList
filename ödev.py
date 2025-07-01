
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        original = head
        copy = head.next
        new_head = copy
        while original:
            original.next = original.next.next
            copy.next = copy.next.next if copy.next else None
            original = original.next
            copy = copy.next

        return new_head
"""
BURADA DA DENEME YAPIYORUM DENEME KODU BU

A = Node(1)
B = Node(2)
C = Node(3)

A.next = B
B.next = C


A.random = C
B.random = A
C.random = B

solution = Solution()
copied_head = solution.copyRandomList(A)

    
print(copied_head.val)                  # 1
print(copied_head.random.val)          # 3 (A'.random → C')
print(copied_head.next.val)            # 2 (B')
print(copied_head.next.random.val)     # 1 (B'.random → A')
print(copied_head.next.next.val)       # 3 (C')
print(copied_head.next.next.random.val)# 2 (C'.random → B')
"""