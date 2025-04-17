# 🔁 Day-5: Next Permutation

This repository contains a Python implementation to compute the **next lexicographically greater permutation** of a given list of numbers. This is part of the **GeeksforGeeks 160 Days DSA Challenge**.

---

## 📌 Problem Statement

Given an array of integers representing a permutation, rearrange the numbers into the **next lexicographically greater permutation** of numbers. If such an arrangement is not possible, it must be rearranged as the lowest possible order (i.e., sorted in ascending order).

---

## 🧠 Approach & Intuition

To compute the next permutation efficiently in **O(n)** time:

1. **Traverse from the end** to find the first decreasing element `arr[i]` such that `arr[i] < arr[i+1]`.
2. **If such an element is found**, again traverse from the end and find the first element `arr[j] > arr[i]`.
3. **Swap** `arr[i]` and `arr[j]`.
4. **Reverse** the sub-array from `i+1` to the end to get the next permutation.

> If no such `i` is found, the array is in descending order. In that case, reversing the whole array gives the lowest permutation.

---

## ▶️ Sample Input & Output
```
arr = [3, 2, 1]
 Output:
 Original: [3, 2, 1]
 Next Permutation: [1, 2, 3]
```
---
## ✅ Time & Space Complexity
1. Time Complexity: O(n)

2. Space Complexity: O(1) (in-place)
---
## 📅 Challenge Tag
#gfg160 #geekstreak2025 #Day5
---
## 🙌 Contribution
This implementation is part of a DSA Daily Challenge series created by Vikash Joshi, designed to strengthen algorithmic thinking and problem-solving.

Feel free to ⭐ the repository if you find it helpful!
