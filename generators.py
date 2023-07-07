"""
really useful for working with really large datasets
"""

def my_range(start, stop, step):
    while start < stop:
        yield start
        start += step
        
a_range = my_range(0, 20, 2)

print(a_range)

# for num in a_range:
#     print(num)
    
# print(list(a_range))

print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))
print(next(a_range))