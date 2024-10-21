# NOTES

## Complexity Analysis & Optimization
- it's a way of determining how input size affect the performance of the program, in terms of time and space
- maths formulas can play a large role in reducing the complexity, the hard thing is that, what kind of formula

**Example 1**: to calculate the sum from 1 to n, we can use a for-loop like this
```
def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
# the complexity will be O(n)
```
but if we know a math formula to calculate the sum of n terms:
```
def sum_numbers(n):
    return n * (n+1) / 2
# the complexity will be O(1)
```

**Example 2:** check for duplicates in a list, we can use 2 for-loops
```
def contains_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
# complexity = O(n^2)
```
but if we sort the list first then compare adjacent values only, we will need only 1 for-loop, it will be better, even if the complexity of python sort() is O(nlogn), it's still better than O(n^2)
```
def contains_duplicate(lst):
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            return True
    return False
# complexity = O(nlogn)
```

## Set Methods
- based on discrete maths
- using set methods are really fast, good for optimization
- to initialize a set: ```unique = set()```
- to add element in a set: ```unique.add(2)```
- before apply the set methods below, make sure to convert the data to set type first by doing ```set()```
1. Intersection (```&```):
```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1 & set2
print(union_set)  # prints: {3, 4}
```
2. Union (```|```):
```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1 | set2
print(union_set)  # prints: {1, 2, 3, 4, 5, 6}
```
3. Difference (```-```):
```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff_set = set1 - set2
print(diff_set)  # prints: {1, 2}
```
4. Symmetric Difference (```^```):
```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sym_diff_set = set1 ^ set2
print(sym_diff_set)  # prints: {1, 2, 5, 6}
# output elements that only reside in one of the sets, not both
```
5. Subset (```<=```):
```
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1 <= set2)  
# prints: True, cause set1 is a subset of set 2
```