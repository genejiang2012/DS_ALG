
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 
# 你可以按任意顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
# 
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
# 
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# 

# 提示：
# 
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        '''
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a list of integers")
        if not isinstance(target, int):
            raise ValueError("target must be an integer")
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            
            if nums[left] + nums[right] < target:
                left += 1
            else :
                right -= 1         
  
        return []


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        '''
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a list of integers")
        if not isinstance(target, int):
            raise ValueError("target must be an integer")
        
        num_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            else:
                num_dict[num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 16, 19]
    target = 21

    print("The first solution:")
    print(Solution().twoSum(nums, target))
    
    print("The second solution:")
    print(Solution2().twoSum(nums, target))