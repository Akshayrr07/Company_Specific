def is_anagram():
    s1 = input().lower()
    s2 = input().lower()
    return (sorted(s1) == sorted(s2))

print(is_anagram())



# class Solution:
#     def __init