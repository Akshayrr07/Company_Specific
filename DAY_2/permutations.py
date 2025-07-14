def permute(nums, path, used, res):
    if len(path) == len(nums):
        res.append(tuple(path))
        return
    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            permute(nums, path + [nums[i]], used, res)
            used[i] = False

a = list(input().split())
res = []
used = [False] * len(a)
permute(a, [], used, res)
print(*res, "\nNumber of permutations:", len(res))
   