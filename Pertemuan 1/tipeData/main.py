# Tipe data di Python

# Integer (bilangan bulat)
data_integer = 1
print("data:", data_integer, ", bertipe :", type(data_integer))

# Float (bilangan real)
data_float  = 1.5
print("data:", data_float, ", bertipe :", type(data_float))

# String (karakter)
data_string = "fauzan abrar 2"
print("data:", data_string, ", bertipe :", type(data_string))

# Boolean (true atau false)
data_bool   = True
print("data:", data_bool, ", bertipe :", type(data_bool))


# Tipe data khusus

# Complex (bilangan kompleks)
data_complex = complex(5,6)
print("data:", data_complex, ", bertipe :", type(data_complex))


# Tipe data dari bahasa C bisa dipakai di Python
from ctypes import c_double

data_c_double = c_double(10.5)
print("data:", data_c_double, ", bertipe :", type(data_c_double))