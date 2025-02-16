#1.
# class IterableGenerator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    
#     def __iter__(self):
#         def gen():
#             current = self.start
#             while current <= self.end:
#                 yield current
#                 current += 1
#         return gen()
# iterable_obj = IterableGenerator(1, 5)

# for number in iterable_obj:
#     print(number)

#2.
def safe_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Error occurred: {e}"

    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

print(calculate("2 + 3"))
print(calculate("10 / 0"))  
print(calculate("invalid_expression"))  
