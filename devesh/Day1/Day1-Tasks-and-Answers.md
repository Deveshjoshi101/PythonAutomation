### Day 1: Introduction to Python & Setup - Detailed Guide

#### **Objective**: Get trainees comfortable with Python basics and tools. 🎯🎉

---

### **Topics and Answers**

#### 1. Installing Python and VS Code 🎨✨

- **Steps to Install Python**:

  1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
  2. Download the latest version for your operating system.
  3. During installation, ensure you check the box **"Add Python to PATH"**.
  4. Verify installation by opening a terminal (Command Prompt/PowerShell/Terminal) and typing:
     ```
     python --version
     ```

- **Steps to Install VS Code**:
  1. Download Visual Studio Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
  2. Install it by following the on-screen instructions.

#### 2. Configuring VS Code with Python Extensions 🚀🔥

- **Steps**:
  1. Open VS Code and go to the Extensions Marketplace (Ctrl+Shift+X).
  2. Search for the **"Python" extension** by Microsoft.
  3. Click **Install**.
  4. Configure Python interpreter by pressing `Ctrl+Shift+P`, typing "Python: Select Interpreter," and choosing the appropriate version.

#### 3. Introduction to pip and Setting Up Virtual Environments (venv) 🛠️🌟

- **Using pip**:

  - Verify installation by typing:
    ```
    pip --version
    ```
  - Install a library (e.g., `requests`) using:
    ```
    pip install requests
    ```

- **Creating and Activating Virtual Environments**:
  1. Create a new virtual environment:
     ```
     python -m venv myenv
     ```
  2. Activate it:
     - Windows:
       ```
       myenv\Scripts\activate
       ```
     - macOS/Linux:
       ```
       source myenv/bin/activate
       ```

#### 4. Basic Python Syntax, Indentation, and Comments 📏✏️

- **Syntax**:

  - Python relies on indentation instead of braces:
    ```python
    if True:
        print("Hello, Python!")
    ```

- **Comments**:
  - Single-line:
    ```python
    # This is a comment
    ```
  - Multi-line:
    ```python
    """
    This is a
    multi-line comment.
    """
    ```

#### 5. Variables and Data Types 🎛️📊

- **Variables**:

  - Created by assignment:
    ```python
    x = 10  # Integer
    name = "John"  # String
    ```

- **Common Data Types**:
  - `int`: Integers (e.g., 10, -5)
  - `float`: Floating-point numbers (e.g., 3.14, -0.01)
  - `str`: Strings (e.g., "Hello")
  - `bool`: Boolean (e.g., True, False)

#### 6. Arithmetic Operations and String Manipulations 🔢📚

- **Operations**:

  ```python
  addition = 5 + 3       # 8
  subtraction = 5 - 3    # 2
  multiplication = 5 * 3 # 15
  division = 5 / 2       # 2.5
  ```

- **String Manipulations**:
  ```python
  greeting = "Hello" + " World!"  # Concatenation
  length = len(greeting)          # Length of string
  ```

#### 7. Taking Input and Printing Outputs 📝🔊

- **Input**:
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name + "!")
  ```

#### 8. Debugging Using Print Statements 🕵️‍♂️💻

- **Example**:
  ```python
  x = 10
  print("The value of x is:", x)  # Debugging output
  ```

#### 9. Python Execution in VS Code ⚡🖥️

- **Steps**:
  1. Open a Python file in VS Code.
  2. Press `F5` or run the script by typing:
     ```
     python script_name.py
     ```

#### 10. Differences Between Python 2 and 3 📜⏳

- **Key Differences**:
  - Print statement:
    - Python 2:
      ```python
      print "Hello"
      ```
    - Python 3:
      ```python
      print("Hello")
      ```
  - Division:
    - Python 2:
      ```python
      print 5 / 2  # Output: 2
      ```
    - Python 3:
      ```python
      print(5 / 2)  # Output: 2.5
      ```

---

### **Tasks with Answers** 🎯✅

#### Task 1: Install Python and Set Up VS Code

- **Solution**: Follow the above steps.

#### Task 2: Create and Activate a Virtual Environment

- **Solution**:
  ```
  python -m venv myenv
  myenv\Scripts\activate  # Windows
  ```

#### Task 3: Write a Script to Calculate the Area of a Rectangle

- **Script**:
  ```python
  length = float(input("Enter length: "))
  width = float(input("Enter width: "))
  area = length * width
  print("Area of the rectangle is:", area)
  ```

#### Task 4: Debug a Faulty Script

- **Faulty Script**:
  ```python
  length = input("Enter length: ")
  width = input("Enter width: ")
  area = length * width
  print(area)
  ```
- **Corrected Script**:
  ```python
  length = float(input("Enter length: "))
  width = float(input("Enter width: "))
  area = length * width
  print("Area:", area)
  ```

#### Task 5: Create a Greeting Program

- **Script**:
  ```python
  name = input("What is your name? ")
  print("Welcome, " + name + "!")
  ```

#### Task 6: Add Two Numbers Taken as Input

- **Script**:
  ```python
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print("Sum:", num1 + num2)
  ```

#### Task 7: Experiment with Arithmetic Operations

- **Script**:
  ```python
  a = 10
  b = 3
  print("Addition:", a + b)
  print("Division:", a / b)
  print("Modulus:", a % b)
  ```

#### Task 8: Write a Script to Swap Two Variables

- **Script**:
  ```python
  x = 5
  y = 10
  x, y = y, x
  print("x:", x, "y:", y)
  ```

#### Task 9: Check Python’s Version

- **Command**:
  ```
  python --version
  ```

#### Task 10: Execute a Python File in VS Code

- **Steps**:
  1. Save the Python script (e.g., `hello.py`).
  2. Press `F5` or run:
     ```
     python hello.py
     ```
