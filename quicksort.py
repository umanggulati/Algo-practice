def quicksort(x):
    if len(x) < 2:
        return x

    else:
        pivot = x[0]

        low = [i for i in x[1:] if i <= pivot]

        high = [i for i in x[1:] if i > pivot]

        
        return quicksort(low) + [pivot] + quicksort(high)
print(quicksort([10, 5, 2, 3]))
