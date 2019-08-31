n=int(input())
r=list(map(int,input().split(' ')))
print(max([r.count(i) for i in r]))