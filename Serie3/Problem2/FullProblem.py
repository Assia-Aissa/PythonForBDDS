# Function to calculate the nth Fibonacci number
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# Function to generate all Fibonacci numbers less than n
def SuiteFibo(n):
    fibo_list = []  # List to store Fibonacci numbers
    i = 1
    while True:
        numb = fibo(i)
        if numb >= n:
            break
        fibo_list.append(numb)
        i += 1
    return fibo_list

# Function to encode a number n using Fibonacci numbers
def coder(n):
    fibo_list = SuiteFibo(n)  # Get Fibonacci numbers less than n
    binary_representation = [0] * len(fibo_list)  # Initialize binary representation

    # Encode n as a sum of Fibonacci numbers
    for i in range(len(fibo_list) - 1, -1, -1):  # Iterate from largest to smallest Fibonacci
        if fibo_list[i] <= n:
            binary_representation[i] = 1  # Mark as used
            n -= fibo_list[i]  # Reduce n by the Fibonacci number

    return [fibo_list, binary_representation]

# Function to decode a Fibonacci binary representation back to a number
def decoder(fibo_binary):
    fibo_list, binary_representation = fibo_binary  # Extract Fibonacci numbers and binary code
    decoded_number = 0

    # Sum Fibonacci numbers where the binary code is 1
    for i in range(len(binary_representation)):
        if binary_representation[i] == 1:
            decoded_number += fibo_list[i]

    return decoded_number

# Example usage
n = 10
encoded = coder(n)
print(f"Encoded {n} as: {encoded}")

decoded = decoder(encoded)
print(f"Decoded back to: {decoded}")
