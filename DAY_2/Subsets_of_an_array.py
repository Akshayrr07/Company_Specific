# from itertools import combinations

# a = list(map(int,input().split()))

# r = [[]]
# # for i in range(1, len(a)+1):
# #     r += list(combinations(a, i))
# # print([list(i) for i in r])


a = list(map(int,input().split()))

r = [[]]

for j in a:
    r += [a+[j] for a in r]
print(r)