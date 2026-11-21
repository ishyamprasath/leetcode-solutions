class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True

    def _find(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and '#' in node

    def isPrefix(self, word: str) -> bool:
        return self._find(word) is not None
