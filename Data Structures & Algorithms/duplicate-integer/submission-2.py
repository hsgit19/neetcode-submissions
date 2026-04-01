class Solution:
    def hasDuplicate(self, nums: List[int]):
        temp = set()
        for num in nums:
           if num in temp:
             return True
           else:
             temp.add(num)

        return False                
        