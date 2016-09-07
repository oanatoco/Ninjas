import math

num_paths = math.factorial(40)/math.factorial(20)
print(num_paths)

num_paths2 = 1
for i in range(21,41):
    num_paths2 = num_paths2*i
print(num_paths2)
num_paths3=num_paths2/(math.factorial(20))
print(num_paths3)

