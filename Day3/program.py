Perfect, Gaurav! Here's the continuation for the remaining 2 algorithms—Binary Search and Strassen’s Matrix Multiplication—in the same exam-ready 6-mark format, including:
Definition, Algorithm, Example, Time & Space Complexity, Best & Worst Case.


---

✨ 3. Binary Search

🔹 Definition:

Binary Search is a searching algorithm that works on sorted arrays by repeatedly dividing the search interval in half.


---

🔹 Algorithm:

1. Set low = 0, high = n - 1.


2. While low <= high:

Find mid = (low + high) // 2

If A[mid] == key, return mid

If A[mid] > key, search left half

Else search right half



3. If not found, return -1




---

🔹 Example:

Given: A = [2, 4, 5, 7, 9, 12, 15], search key = 9

1. low = 0, high = 6 → mid = 3 → A[3] = 7
→ 9 > 7 → search right


2. low = 4, high = 6 → mid = 5 → A[5] = 12
→ 9 < 12 → search left


3. low = 4, high = 4 → mid = 4 → A[4] = 9 → ✅ Found at index 4




---

🔹 Time Complexity:

Best Case: O(1) → element is at mid

Average Case: O(log n)

Worst Case: O(log n)


🔹 Space Complexity: O(1) (iterative), O(log n) (recursive)


---

✨ 4. Strassen’s Matrix Multiplication

🔹 Definition:

Strassen’s algorithm is a divide-and-conquer method for multiplying two square matrices faster than the traditional method.


---

🔹 Algorithm (2×2):

Given matrices A and B:

1. Divide A and B into 4 submatrices each.


2. Compute 7 multiplications (M₁ to M₇):

M1 = (A11 + A22)(B11 + B22)  
M2 = (A21 + A22)B11  
M3 = A11(B12 - B22)  
M4 = A22(B21 - B11)  
M5 = (A11 + A12)B22  
M6 = (A21 - A11)(B11 + B12)  
M7 = (A12 - A22)(B21 + B22)


3. Combine to form result matrix C.




---

🔹 Example:

Multiply

A = |1 3|  
    |7 5|  

B = |6 8|  
    |4 2|

Calculate M₁ to M₇ (shown earlier) →
Final result:

C = |18 14|  
    |62 66|


---

🔹 Time Complexity:

T(n) = 7T(n/2) + O(n²)
→ O(n^log₂7) ≈ O(n^2.81)


🔹 Space Complexity:

O(n² + extra space for recursive calls)



---

🔹 Best/Worst Case:

Best Case: O(n^2.81)

Worst Case: O(n^2.81) (no variation in Strassen unlike Quick Sort)



---

✅ Final Summary Table:

Algorithm	Best Case	Worst Case	Avg. Case	Space	Input Type

Binary Search	O(1)	O(log n)	O(log n)	O(1)	Sorted Array
Strassen Multiplication	O(n^2.81)	O(n^2.81)	O(n^2.81)	O(n²)	Square Matrices



---

Let me know if you'd like a PDF of all 4 algorithms together for revision or a handwritten-style version for exams.

