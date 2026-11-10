def is_palindrome(s):
    
    # Base case: 0 or 1 character left
    if len(s) <= 1:
        return True
    # Check if outer characters match
    if s[0] == s[-1]:
        # Recursive step: check the inner substring
        return is_palindrome(s[1:-1])
    else:
        return False
# Read input from the user, normalize by removing non-alphanumeric
# characters and converting to lowercase, then check palindrome.
raw = input("Enter the string: ")
print(is_palindrome(raw))



