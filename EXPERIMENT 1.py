import time
import random

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if arr[high] == arr[low]:
            if arr[low] == target:
                return low, comparisons
            else:
                return -1, comparisons

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comp':>12} {'BS Comp':>12}")
    print("-" * 68)

    for size in sizes:
        arr = list(range(10, size * 10 + 10, 10))
        target = arr[size // 2]

        start = time.perf_counter()
        for _ in range(100):
            _, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            _, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>12} {comp_bs:>12}")


arr = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
target = 64

index, comparisons = interpolation_search(arr, target)

print("Array:", arr)
print("Searching for:", target)
print("Found at index:", index)
print("Comparisons:", comparisons)
print()
performance_analysis()



""""
SAMPLE OUTPUT:

Array: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
Searching for: 64
Found at index: 7
Comparisons: 1

      Size   IS Time(ms)   BS Time(ms)      IS Comp      BS Comp
--------------------------------------------------------------------
      1000        0.0019        0.0034            1           10
      5000        0.0022        0.0040            1           13
     10000        0.0025        0.0045            1           14
     50000        0.0029        0.0058            1           16
    100000        0.0033        0.0065            1           17
    
"""
