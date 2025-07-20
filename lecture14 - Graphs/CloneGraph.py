from collections import defaultdict
from typing import List


class Solution:
    def clone(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
        return node

    seen = {}
    stack = [node]
    seen[node] = Node(node.val, [])

    while stack:
        v = stack.pop()
        for n in v.neighbors:
            if n not in seen:
                seen[n] = Node(n.val, [])
                stack.append(n)
            seen[v].neighbors.append(seen[n])

    return seen[node]