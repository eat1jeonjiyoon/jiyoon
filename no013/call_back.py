# def callback(num):
#     # global count
#     num -= 1
#     if num == 0:
#         print("Count reached zero. Stopping execution.")
#         return
#     print("Callback function executed. count", num)
#     callback(num)
#     print("Callback function executed. count", num)
# callback(3)



# 1에서 10까지 더하기
# def add_numbers(num):
#     if num <= 1:
#         return 1
#     else:
#         return num + add_numbers(num - 1)
#     print(add_numbers(900))

# def add_numbers(start, end):
#     if end <= start:
#         return 1
#     return end + add_numbers(start, end - 1)
# print(add_numbers(1, 10))



# def add_numbers(start, end):
#     foo = ((start + end) * end) / 2
#     print("foo:", foo)
# add_numbers(1, 100000)



# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# def factorial(n):
#     if n <= 1:
#         print("n:", n)
#         return 1
#     print("n:", n)
#     foo = factorial(n - 1)
#     print("n:", n)
#     return n * foo
# print(factorial(5))



# def countdown(n):
#     if n <= 0:
#         print("발사!!!")
#         return
#     print(n)
#     countdown(n - 1)
# countdown(5)

# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i)
#     print("발사!!!")
# countdown(5)



# def print_start(n):
#     if n <= 0:
#         return
#     print("*" * n) #역삼각형
#     print_start(n - 1)
#     print("*" * n) #삼각형
# print_start(5)



# def gugu(dan, num):
#     num = 1
#     if num > 9:
#         return
#     print(f"{dan} * {num} = {dan * num}")
#     gugu(dan, num + 1)
# gugu(2)

# def multiplication_table():
#     for i in range(1, 10):
#         for j in range(1, 10):
#             print(f"{i} x {j} = {i * j:2}")
#         print()

# multiplication_table()



def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 4))