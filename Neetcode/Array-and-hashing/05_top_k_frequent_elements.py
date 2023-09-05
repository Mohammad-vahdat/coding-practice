"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        rep = [[] for i in range(len(nums)+1)]

        for key, value in seen.items():
            rep[value].append(key)

        res = []
        count = 0
        for i in range(len(rep)-1, 0, -1):

            for j in range(len(rep[i])):

                if rep[i][j] != []:
                    res.append(rep[i][j])
                    count += 1
                
                if count == k:
                    return res