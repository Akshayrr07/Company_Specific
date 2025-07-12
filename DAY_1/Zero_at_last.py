# l = list(map(int, input().split()))
# l1 = []
# l2 = []
# for i in l:
#     if i == 0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l2 + l1)

class Solution():
    def __init__(self):
        self.l = []
        self.l1 = []
        self.l2 = []

    def get_input(self):
        self.l = list(map(int,input().split()))

    def Zero_at_last(self):
        for i in self.l:
            if i == 0:
                self.l1.append(i)
            else:
                self.l2.append(i)
        return (self.l2 + self.l1)
    
    def display(self):
        print(self.Zero_at_last())


if __name__ == "__main__":
    a = Solution()
    a.get_input()
    a.display()