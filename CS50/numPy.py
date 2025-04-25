# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Check the output when we add two list
print(baseball+baseball)

# Check the output when we add two numpy arrays
print(np_baseball+np_baseball)