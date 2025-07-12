class Solution():
    def __init__(self):
        self.array = self.target = None
        self.r = []

    def get_input(self):
        self.array = list(map(int, input().split(",")))
        self.target = int(input())
    
    def two_sum(self):
        self.l = len(self.array)
        self.r = []
        for i in range(self.l):
            for j in range(i+1, self.l):
                if self.array[i] + self.array[j] == self.target:
                    self.r.append((i, j))
                    break
        if not self.r:
            return -1
        return self.r

    def display(self):
        print(self.r[0])



if __name__ == "__main__":
    S = Solution()
    S.get_input()
    S.two_sum()
    S.display()