def find_the_winner(n, k):
    def josephus(n, k):
        if n == 1:
            return 0
        else:
            return (josephus(n - 1, k) + k) % n
    
    # Convert the zero-based result to one-based
    return josephus(n, k) + 1

# Example usage:
n = 5
k = 2
print(find_the_winner(n, k))  # Output should be 3
