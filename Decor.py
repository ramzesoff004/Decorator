import time


def log_function_calls(func):
    def wrapper(*args, **kwargs):
        print(f'Calling multiply_numbers with args: {args}, kwargs: {kwargs}')
        print(f'{func.__name__} returned {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return wrapper


# @log_function_calls
# def multiply_numbers(x, y):
#     return x * y
# result = multiply_numbers(10, 20)
# print("Result:", result)


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took seconds to {end_time - start_time} execute')
        return result
    return wrapper


# @measure_execution_time
# def calculate_multiply(numbers):
#     tot = 1
#     for x in numbers:
#         tot *= x
#     return tot
#
# res = calculate_multiply([1, 2, 3, 4, 5])
# print("Result:", res)


class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in self.cache:
            result = self.func(*args, **kwargs)
            self.cache[key] = result
            return result

        else:
            print('Retrieving result from cache...')
            return self.cache[key]


# @CacheResult
# def calculate_multiply(x, y):
#     print("Calculating the product of two numbers...")
#     return x * y
#
# print(calculate_multiply(4, 5))
# print(calculate_multiply(4, 5))
# print(calculate_multiply(5, 7))
# print(calculate_multiply(5, 7))


class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.call_times = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            self.call_times = [item for item in self.call_times if current_time - item < self.period]
            if len(self.call_times) < self.max_calls:
                self.call_times.append(current_time)
                return func(*args, **kwargs)
            else:
                print('Error occurred: Rate limit exceeded. Please try again later.')
        return wrapper


# @RateLimiter(max_calls=6, period=10)
# def api_call():
#     print("API call executed successfully...")
#
# for _ in range(8):
#     try:
#         api_call()
#     except Exception as e:
#         print(f"Error occurred: {e}")
# time.sleep(10)
# api_call()

