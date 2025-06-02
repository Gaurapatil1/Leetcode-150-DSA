# Day 1 Notes - Contains Duplicate

## 🔍 Problem Statement
Given an integer array `nums`, return `true` if any value appears more than once in the array, and return `false` if every element is distinct.

---

## ✅ Example
```python
Input: nums = [1,2,3,4]
Output: False

Input: nums = [1,2,3,1]
Output: True

🧠 Approaches to Solve
✅ Brute Force (Nested Loops)
Idea: Compare every element with every other element.

Time Complexity: O(n²)

Space Complexity: O(1)

✅ Easy to understand, but inefficient for large inputs.

✅ Hash Set (Efficient Approach)
Idea: Use a set to track elements seen so far.

If we find a number already in the set, return True.

Time Complexity: O(n)

Space Complexity: O(n)

⚡ Much faster and cleaner.

