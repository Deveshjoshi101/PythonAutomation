### **Day 9: Error Handling & Optimization**

**Objective**: Make automation scripts robust and efficient.

**Topics Covered:**

1. **Types of errors: syntax, runtime, and logical**:

   - **Syntax errors** occur when the code has incorrect syntax. They are typically due to misplaced punctuation marks or incorrect keywords.
   - **Runtime errors** happen during the execution of a program. These errors may not be evident until a certain operation is attempted, such as dividing by zero.
   - **Logical errors** are mistakes in the program's logic. These don’t raise exceptions but may produce incorrect results.

   **Examples**:

   - **Syntax error**:

     ```python
     # Syntax error example: missing a closing parenthesis
     def add_numbers(a, b
         return a + b
     ```

   - **Runtime error**:

     ```python
     # Runtime error example: dividing by zero
     result = 10 / 0  # This will raise a ZeroDivisionError
     ```

   - **Logical error**:

     ```python
     # Logical error: incorrect condition
     def check_number(number):
         if number == 5:
             return "Number is 5"
         else:
             return "Number is not 5"

     print(check_number(5))  # Incorrectly returns "Number is not 5"
     ```

2. **Using `try`, `except`, and `finally` for error handling**:

   - `try`: Contains the code that may cause an exception.
   - `except`: Specifies what to do if an exception occurs.
   - `finally`: Code that runs regardless of whether an exception occurred or not.

   **Example**:

   ```python
   try:
       result = 10 / 0  # This will raise a ZeroDivisionError
   except ZeroDivisionError as e:
       print(f"An error occurred: {e}")
   finally:
       print("This will always run regardless of an error.")
   ```

   In this example, `try` executes the code that may cause an error. If an error occurs, it moves to the `except` block where the error is caught and handled. The `finally` block always executes, regardless of whether an exception occurred or not.

3. **Raising custom exceptions with `raise`**:

   - Custom exceptions can be used to handle specific errors that are not captured by standard exceptions.
   - `raise` allows you to raise an exception manually when a certain condition is met.

   **Example**:

   ```python
   class InvalidInputError(Exception):
       pass

   def validate_input(num):
       if num < 0:
           raise InvalidInputError("Number cannot be negative")

   try:
       validate_input(-5)
   except InvalidInputError as e:
       print(e)  # Output: Number cannot be negative
   ```

   Here, `InvalidInputError` is a custom exception that is raised when the `validate_input` function encounters a negative input.

4. **Debugging techniques and tools in VS Code**:

   - **Breakpoints**: You can set breakpoints by clicking to the left of the line numbers in the editor. Execution will pause at these points when the script runs, allowing you to inspect the state of the program.
   - **Watch**: Use the "Watch" pane in VS Code to evaluate variables or expressions without interrupting the execution flow.
   - **Debug Console**: This is an interactive console that allows you to run Python code while the program is paused at a breakpoint.
   - **Debug Output**: Displays any output generated by the application while it is being debugged.

   **Example**:

   ```python
   import time

   def divide_numbers(a, b):
       return a / b

   # Setting a breakpoint here
   result = divide_numbers(10, 0)  # This will trigger an error
   ```

   While running the script, the program will hit the breakpoint, and you can inspect the variables in the debug console.

