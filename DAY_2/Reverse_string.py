s = input()
r = ''
# print(s[::-1])

# for i in range(len(s)-1, -1, -1):
#     r += s[i]
# print(r)

def r_s(s):
    if len(s) == 0:
        return s
    return r_s(s[1:])+ s[0]
print(r_s(s))