from algorithms.heap_sort import heap_sort

def kth_greatest(k,arr):
    #sorting the array
    heap_sort(arr)
    return arr[-k]