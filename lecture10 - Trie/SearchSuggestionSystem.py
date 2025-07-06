from typing import List


class Solution:
    def suggestionProducts(self, products: List[str], searchWorld: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)
        result = []

        for i in range(len(searchWorld)):
            found = root.search(searchWorld[:i + 1])
            if found:
                result.append(sorted(found)[:3])
            else:
                result.append([])

        return result