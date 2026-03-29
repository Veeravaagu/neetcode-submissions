class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1:30 Wrong Soln.
        res = []
        nums.sort()
        for i in range (len(nums)):
            target = nums[i]
            left = 0
            right = len(nums) - 1
            while right > left and right != left:
                if left == i:
                    left += 1
                elif right == i:
                    right -=1
                else:
                    if nums[left] + nums[right] == -nums[i]:
                        if [nums[i],nums[left],nums[right]] or [nums[right],nums[i],nums[left]] or [nums[left],nums[right],nums[i]] or [nums[right],nums[left],nums[i]] or [nums[i],nums[right],nums[left]] not in res:
                            res.append([nums[i],nums[left],nums[right]])
                        left +=1 
                        right -=1
                    elif nums[left] + nums[right] > -nums[i]:
                        right -= 1
                    else:
                        left += 1
            i += 1
        return res
            



        