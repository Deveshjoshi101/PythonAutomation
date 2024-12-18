## **Day 2: Control Structures & Functions**

---

### **Objective**

The goal of Day 1 is to familiarize trainees with the essential tools and concepts required for Python programming and collaborative software development. By the end of the day, trainees should be able to write basic Python programs, execute scripts, and manage their code using Git and GitHub.

---

## **Topics Covered**

### **1. Introduction to Conditional Statements: `if`, `else`, `elif`**

Conditional statements allow decision-making in a program.

#### **Syntax**:

```python
if condition:
    # Code to execute if condition is true
elif another_condition:
    # Code to execute if another_condition is true
else:
    # Code to execute if no condition is true
```

#### **Examples**:

- **Check Age Group**:

```python
age = 25

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

- **Odd or Even Check**:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### **2. Logical Operators (`and`, `or`, `not`)**

Used to combine or negate conditions.

#### **Examples**:

- **`and` Example**:

```python
x, y = 10, 20

if x > 5 and y > 15:
    print("Both conditions are true")
```

- **`or` Example**:

```python
if x > 15 or y > 15:
    print("At least one condition is true")
```

- **`not` Example**:

```python
is_raining = False

if not is_raining:
    print("It's not raining")
```

---

### **3. Loops:**

#### **`for` Loop**:

Used to iterate over sequences (lists, strings, ranges).

**Example**: Print numbers from 1 to 5:

```python
for i in range(1, 6):
    print(i)
```

#### **`while` Loop**:

Used when the number of iterations depends on a condition.

**Example**: Countdown from 5:

```python
count = 5

while count > 0:
    print(count)
    count -= 1
```

---

### **4. Nested Loops and Loop Control (`break`, `continue`, `pass`)**

- **Nested Loops**:
  Loops inside another loop.

  **Example**:

  ```python
  for i in range(1, 4):
      for j in range(1, 4):
          print(f"i={i}, j={j}")
  ```

- **`break`**: Exit the loop.  
   **Example**:

  ```python
  for i in range(1, 10):
      if i == 5:
          break
      print(i)
  ```

- **`continue`**: Skip the current iteration.  
   **Example**:

  ```python
  for i in range(1, 10):
      if i % 2 == 0:
          continue
      print(i)
  ```

- **`pass`**: Placeholder for future code.  
   **Example**:
  ```python
  for i in range(1, 5):
      if i == 3:
          pass  # Placeholder
      print(i)
  ```

---

### **5. Introduction to Functions: Defining and Calling**

Functions encapsulate reusable code.

#### **Syntax**:

```python
def function_name(parameters):
    # Code block
    return value
```

#### **Example**:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

### **6. Parameters and Return Values in Functions**

Functions can accept arguments and return results.

#### **Example**:

```python
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # Output: 12
```

---

### **7. Default and Keyword Arguments**

- **Default Arguments**: Provide a default value for parameters.
- **Keyword Arguments**: Pass arguments explicitly by name.

#### **Examples**:

- **Default Arguments**:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!
```

- **Keyword Arguments**:

```python
def power(base, exponent):
    return base ** exponent

print(power(exponent=3, base=2))  # Output: 8
```

---

### **8. Lambda Functions**

Anonymous functions created with `lambda`.

#### **Syntax**:

```python
lambda arguments: expression
```

#### **Examples**:

- **Basic Lambda**:

```python
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

- **Lambda with `filter`**:

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]
```

---

### **9. Function Scope and `global` Keyword**

- **Local Scope**: Variables declared inside a function.
- **Global Scope**: Variables declared outside functions.
- **`global` Keyword**: Modify a global variable inside a function.

#### **Examples**:

- **Local Scope**:

```python
def greet():
    name = "Alice"
    print(f"Hello, {name}")

greet()
# print(name)  # Error: name is not defined
```

- **Global Scope**:

```python
x = 10

def print_global():
    print(x)  # Accesses the global variable

print_global()
```

- **`global` Keyword**:

```python
x = 10

def modify_global():
    global x
    x += 5

modify_global()
print(x)  # Output: 15
```

---

### **10. Using `help()` for Built-in Functions**

The `help()` function provides documentation for Python’s built-in functions and objects.

#### **Examples**:

- **Check Documentation**:

```python
help(len)    # Displays usage of len()
help(print)  # Displays usage of print()
```

- **Learn About Data Types**:

```python
help(str)    # String methods and attributes
help(list)   # List methods and attributes
```

---

### **Hands-On Tasks**

---

### **1. Check if a Number is Positive, Negative, or Zero**

#### **Code**:

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example
number = float(input("Enter a number: "))
print(f"The number is {check_number(number)}")
```

---

### **2. Calculate Grades Based on Input Marks**

#### **Code**:

```python
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "Fail"

# Example
marks = int(input("Enter marks: "))
print(f"Grade: {calculate_grade(marks)}")
```

---

### **3. Print Numbers from 1 to 10 Using a `while` Loop**

#### **Code**:

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

---

### **4. Calculate the Factorial of a Number**

#### **Code**:

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
```

---

### **5. Find the Largest of Three Numbers**

#### **Code**:

```python
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

# Example
x, y, z = map(int, input("Enter three numbers separated by space: ").split())
print(f"The largest number is {find_largest(x, y, z)}")
```

---

### **6. Print the Fibonacci Sequence Up to 10 Terms**

#### **Code**:

```python
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example
print(f"Fibonacci sequence (10 terms): {fibonacci(10)}")
```

---

### **7. Reverse a String**

#### **Code**:

```python
def reverse_string(s):
    return s[::-1]

# Example
string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")
```

---

### **8. Print a Pyramid Pattern Using Nested Loops**

#### **Code**:

```python
def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Example
rows = int(input("Enter the number of rows: "))
pyramid_pattern(rows)
```

---

### **9. Lambda Function to Add 10 to a Number**

#### **Code**:

```python
add_ten = lambda x: x + 10

# Example
number = int(input("Enter a number: "))
print(f"Number after adding 10: {add_ten(number)}")
```

---

### **10. Debug a Function with Missing or Incorrect Return Statements**

#### **Original (Faulty) Function**:

```python
# Function to calculate square of a number
def square(num):
    result = num * num  # Missing return statement
```

#### **Fixed Code**:

```python
def square(num):
    return num * num

# Example
number = int(input("Enter a number: "))
print(f"The square of {number} is {square(number)}")
```
