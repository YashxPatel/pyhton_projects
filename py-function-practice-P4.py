# 1
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

num1 = (25)
num2 = (3)
num3 = (2000)

maximum = max_num(num1, num2, num3)

# 2
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

list1 = [2, 3, 4, 5]
print("Result 1:", mult_list(list1))

# 3
def rev_string(string):
    return string[::-1]

input_string = input("Enter a string: ")
print("Reversed string:", rev_string(input_string))

# 4
def num_within(number, start, end):
    return start <= number <= end

# Example usage of the function
num = (6)
start = (1)
end = (6)

within_range = num_within(num, start, end)
if within_range:
    print("True.")
else:
    print("False")

# 5


