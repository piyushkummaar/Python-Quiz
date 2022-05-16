# sum 1+2+1  = 4
# prd 1*2*1 = 2
# def sum_fun(num = 1314):
#     num_sum = 0 
#     for i in str(num):
#         num_sum = num_sum + int(i)  
#     return num_sum

# def pro_fun(num = 1314):
#     num_sum = 1
#     for i in str(num):
#         num_sum = num_sum * int(i)  
#     return num_sum

# print(abs(sum_fun() - pro_fun()))

import numpy as np
num = 1314
sum_fun = sum([int(i)  for i in str(num)])
pro_fun = np.prod([int(i)  for i in str(num)])
print(abs(sum_fun - pro_fun))



