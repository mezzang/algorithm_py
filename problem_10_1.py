class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = -1
        self.first = -1
    
    def find(self, key):
        if not key:
            return self
        else:
            char = key[0]
            if char not in self.children:
                return None
            return self.children[char].find(key[1:])
    
    def insert(self, key, id):
        if self.first == -1:
            self.first = id
        
        if not key:
            self.terminal = id
        
        else:
            char = key[0]
            if char not in self.children:
                self.children[char] = TrieNode()
            self.children[char].insert(key[1:], id)
    
    def type(self, key, id):
        if not key:
            return 0
        else:
            if self.first == id:
                return 1
            return 1 + self.children[key[0]].type(key[1:], id)
        
def count_keys(trie, word):
        node = trie.find(word)
        if not node or node.terminal == -1:
            return len(word)
        else:
            return trie.type(word, node.terminal)
    
def solong(dicwords, keywords):
    dicwords.sort(key = lambda x: (-int(x[1]), x[0]))
    trie = TrieNode()
    for i, x in enumerate(dicwords):
        trie.insert(x[0], i)
    trie.first = -1
    cnt = sum(count_keys(trie, s) for s in keywords)
    return cnt + len(keywords) - 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    dicwords = [input().split() for _ in range(n)]
    keywords = input().split()
    print(solong(dicwords, keywords))
