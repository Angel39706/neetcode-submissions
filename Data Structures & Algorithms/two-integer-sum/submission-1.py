class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Storage = {}
        #Iterate through nums with index
        for i, num in enumerate(nums):
            #Search for goal in Storage
            goal = target - num
            if goal in Storage:
                return [Storage[goal],i]
            #If not found store num in Storage to find next goal
            Storage[num] = i
