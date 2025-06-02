

### 🐍 `program.py`


# Brute Force Solution - O(n^2)
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Optimized Solution using Set - O(n)
class SolutionOptimized:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Test
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    sol = SolutionOptimized()
    print(sol.hasDuplicate(nums))  # Output: True
