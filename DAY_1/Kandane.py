# def kadane(l):
#     f = l[0]
#     s = l[0]

#     for i in range(1,len(l)):
#         s = max(l[i],s+l[i])
#         f = max(f,s)
#     return f

# l = list(map(int,input().split()))
# print(kadane(l))

class Solution():
    
    def __init__(self):
        self.l = []
        self.first = self.second = None

    def get_input(self):
        self.l = list(map(int,input().split()))
    
    def display(self):
        print(self.kadane())

    def kadane(self):
        if not self.l:
            return 0

        max_current = max_global = self.l[0]
        for i in range(1, len(self.l)):
            max_current = max(self.l[i], max_current + self.l[i])
            max_global = max(max_global, max_current)
        return max_global


if __name__ == "__main__":
    a = Solution()
    a.get_input()
    a.display()

