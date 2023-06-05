from typing import List


# Let's create a hashMap, and then iterate over all numbers in the nums list. If on some point number already
# contained in the hashMap, we can count that as duplicate and return True. If not, for loop will simply over and
# return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False
