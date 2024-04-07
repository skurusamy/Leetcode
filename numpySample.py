import numpy as np;
a = np.random.uniform(size=(3,2))
print(a)
b = a/a[1,:] #each element is divided by the element in second row of corresponding coliumn
print("B")
print(b)