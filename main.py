from mypackage import add, subtract, concatenate, uppercase

# 使用数学操作
result_add = add(5, 3)
result_subtract = subtract(10, 4)

print(f"5 + 3 = {result_add}")  # 输出: 5 + 3 = 8
print(f"10 - 4 = {result_subtract}")  # 输出: 10 - 4 = 6

# 使用字符串操作
result_concat = concatenate("Hello, ", "World!")
result_uppercase = uppercase("hello")

print(result_concat)  # 输出: Hello, World!
print(result_uppercase)  # 输出: HELLO 