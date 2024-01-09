import cupy as cp

# Define the arrays
array1 = []
array2 = []
for i in range(0, 10):
    for j in range(0, 10):
        array2.append(i * j)
    array1.append(array2)

array3 = []
array4 = []
for i in range(0, 10):
    for j in range(0, 10):
        array4.append(i * j)
    array3.append(array4)

# Convert lists to Cupy arrays
array1_gpu = cp.asarray(array1)
array3_gpu = cp.asarray(array3)

# Reshape the arrays to 1D for dot product
array1_1d = array1_gpu.reshape(-1)
array3_1d = array3_gpu.reshape(-1)

# Calculate the dot product on the GPU
dot_product_gpu = cp.dot(array1_1d, array3_1d)

# Transfer the result back to the CPU if needed
dot_product_cpu = cp.asnumpy(dot_product_gpu)

print(dot_product_cpu)
