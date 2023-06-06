# Sorting Algorithms

!!! tip

    Check out this sorting algorithm visualizer: [https://visualgo.net/en/sorting](https://visualgo.net/en/sorting){target=_blank}

## Insertion Sort

!!! info

    Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. [^1]

```python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
```

```python
array = [5, 2, 4, 6, 1, 3]
insertion_sort(array)

print(array)

# Output:
# >>> [1, 2, 3, 4, 5, 6]
```

## Quick Sort

!!! info

    Quicksort is an efficient sorting algorithm. It is a divide and conquer algorithm. [^2]

```python
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
```

```python
array = [5, 2, 4, 6, 1, 3]
quick_sort(array, 0, len(array) - 1)
print(array)

# Output:
# >>> [1, 2, 3, 4, 5, 6]
```

## Divide & Conquer

!!! info

    Divide and conquer is an algorithm design paradigm based on multi-branched recursion. A divide-and-conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. Then the solutions of the sub-problems can be combined to solve the original problem. [^3]

[^1]: [https://www.programiz.com/dsa/insertion-sort](https://www.programiz.com/dsa/insertion-sort){target=\_blank}
[^2]: [https://www.geeksforgeeks.org/python-program-for-quicksort/](https://www.geeksforgeeks.org/python-program-for-quicksort/){target=\_blank}
[^3]: [https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm){target=\_blank}
