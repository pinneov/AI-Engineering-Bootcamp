print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)

empty_value = None

print(empty_value == None)  # Compares values: True, but not preferred - can be tricked by __eq__() implementation of the object
print(empty_value is None)  # Compares references: True, preferred - is indicates that they are pointing at the same instance and None is singleton so there is only ever one instance of None

empty_value = 10

print(empty_value == None)      # False
print(empty_value is None)      # False
