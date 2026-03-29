class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #CHATGPT HELP
        hashset = set(nums)
        longest = 0
        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                longest = max(longest, length)
        return longest
#hashset = set()
#for num in nums:
    #hashset.add(num)
    #i = 1
    #count = 1
    #while i < len(nums) + 1:
       # while num + i in hashset:
      #      count += 1
     #       i += 1
     #   while num - i in hashset:
     #       count += 1
     #       i += 1
      #  i += 1

            