5. **Logging errors using the `logging` module**:

   - The `logging` module provides a flexible framework for emitting log messages from Python programs.
   - Levels of logging include `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
   - Logging can be configured to write to files, the console, or both.

   **Example**:

   ```python
   import logging

   logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

   try:
       result = 10 / 0
   except ZeroDivisionError as e:
       logging.error(f"An error occurred: {e}")
   ```

   This setup ensures that all messages of level `DEBUG` and above are output. The log entry includes the time, level, and the error message, which can be helpful for troubleshooting.

6. **Optimizing scripts for performance**:

   - Minimize the number of API requests, database queries, and unnecessary calculations.
   - Use list comprehensions and generator expressions for concise and efficient looping.
   - Profile code to identify bottlenecks and optimize accordingly.
   - **Example**:

     ```python
     # Inefficient approach
     results = []
     for i in range(1000):
         results.append(i ** 2)

     # Optimized approach using list comprehension
     results = [i ** 2 for i in range(1000)]
     ```

   - Profiling tools like `cProfile` can help identify which parts of your code are slowing down the execution.

7. **Refactoring code for better readability**:

   - Simplify complex logic by breaking down into smaller functions.
   - Use descriptive variable and function names.
   - Remove redundant code.
   - **Example**:

     ```python
     # Poorly structured code
     def calculate_average(nums):
         total = 0
         for num in nums:
             total += num
         return total / len(nums)

     # Refactored code
     def calculate_average(nums):
         return sum(nums) / len(nums)
     ```

   In the refactored version, the function is more readable and concise, eliminating the need for a temporary variable.

8. **Writing reusable utility functions**:

   - Create functions that encapsulate common operations.
   - These functions can be used across different parts of your application, improving modularity and reducing redundancy.
   - **Example**:

     ```python
     def convert_to_celsius(fahrenheit):
         return (fahrenheit - 32) * 5/9

     def convert_to_fahrenheit(celsius):
         return celsius * 9/5 + 32

     # Using utility functions
     temp_in_celsius = convert_to_celsius(100)
     temp_in_fahrenheit = convert_to_fahrenheit(37)
     ```

   Utility functions like these not only make the code easier to understand but also easier to modify in the future without affecting other parts of the application.

9. **Unit testing with `unittest`**:

   - Unit tests verify the correctness of individual components of the program.
   - `unittest` is a built-in Python module that provides a framework for creating and running tests.
   - **Example**:

     ```python
     import unittest

     def add(a, b):
         return a + b

     class TestAddFunction(unittest.TestCase):
         def test_add_positive_numbers(self):
             self.assertEqual(add(2, 3), 5)

         def test_add_negative_numbers(self):
             self.assertEqual(add(-2, -3), -5)

         def test_add_mixed_numbers(self):
             self.assertEqual(add(-2, 3), 1)

     if __name__ == '__main__':
         unittest.main()
     ```

   The `TestAddFunction` class contains test methods that check the addition function with different types of inputs, ensuring that it behaves correctly under various conditions.

10. **Profiling code for bottlenecks**:

- Use `cProfile` to find out which parts of your program consume the most time.
- Analyze the profile output to make optimizations.
- **Example**:

  ```python
  import cProfile

  def sum_large_list(numbers):
      total = 0
      for num in numbers:
          total += num
      return total

  cProfile.run('sum_large_list(range(1000000))')
  ```

The output from `cProfile` will show which functions are consuming the most time, helping you focus your optimization efforts where they will have the most impact.

---

### **Hands-On Tasks:**

---

1. **Write a program that handles division by zero gracefully**:

   - **Objective**: Write a Python program that safely performs division, catching a `ZeroDivisionError` and handling it gracefully.
   - **Example**:

     ```python
     def divide_numbers(a, b):
         try:
             result = a / b
         except ZeroDivisionError:
             return "Cannot divide by zero"
         else:
             return result

     # Usage
     print(divide_numbers(10, 2))  # Outputs: 5.0
     print(divide_numbers(10, 0))  # Outputs: Cannot divide by zero
     ```

   This program catches the `ZeroDivisionError` in the `except` block and returns a user-friendly message.

2. **Create a custom exception for invalid user inputs**:

   - **Objective**: Create a custom exception class and use it to handle invalid inputs.
   - **Example**:

     ```python
     class InvalidInputError(Exception):
         pass

     def validate_age(age):
         if not (0 <= age <= 150):
             raise InvalidInputError("Age must be between 0 and 150")

     try:
         validate_age(-5)  # Invalid input
     except InvalidInputError as e:
         print(e)  # Outputs: Age must be between 0 and 150
     ```

   The `InvalidInputError` is raised when the `validate_age` function is passed an invalid age.

3. **Debug a script with logical errors using VS Code breakpoints**:

   - **Objective**: Use VS Code breakpoints to identify and fix logical errors in a script.
   - **Example**:

     ```python
     def find_max(nums):
         max_num = nums[0]
         for num in nums:
             if num > max_num:
                 max_num = num
         return max_num

     # Setting breakpoint here
     numbers = [1, 2, 3, 4, 5]
     print(find_max(numbers))  # Potential logical error might exist

     # Running the script in VS Code and checking the value of `max_num` at the breakpoint
     ```

   Setting a breakpoint allows you to pause the execution and inspect variables, helping to identify where logic fails.

4. **Add logging to an existing script to track its execution**:

   - **Objective**: Use Python’s `logging` module to add logging to an existing script to monitor its execution.
   - **Example**:

     ```python
     import logging

     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

     def some_function():
         logging.debug("Function started")
         # Some operations
         logging.info("Function completed successfully")

     some_function()
     ```

   This setup logs messages to the console, providing a timestamp, logging level, and the message itself, which is useful for debugging and monitoring script behavior.

5. **Refactor a repetitive script into reusable functions**:

   - **Objective**: Break down a repetitive script into smaller, reusable functions.
   - **Example**:

     ```python
     def add(a, b):
         return a + b

     def subtract(a, b):
         return a - b

     def multiply(a, b):
         return a * b

     def divide(a, b):
         if b == 0:
             return "Cannot divide by zero"
         return a / b

     # Using the functions
     print(add(5, 3))        # Outputs: 8
     print(subtract(10, 6))  # Outputs: 4
     print(multiply(2, 7))   # Outputs: 14
     print(divide(15, 3))    # Outputs: 5.0
     print(divide(15, 0))    # Outputs: Cannot divide by zero
     ```

   Refactoring into functions makes the code more modular, reusable, and easier to maintain.

6. **Write unit tests for a simple calculator program**:

   - **Objective**: Write unit tests using `unittest` for a simple calculator program.
   - **Example**:

     ```python
     import unittest

     def add(a, b):
         return a + b

     def subtract(a, b):
         return a - b

     def multiply(a, b):
         return a * b

     def divide(a, b):
         if b == 0:
             raise ValueError("Cannot divide by zero")
         return a / b

     class TestCalculator(unittest.TestCase):
         def test_add(self):
             self.assertEqual(add(2, 3), 5)

         def test_subtract(self):
             self.assertEqual(subtract(5, 3), 2)

         def test_multiply(self):
             self.assertEqual(multiply(2, 3), 6)

         def test_divide(self):
             self.assertEqual(divide(6, 3), 2)
             with self.assertRaises(ValueError):
                 divide(5, 0)

     if __name__ == '__main__':
         unittest.main()
     ```

   Unit tests ensure that each function works as expected under different conditions and inputs.

7. **Optimize a loop-heavy script for performance**:

   - **Objective**: Identify and optimize a script with heavy loops to improve performance.
   - **Example**:

     ```python
     import time

     def sum_large_list():
         total = 0
         for i in range(1000000):
             total += i
         return total

     # Inefficient loop
     start_time = time.time()
     sum_large_list()
     end_time = time.time()
     print(f"Time taken: {end_time - start_time} seconds")

     # Optimized using list comprehension
     def optimized_sum():
         return sum(range(1000000))

     start_time = time.time()
     optimized_sum()
     end_time = time.time()
     print(f"Time taken: {end_time - start_time} seconds")
     ```

   The optimized version of the `sum_large_list` function uses `sum()` which is faster due to optimized internal loops.

8. **Use `timeit` to profile the execution time of functions**:

   - **Objective**: Measure the execution time of functions to identify performance bottlenecks.
   - **Example**:

     ```python
     import timeit

     def add(a, b):
         return a + b

     # Time the add function
     time_taken = timeit.timeit('add(5, 3)', globals=globals(), number=1000000)
     print(f"Time taken for add function: {time_taken} seconds")
     ```

   `timeit` is used to measure how long a piece of Python code takes to run. This helps in identifying if a function is slow and needs optimization.

9. **Implement caching for API responses in a script**:

   - **Objective**: Cache API responses to avoid redundant requests and improve performance.
   - **Example**:

     ```python
     import requests
     from cachetools import cached, TTLCache

     cache = TTLCache(maxsize=100, ttl=300)  # Cache with a 5-minute expiration time

     @cached(cache)
     def fetch_weather(city):
         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key"
         response = requests.get(url)
         return response.json()

     # Fetch weather for London, cached response if repeated
     weather_london = fetch_weather("London")
     print(weather_london)

     # Fetch weather for London again, this time from cache
     weather_london_cached = fetch_weather("London")
     print(weather_london_cached)
     ```

   Caching using `cachetools` reduces the time spent fetching data from the API by storing results for a specified duration.

10. **Create a logging setup that writes error logs to a file**:

- **Objective**: Configure logging to write error messages to a file for better monitoring and debugging.
- **Example**:

  ```python
  import logging

  logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      logging.error(f"An error occurred: {e}")
  ```

This setup logs all errors to a file `error.log`, which can be useful for post-execution review and debugging.

**11. Identify and Diagnose Errors in Code**:

- **Objective**: Write a script that not only catches errors but also provides a diagnostic message specifying whether the error was due to incorrect input, a processing issue, or a coding mistake.
- **Example**:

```python
import sys

