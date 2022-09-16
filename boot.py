import numpy as np
speed=[99,88,55,65,42,89,51,68,52,78,99,14]
x=np.mean(speed)
print(x)
# result 66.66666666666667

marks=[30,35,39,31,20,25,8,36,39,32,35,36]
y=np.percentile(marks,25)
print(y)
#result  28.75


# standard deviation
z=np.std(speed)
print(z)
# result 24.421074687427023