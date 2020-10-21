def ceaserCipherEncrypt(string,key):
    ans = []
    for i in string:
        val = ord(i)+key
        if val > 122:
            val = val %122 + 96
        ans.append(chr(val))
    return "".join(ans)

print(ceaserCipherEncrypt("helloz",5))