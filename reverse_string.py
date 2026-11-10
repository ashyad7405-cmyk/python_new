def reverse_string(s):
    
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])



user_input = input("Enter a string: ")
print(reverse_string(user_input))