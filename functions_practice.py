def hello():
    print("Hello, user!")

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]

result = pack("blackberry", 69, True)
print(result)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for item in food_list[1:]:
            print("Next I eat", item)

eat_lunch(["sandwich", "fruit", "chips", "juice"])