"""
LeetCode 429. N-ary Tree Level Order Traversal
Given an n-ary tree, return its level order traversal.

Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(N) for the queue + result
"""

from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children or []


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        res: List[List[int]] = []
        dq: deque[Node] = deque([root])

        while dq:
            size = len(dq)
            level: List[int] = []

            for _ in range(size):
                node = dq.popleft()
                level.append(node.val)

                if node.children:
                    for ch in node.children:
                        dq.append(ch)

            res.append(level)

        return res


