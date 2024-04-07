
class TrieNode:
    def __init__(self) -> None:
        self.parent = [None]*26
        self.child  = [None]*26
        self.count = [0]*26

class Trie:
    def __init__(self) -> None:
        self.root = self.getNode()
    def getNode(self):
        return TrieNode()
    
    def insert(self,st1):
        ancestor = self.root
        for i in range(len(st1)):
            curIndex = ord(st1[i]) - ord('a')
            if ancestor.child[curIndex] is None:
                ancestor.child[curIndex] = st1[i]
                if i != 0:
                    ancestor.parent[curIndex] = st1[i-1]
        ancestor.count[curIndex] = ancestor.count[curIndex] + 1
    def search(self,st1):
        ancestor = self.root
        for i in range(len(st1)):
            curIndex = ord(st1[i]) - ord('a')
            if ancestor.child[curIndex] != st1[i]:
                return False
        if ancestor.count[curIndex] != 0:
            return True
        return False
    def delete(self,st1):
        ancestor = self.root
        for i in range(len(st1)):
            curIndex = ord(st1[i]) - ord('a')
            if ancestor.child[curIndex] != st1[i]:
                return False
        if ancestor.count[curIndex] != 0:
            ancestor.count[curIndex] -= 1
            return True
        else:
            return False

 
            



t = Trie()

#arr =["Hi","This","is","subha","Hello"]
arr = ["subha","subh","us"]
for i in arr:
    t.insert(i)

'''
print("Prefix:",t.search("prefix"))
print("Hello",t.search("Hello"))
print("Delete Hello:",t.delete("Hello"))
print("Hello",t.search("Hello"))
'''