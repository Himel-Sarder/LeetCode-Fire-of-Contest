class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        LastVisited = []
        consecutivePrev = 0
        nums = []

        for word in words:
            if word == "prev":
                consecutivePrev += 1
                if consecutivePrev <= len(nums):
                    LastVisited.append(nums[len(nums) - consecutivePrev])
                else:
                    LastVisited.append(-1)
            else:
                consecutivePrev = 0
                nums.append(int(word))

        return LastVisited
