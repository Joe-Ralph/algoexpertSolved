string = 'ralphin'

class SuffixTrie:
    def __init__(self):
        self.root = {}
        self.suffixEnd = '*'

    def createTrieFrom(self,string):
        for i in range(len(string)):
            self.formTrie(string,i)

    def formTrie(self,string,i):
        node = self.root
        for j in range(i,len(string)):
            curr = string[j]
            if curr not in node:
                node[curr] = {}
            else:
                pass
            node = node[curr]
        node[self.suffixEnd] = True

    def contains(self,string):
        node = self.root
        for i in string:
            if i in node:
                node = node[i]
                continue
            else:
                return False
        return self.suffixEnd in node

hello = SuffixTrie()

hello.createTrieFrom(string)
print(hello.contains('phin'))