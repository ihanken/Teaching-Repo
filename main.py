#/usr/bin/python

def isPal(s):
    if len(s) < 2: return True

    for i in range(len(s) // 2):
        if s[i] != s[-1 * (i + 1)]: return False

    return True

if __name__ == "__main__":
    print(isPal("a"))
    print(isPal("ab"))
    print(isPal("aba"))
    print(isPal("abba"))
    print(isPal("abcba"))
    print(isPal("abccc"))
