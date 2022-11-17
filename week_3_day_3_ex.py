# Exercise 1
# Filter out all of the empty strings from the list below

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def filter_s(places):
    if places.strip():
        return True
    else:
        return False

new_list = list(filter(filter_s, places))
print(new_list)


# places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

# print(list(filter(lambda place: True if place != " " else False, places)))

# places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

# def filter_space(places):
#     no_space = []
#     for place in places:
#         if place[0] != " ":
#             no_space.append(place)
#         return no_space
    
# print(filter_space(places))
# print(list(filter(lambda x : x != "", places)))


# Exercise 2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def sort_author(author):
    author.sort(key = lambda x : x.split(" ")[-1].lower())
    return author
print(sort_author(author))


# Exercise 3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

print(list(map(lambda x : (x[0], (9/5) * x[1] + 32), places)))

# Exercise 4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# def recursive_fib_s(num):
#     if num <= 1:
#         print(f'Iteration({num}) = 1')
#         return num
#     return recursive_fib_s(num - 1) + recursive_fib_s(num - 2)

# print(recursive_fib_s(5))


def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))