# def say_hello(name):
#     print('Hello, {}'.format(name))
#     say_hello(name)

# say_hello("Alpha")

# def countdown(num):
#     if num == 0:
#         print('blast off')
#         return

#         # recurssive step here
#     print(num)
#     countdown(num - 1)

# countdown(10)

# handles edge case for negative number

# def countdown(num):
#     if num == 0:
#         print('blast off')
#         return
#     elif num < 0:
#         print('please input positive number')
#         return

#     print(num)
#     countdown(num-1)

# countdown(100)
# countdown(-10)

numbers = [1, 2, 3, 4, 5]
def add_number(num_array, result=0):
  num_pop = num_array.pop()
  result += num_pop
  # base case
  if len(num_array) == 0:
    print('RESULT : ', result)
    return result
  # recursive step
  return add_number(num_array, result)
print(add_number(numbers))