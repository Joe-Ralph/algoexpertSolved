inp = ['yo','act','flop','tac','cat','oy','olfp']


def groupAnagrams(wordlist):
    hashmap = {}
    for i in wordlist:
        currentWord = ''.join(sorted(i))
        if currentWord in hashmap:
            hashmap[currentWord].append(i)
        else:
            hashmap[currentWord] = [i]
    return list(hashmap.values())

print(groupAnagrams(inp))
