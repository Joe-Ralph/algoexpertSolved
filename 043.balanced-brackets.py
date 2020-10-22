inp = '(([]()()){})'

def areBalancedBrackets(string):
    stack = []
    hashmap = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    for i in string:
        if i in hashmap.values():
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                if hashmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
    return True if not stack else False

print(areBalancedBrackets(inp))