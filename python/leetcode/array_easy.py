# -*- coding: utf-8 -*-
import copy
from typing import List


class Question:
    def __init__(self, number: int = 0) -> None:
        self.question_number = number

    def question_704(self, nums: List[int], target: int) -> int:
        """
        给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

        示例 1:
            输入: nums = [-1,0,3,5,9,12], target = 9
            输出: 4
            解释: 9 出现在 nums 中并且下标为 4
        示例 2:
            输入: nums = [-1,0,3,5,9,12], target = 2
            输出: -1
            解释: 2 不存在 nums 中因此返回 -1

        提示：
            你可以假设 nums 中的所有元素是不重复的。
            n 将在 [1, 10000]之间。
            nums 的每个元素都将在 [-9999, 9999]之间。
        """
        idx = -1
        low = 0
        high = len(nums)
        while True:
            if low == high:
                break
            medium = int((high + low) / 2)
            if nums[medium] == target:
                idx = medium
                break
            elif nums[medium] > target:
                low = low
                high = medium
            else:
                low = medium + 1
                high = high
        return idx
        
    def question_27(self, nums: List[int], val: int) -> int:
        """
        给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

        假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

        更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
        返回 k。
        用户评测：
        评测机将使用以下代码测试您的解决方案：
            int[] nums = [...]; // 输入数组
            int val = ...; // 要移除的值
            int[] expectedNums = [...]; // 长度正确的预期答案。
                                        // 它以不等于 val 的值排序。

            int k = removeElement(nums, val); // 调用你的实现

            assert k == expectedNums.length;
            sort(nums, 0, k); // 排序 nums 的前 k 个元素
            for (int i = 0; i < actualLength; i++) {
                assert nums[i] == expectedNums[i];
            }
        如果所有的断言都通过，你的解决方案将会 通过。

        示例 1：
            输入：nums = [3,2,2,3], val = 3
            输出：2, nums = [2,2,_,_]
            解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
            你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
        示例 2：
            输入：nums = [0,1,2,2,3,0,4,2], val = 2
            输出：5, nums = [0,1,4,0,3,_,_,_]
            解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
            注意这五个元素可以任意顺序返回。
            你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
        
        提示：
            0 <= nums.length <= 100
            0 <= nums[i] <= 50
            0 <= val <= 100
        """
        # 官方解法一
        left = 0
        right = 0
        while right < len(nums):
            if val != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

        # 自己尝试
        # swap_idx = len(nums) - 1
        # idx = 0
        # while idx <= swap_idx:
        #     if val == nums[idx]:
        #         nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
        #         swap_idx -= 1
        #     else:
        #         idx += 1
        # return swap_idx + 1
        
    def question_977(self, nums: List[int]) -> List[int]:
        """
        给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

        示例 1：
            输入：nums = [-4,-1,0,3,10]
            输出：[0,1,9,16,100]
            解释：平方后，数组变为 [16,1,0,9,100]
            排序后，数组变为 [0,1,9,16,100]
        示例 2：
            输入：nums = [-7,-3,2,3,11]
            输出：[4,9,9,49,121]

        提示：
            1 <= nums.length <= 104
            -104 <= nums[i] <= 104
            nums 已按 非递减顺序 排序

        进阶：
            请你设计时间复杂度为 O(n) 的算法解决本问题
        """
        result = []
        for i in range(0, len(nums)):
            nn = nums[i] ** 2
            result.append(nn)
            result.insert
        return result
        
    
def test(question_number=0):
    q = Question(question_number)
    if 704 == question_number:
        nums = [-1,0,3,5,9,12]
        target = 2
        res = q.question_704(nums, target)
    elif 27 == question_number:
        nums = [-1,0,12,3,5,9,12]
        target = 12
        nums = [2, ]
        target = 3
        res = q.question_27(nums, target)
    elif 977 == question_number:
        nums = [-4,-1,0,3,10]
        res = q.question_977(nums)
    else:
        res = "Error question number"
    print(f"res: {res}")
    

if "__main__" == __name__:
    # test(704)
    # test(27)
    test(977)
