import argparse
import random
import time

# Script Metadata
__author__ = 'Cliff'
__version__ = '1.1'

# Enhanced Merge Sort Implementation with Verbose Option and Step Count

def merge_sort(arr, verbose=False, count_steps=False):
    step_count = 0

    def merge_sort_inner(arr):
        nonlocal step_count
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            step_count += 1  # Increment for division step

            if verbose:
                print(f"Dividing: {arr} into\n  Left: {L}\n  Right: {R}")

            merge_sort_inner(L)
            merge_sort_inner(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                step_count += 1  # Increment for each comparison
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                step_count += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                step_count += 1

            if verbose:
                print(f"Merging: {arr}")

        return arr

    sorted_array = merge_sort_inner(arr)
    if verbose:
        print("Sorted Array:", sorted_array)

    if count_steps:
        print(f"Merge Sort Steps: {step_count}")
    if verbose:
        print("Merge Sort is stable and not in-place. Space Complexity: O(n)")
    return sorted_array

# Enhanced Quick Sort Implementation with Verbose Option and Step Count
def quick_sort(arr, verbose=False, count_steps=False):
    step_count = 0

    def quick_sort_inner(arr):
        nonlocal step_count
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left, right = [], []
            for x in arr:
                if x != pivot:  # Counting comparison
                    step_count += 1
                if x < pivot:
                    left.append(x)
                elif x > pivot:
                    right.append(x)

            if verbose:
                print("Pivot:", pivot)
                print("Left:", left, "Right:", right)

            return quick_sort_inner(left) + [pivot] + quick_sort_inner(right)

    sorted_array = quick_sort_inner(arr)
    if verbose:
        print("Sorted Array:", sorted_array)

    if count_steps:
        print(f"Quick Sort Steps: {step_count}")
    if verbose:
        print("Quick Sort is not stable but in-place. Space Complexity: O(log n)")
    return sorted_array

# Enhanced Heap Sort Implementation with Verbose Option and Step Count

def heap_sort(arr, verbose=False, count_steps=False):
    step_count = 0

    def heapify(arr, n, i):
        nonlocal step_count
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
            step_count += 1

        if r < n and arr[largest] < arr[r]:
            largest = r
            step_count += 1

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
            step_count += 1

        if verbose:
            print(f"Heapify called on index {i}, heap: {arr[:n]}")

    n = len(arr)

    # Building the heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extracting elements from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    # Print the sorted array if verbose mode is enabled
    if verbose:
        print("Sorted Array:", arr)

    if count_steps:
        print(f"Heap Sort Steps: {step_count}")
    if verbose:
        print("Heap Sort is not stable but in-place. Space Complexity: O(1)")
    return arr

def read_data(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def run_sorting_algorithm(algorithm, data, verbose, count_steps):
    start_time = time.time()
    data_point_count = len(data)
    print(f"Running {algorithm} sort on {data_point_count} data points...")

    if algorithm == 'merge':
        sorted_data = merge_sort(data.copy(), verbose=verbose, count_steps=count_steps)
    elif algorithm == 'quick':
        sorted_data = quick_sort(data.copy(), verbose=verbose, count_steps=count_steps)
    elif algorithm == 'heap':
        sorted_data = heap_sort(data.copy(), verbose=verbose, count_steps=count_steps)

    elapsed_time = time.time() - start_time
    return sorted_data, elapsed_time


def main():
    # ASCII Banner for "IFQ664 algorithms"
    ascii_banner = """
    *************************
    *** IFQ664 Algorithms ***
    *************************
    """
    print(ascii_banner)

    parser = argparse.ArgumentParser(
        description='IFQ664 Algorithms Script: Implements various sorting algorithms with additional functionality for educational purposes.',
        epilog=f'Author: {__author__}\nVersion: {__version__}\nThis script is instructional for IFQ664.',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('-f', '--file', required=True, help='Input file containing data to sort')
    parser.add_argument('-a', '--algorithm', choices=['merge', 'quick', 'heap', 'all'], required=True, help='Sorting algorithm to use')
    parser.add_argument('-i', '--instruct', action='store_true', help='Enable instructional output for sorting algorithms')

    args = parser.parse_args()

    data = read_data(args.file)

    if args.algorithm == 'all':
        for algorithm in ['merge', 'quick', 'heap']:
            print(f"Running {algorithm} sort...")
            _, time_taken = run_sorting_algorithm(algorithm, data, args.instruct, count_steps=True)
            print(f"{algorithm.capitalize()} Sort Time: {time_taken:.5f} seconds\n")
    else:
        _, time_taken = run_sorting_algorithm(args.algorithm, data, args.instruct, count_steps=True)
        print(f"{args.algorithm.capitalize()} Sort Time: {time_taken:.5f} seconds")



if __name__ == "__main__":
    main()
