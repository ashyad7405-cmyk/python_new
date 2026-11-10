def tower_of_hanoi(n, source, destination, auxiliary):
    # Base case: if only 1 disk is left, move it directly
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary using destination as helper
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth disk from source to destination
    print(f"Move disk {n} from rod {source} to rod {destination}")
    
    # Step 3: Move the n-1 disks from auxiliary to destination using source as helper
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Test the function with 3 disks
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
