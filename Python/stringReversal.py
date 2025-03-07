def reverse_string(s):
    """Inefficient string reversal using manual loops"""
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):  # Iterates character by character
        reversed_str += s[i]  # String concatenation in loop (O(n²) complexity)

    return reversed_str

text = "This is an inefficient string reversal"
print(reverse_string(text))
