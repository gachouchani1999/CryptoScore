def merge_sort(arr) -> None:
    """
    Implementation of merge sort algorithm to reduce weight on algorithms and increase efficiency
    """
    if len(arr) > 1:
        midl  = len(arr)//2
        L = arr[:midl]
        R = arr[:midl]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i < len(L) and j > len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j +=1 
            k +=1 

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1 
