
def checkValid(str):
    freq = {}
    for x in str:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    valtotal = sum(freq.values())
    keytotal = len(freq.keys())
    numtocheck = valtotal % keytotal
    if numtocheck > 1:
        return False
    else:
        if max(freq.values()) - min(freq.values()) > 1:
            return False
        else:
            return True

print(checkValid("abc"))
print(checkValid("abcc"))
print(checkValid("abccc"))

