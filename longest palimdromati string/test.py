import numpy as np

def outer_product_2d(arr1, arr2):
  result = [[0 for _ in range(len(arr1) + 1)] for _ in range(len(arr2) + 1)]
  
  for i in range(1,len(arr1) + 1):
    result[0][i] = arr1[i - 1]
    result[i][0] = arr2[i - 1]
    for j in range(1, len(arr2) + 1):
      result[i][j] = arr1[i - 1] + arr2[j - 1]

  # Use np.outer for efficient outer product calculation
  return result

# Example usage
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

result = outer_product_2d(arr1, arr2)

print(result)