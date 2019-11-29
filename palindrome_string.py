st = input("enter the string: ")
k = int(input("enter the value: "))
def isKPalRec(str1, str2, m, n):
    if not m: return n
    if not n: return m
    if str1[m - 1] == str2[n - 1]:
        return isKPalRec(str1, str2, m - 1, n - 1)
    res = 1 + min(isKPalRec(str1, str2, m - 1, n),
                  (isKPalRec(str1, str2, m, n - 1)))
    return res
def isKPal(st, k):
    revStr = st[::-1]
    l = len(st)
    return (isKPalRec(st, revStr, l, l) <= k * 2)
print("True" if isKPal(st, k) else "False")


