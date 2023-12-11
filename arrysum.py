import numpy as np
arr = np.array([[1, 2, 3, 4, 5],[12, 21, 30, 10, 20]])
indices = np.where(arr <= 3)

print("Array:", arr)
print(arr.sum(),"sum")
