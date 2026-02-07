"""
707. Design Linked List

Design your implementation of a linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes:
    - val: value of the current node
    - next: pointer/reference to the next node
If you want to use a doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList()         -> Initializes the MyLinkedList object.
int get(index)         -> Get the value of the index-th node in the linked list. If the index is invalid, return -1.
void addAtHead(val)    -> Add a node of value val before the first element of the linked list.
                         After the insertion, the new node will be the first node of the linked list.
void addAtTail(val)    -> Append a node of value val as the last element of the linked list.
void addAtIndex(index, val) -> Add a node of value val before the index-th node in the linked list.
                              If index equals the length of the linked list, the node will be appended to the end.
                              If index > length, the node will not be inserted.
void deleteAtIndex(index) -> Delete the index-th node in the linked list, if the index is valid.

Example 1:
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]

Output:
[null, null, null, null, 2, null, 3]

Explanation:
MyLinkedList myLinkedList = new MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.get(1)              # returns 2
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
myLinkedList.get(1)              # returns 3

Constraints:
    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex, and deleteAtIndex.
"""

################################################################################
# Brute force/baseline solution: Singly Linked List implementation
# Approach: Simple iterative handling for each operation.
# Intuition: Use a size counter and head pointer.
# TC: O(N) for get, addAtIndex, deleteAtIndex; O(1) for addAtHead, O(N) for addAtTail
# SC: O(N)
################################################################################

# Node object for singly linked list.
class Node:
    def __init__(self, val):
        # Node contains a value and a next pointer
        self.val = val
        self.next = None

class MyLinkedList:
    """
    Implements a singly linked list with O(N) insert/delete/get at arbitrary index,
    but O(1) add at head.
    """
    def __init__(self):
        # Head pointer to the first node and size counter
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Return the value of the node at the given index (0-based).
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Insert a node of value val at the head of the list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val at the tail of the list.
        """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index == size, append at tail.
        If index < 0, treat as addAtHead.
        If index > size, do nothing.

        Suppose the current list is:
            head -> [1] -> [2] -> [3] -> None
        To insert value 9 at index 1:
            (index 0)   (index 1) (index 2)
                    |
        After insertion:
            head -> [1] -> [9] -> [2] -> [3] -> None

        For index == 0:
            head -> [X] -> ... # i.e., add at head.
        For index == size:
            ... -> [last] -> [X] -> None # i.e., add at tail.
        """
        if index < 0:
            index = 0
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        # Walk to (index-1)-th node (prev)
        prev = self.head
        for _ in range(index-1):
            prev = prev.next
        # Create new node and insert it
        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the node at the index-th position (if valid).

        Suppose the current list is:
            head -> [1] -> [2] -> [3] -> None
        To delete node at index 1 (value 2):
            (index 0)   (index 1) (index 2)
                    |
        After deletion:
            head -> [1] -> [3] -> None

        If index == 0 (delete head):
            head -> [2] -> [3] -> None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            # Deleting head node
            self.head = self.head.next
        else:
            # Walk to (index-1)-th node (prev)
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            # Bypass the node to be deleted
            prev.next = prev.next.next
        self.size -= 1

# Example usage:
# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# myLinkedList.addAtTail(3)
# myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
# print(myLinkedList.get(1))       # returns 2
# myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
# print(myLinkedList.get(1))       # returns 3