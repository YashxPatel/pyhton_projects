#1
def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

name_args(name="John", age=25, city="New York")

# -------------------------------------------------------------

#2
def all_true(iterable):
    return all(iterable)

list1 = [True, True, True]
result1 = all_true(list1)
print(result1)  # Output: True

# list2 = [True, False, True]
# result2 = all_true(list2)
# print(result2)  # Output: False

# -------------------------------------------------------------

#3
def one_true(iterable):
    return any(iterable)

list1 = [False, False, True]
result1 = one_true(list1)
print(result1)  # Output: True

# list2 = [False, False, False]
# result2 = one_true(list2)
# print(result2)  # Output: False

# -------------------------------------------------------------

#4
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
result = recursive_factorial(number)
print(f"The factorial of {number} is:", result)

# -------------------------------------------------------------

#5
def recursive_deduplicate(string):
    if len(string) < 2:
        return string
    elif string[0] == string[1]:
        return recursive_deduplicate(string[1:])
    else:
        return string[0] + recursive_deduplicate(string[1:])

input_string = input("Enter a string: ")
result = recursive_deduplicate(input_string)
print("After deduplication:", result)

