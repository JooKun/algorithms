def max_heapify(arr,n,i):
    
    left = 2*i + 1
    right = 2*i + 2
    
    max_root = i
    
    if left < n and arr[max_root] < arr[left]:
        max_root = left
    if right < n and arr[max_root] < arr[right]:
        max_root = right
    if max_root != i:
        arr[max_root], arr[i] = arr[i], arr[max_root]
        max_heapify(arr,n,max_root)
        
def heap_sort(arr):
    n = len(arr)
    for i in range (n, -1, -1):
        max_heapify(arr, n, i)
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        max_heapify(arr, i, 0) 