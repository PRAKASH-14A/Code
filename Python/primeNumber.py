def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # Inefficient loop (should check only up to √n)
        if n % i == 0:
            return False
    return True

print(is_prime(997))  # Works but is very slow for large numbers
