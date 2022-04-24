class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        resdic = dict()
        for x in range(0, len(nums)):
            if nums[x] not in resdic.keys():
                resdic[nums[x]] = [x]
            else:
                resdic[nums[x]].append(x)
        lemx = 0
        result = 0
        for i in resdic.keys():
            if len(resdic[i]) > lemx:
                lemx = len(resdic[i])
                result = resdic[i][-1] - resdic[i][0] + 1
            elif len(resdic[i]) == lemx:
                if (resdic[i][-1] - resdic[i][0] + 1) < result:
                    lemx = len(resdic[i])
                    result = resdic[i][-1] - resdic[i][0] + 1
            else:
                continue
        return result