def process_data(data):
    try:
        # Simulating a potential error
        result = 10 / data['value']
        return result
    except ZeroDivisionError as e:
        line_number = sys.exc_info()[-1].tb_lineno
        raise ValueError(f"Processing error: Division by zero on line {line_number}. Problematic data['value']") from e
    except KeyError as e:
        line_number = sys.exc_info()[-1].tb_lineno
        raise ValueError(f"Input error: Missing required key in data dictionary on line {line_number}.") from e
    except Exception as e:
        line_number = sys.exc_info()[-1].tb_lineno
        raise ValueError(f"Unexpected error on line {line_number}: {e}") from e

def main():
    data_valid = {'value': 5}   # Valid input
    data_invalid_key = {}      # Invalid input (missing 'value')
    data_zero_division = {'value': 0}  # Invalid input (division by zero)

    try:
        print(process_data(data_valid))  # Expected output: 2.0
        print(process_data(data_invalid_key))  # Should raise KeyError
        print(process_data(data_zero_division))  # Should raise ZeroDivisionError
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

**Explanation**:

- **Task**: The `process_data` function attempts to divide a number by `data['value']`. It catches specific exceptions:
  - **ZeroDivisionError**: Raised if the division cannot be performed (e.g., `data['value']` is zero).
  - **KeyError**: Raised if the input dictionary is missing the required key.
  - **Exception**: Catches any other unexpected errors.
- **Diagnostic Messages**: Each exception is accompanied by a diagnostic message that indicates the source of the error—whether it was due to an incorrect input, a processing issue, or a programming mistake.
- **`sys.exc_info()`** is used to get the current exception information, which includes the traceback object.
- **`tb_lineno`** extracts the line number from this traceback, providing a precise location for the error.
- Each type of exception now includes a detailed message specifying the line number and the cause of the error.
