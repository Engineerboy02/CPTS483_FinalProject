# main.py
import Test

name = "World"
message = Test.greet(name)
print(message)  # Output: Hello, World!

num1 = 5
num2 = 5
sum_result = Test.add(num1, num2)
print(sum_result)  # Output: 8

Test.timedelay()

print("main script print")