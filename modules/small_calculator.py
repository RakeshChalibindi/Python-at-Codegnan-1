# importing modules
# by imporing the file name

import addition
# importing  function from module
from subtraction import sub

# importing modules with alias name
import multiplication as MUL

# importing function with alis name
from division import div as DIVISION



print(addition.add(x=20,y=50))
print(sub(x=10,y=20))
print(MUL.mul(x=20,y=10))
print(DIVISION(10,5))