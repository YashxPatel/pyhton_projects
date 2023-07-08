#1

def arb_args(*args):
    for arg in args:
        print(arg)

arb_args("apple", "banana", "cherry")

#2
def inner_func(num1, num2):
    def multiply(x, y):
        return x * y

    def add(x, y):
        return x + y

    result_multiply = multiply(num1, num2)
    result_add = add(num1, num2)
    total = result_multiply + result_add

    print("Result of multiplication:", result_multiply)
    print("Result of addition:", result_add)
    print("Total:", total)

inner_func(3, 4)

#3
def lunch_lady(student_name, lunch_preference="Mystery Meat"):
    print(student_name, lunch_preference)
    # print("Lunch Preference:", lunch_preference)

lunch_lady("Yash Patel,", "Pizza")
lunch_lady("John Doe,")

#4 
def sum_n_product(num1, num2):
    sum_result = num1 + num2
    product_result = num1 * num2
    return sum_result, product_result

result_sum, result_product = sum_n_product(3, 4)
print("Sum:", result_sum)
print("Product:", result_product)

#5
alias_arb_args = arb_args

#6
def arb_mean(*args):
    total = 0
    for a in args:
        total += a
        print(a/len(args))

arb_mean(4, 7, 9, 2)
arb_mean(10, 20, 30, 40, 50)
arb_mean()

#7
def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            longest = a
    return longest

result = arb_longest_string("apple", "banana", "cherry")
print("Longest string:", result)

result = arb_longest_string("Hello", "World", "Python")
print("Longest string:", result)

result = arb_longest_string()
print("Longest string:", result)


