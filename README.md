# Redmi – Quick Revision Notes: Contains Duplicate

📅 **Started solving LeetCode Top 150 Problems on June 1**

---

## 📌 Problem
Check if an integer array has **any duplicate** values.

---

## ✅ Approaches

### 1. Brute Force (Nested Loops)
- Compare every pair: `nums[i] == nums[j]`
- **Time**: O(n²)
- **Space**: O(1)
- ✅ Easy to implement
- ❌ Not efficient for large input

### 2. Using Set (Best)
- Use a hash set to track seen elements
- If `num in set`, return True
- **Time**: O(n)
- **Space**: O(n)
- ✅ Clean & fast

---

## 🧪 Sample Input/Output

```python
Input: [1, 2, 3, 4]
Output: False

Input: [1, 2, 3, 1]
Output: True
