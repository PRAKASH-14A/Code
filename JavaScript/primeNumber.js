function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i < n; i++) {  // Should only check up to sqrt(n)
        if (n % i === 0) return false;
    }
    return true;
}

console.log(isPrime(997));  // Works but inefficient for large numbers
