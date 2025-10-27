from create_array import create_numerical_array
from find_in_list import find_x, find_x_2

array_400 = create_numerical_array(400)
array_10 = create_numerical_array(10)

print(array_400)

x = array_400[6]

print(x)

find_x(array_400, 69)

find_x_2(array_400, 30)

array_401 = array_400.copy()

array_401.append(401)

print(array_401)

array_15 = array_10.copy()

array_15.extend([11, 12, 13, 14, 15])

print(array_15)