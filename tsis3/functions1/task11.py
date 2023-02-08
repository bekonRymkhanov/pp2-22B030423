def ispalindrome(word):
    for i in range(len(word)-1):
        if word[-i-1]==word[i]:
            pass
        else:
            return False
    return True
print(ispalindrome("madam"))
print(ispalindrome("msdam"))
print(ispalindrome("a s d f f d s a"))
print(ispalindrome("a s d d f d s a"))
