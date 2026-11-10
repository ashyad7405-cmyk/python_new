def permute(a, l, r):
    # Base case: when the starting index equals the ending index
    if l == r:
        print("".join(a))
    else:
        for i in range(l, r + 1):
            # Swap the current index with the first index
            a[l], a[i] = a[i], a[l]
            # Recursively call for the remaining substring
            permute(a, l + 1, r)
            # Backtrack (undo the swap) to restore the original array
            a[l], a[i] = a[i], a[l]

# Test the function
string = input("enter a string")
n = len(string)
permute(list(string), 0, n - 1)
