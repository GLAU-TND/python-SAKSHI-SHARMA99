l = []
s = input("Enter the string: ")
k = int(input("enter the length of substring"))

l = [s[i:i + k] for i in range(0, len(s), k)]
print(l)
for i in l:
    for j in range(len(i)):
        res = [i[:-1] for i in l if l[i][-1] == ' ']
    else:
        continue
print(res)


