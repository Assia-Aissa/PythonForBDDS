def AfficheSousSequences(T):
    first = []           # List to hold all increasing subsequences
    current = []         # List for the current increasing subsequence

    for i in range(len(T)):
        # If current is empty or T[i] is greater than the last element in current
        if not current or T[i] > current[-1]:
            current.append(T[i])  # Add T[i] to the current subsequence
        else:
            # If we encounter a break in the sequence
            if current:
                first.append(current)  # Save the current subsequence to first
            current = [T[i]]  # Start a new current subsequence with T[i]

    # If there is a current subsequence left, add it to first
    if current:
        first.append(current)

    # Print the subsequences in the required format
    for seq in first:
        result = '<' + ', '.join(str(num) for num in seq) + '>'
        print(result)

# Example usage
T = [1, 2, 5, 3, 12, 25, 13, 8, 4, 7, 24, 28, 32, 11, 14]
AfficheSousSequences(T)
