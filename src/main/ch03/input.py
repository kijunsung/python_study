# a = int(input("a입력: "))
# b = int(input("b입력: "))
#
# print(a, b)
# print(type(a))
# print(type(b))

# "10 20"
number = input("두 수 입력: ").split()
print(number)

number1, number2 = list(map(int, input("두 수 입력: ").split()))

print(type(number1))
print(number2)
