### **Day 1: Introduction to Python & Setup**

---

#### **Objective**

The goal of Day 1 is to familiarize trainees with the essential tools and concepts required for Python programming and collaborative software development. By the end of the day, trainees should be able to write basic Python programs, execute scripts, and manage their code using Git and GitHub.

---

### **Topics Covered**

#### **1. Installing Python and VS Code**

- **Python Installation**:

  - Trainees will download Python 3.x from the [official Python website](https://www.python.org/downloads/).
  - During installation:
    - Select the option **"Add Python to PATH"** to ensure Python can be accessed from the command line.
    - Verify installation by running:
      ```bash
      python --version
      ```
    - This command should output the installed Python version.

- **Installing VS Code**:
  - Download VS Code from [Visual Studio Code](https://code.visualstudio.com/).
  - Install and open the application.
  - Walkthrough of the VS Code interface: Sidebar, Extensions Marketplace, Terminal, and Editor Window.

---

#### **2. Configuring VS Code with Python Extensions**

- In the Extensions Marketplace:
  - Install the **Python Extension** (by Microsoft) for Python support.
  - Install **Pylance** for advanced code analysis and linting.
- Configure VS Code for Python:
  - Open a Python file, press **Ctrl+Shift+P**, and select `Python: Select Interpreter`.
  - Choose the Python interpreter corresponding to the installed version.
- Open the terminal in VS Code and ensure Python commands work by typing:
  ```bash
  python --version
  ```

---

#### **3. Introduction to `pip` and Virtual Environments**

- **`pip`**:

  - Verify `pip` is installed using:
    ```bash
    pip --version
    ```
  - Introduce package management by installing a library, e.g.:
    ```bash
    pip install requests
    ```

- **Virtual Environments**:
  - **Purpose**: Virtual environments help maintain project-specific dependencies.
  - Commands:
    ```bash
    python -m venv myenv
    ```
    - To activate the environment:
      - **Windows**: `myenv\Scripts\activate`
      - **Mac/Linux**: `source myenv/bin/activate`
    - To deactivate:
      ```bash
      deactivate
      ```

---

#### **4. Basic Python Syntax**

- **Indentation**:

  - Emphasize that Python relies on indentation for block definitions (no braces or semicolons).
  - Example:
    ```python
    if True:
        print("Indented correctly!")
    ```

- **Comments**:
  - Single-line comments: `# This is a comment`.
  - Multi-line comments: `"""This is a multi-line comment."""`.

---

#### **5. Variables and Data Types**

- **Overview**: Introduce the main data types (`int`, `float`, `str`, `bool`) and how to declare variables.
- Examples:
  ```python
  x = 10         # Integer
  y = 3.14       # Float
  name = "Alice" # String
  is_active = True # Boolean
  print(type(x)) # Output: <class 'int'>
  ```

---

#### **6. Arithmetic Operations and String Manipulations**

- **Arithmetic Operators**:
  - Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), etc.
- **String Manipulations**:
  ```python
  greeting = "Hello"
  name = "Alice"
  print(greeting + ", " + name + "!") # Concatenation
  print(name.upper())  # Output: ALICE
  print(name.lower())  # Output: alice
  ```

---

#### **7. Taking Input and Printing Output**

- Example of input and output:
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
  ```

---

#### **8. Debugging with Print Statements**

- Show how to print variable values to debug:
  ```python
  x = 10
  print("x =", x)  # Output: x = 10
  ```

---

#### **9. Python Execution in VS Code**

- Save a script as `example.py` in VS Code.
- Run the script:
  - Using the terminal: `python example.py`.
  - Using the green play button.

---

#### **10. Differences Between Python 2 and 3**

- Discuss briefly:
  - `print` is a function in Python 3 (`print("Hello")`), while it was a statement in Python 2 (`print "Hello"`).
  - Integer division in Python 3 always returns a float (`5/2 = 2.5`).

---

#### **11. Introduction to Git and GitHub**

- **GitHub Account**:

  - Create a GitHub account at [https://github.com](https://github.com).

- **Installing Git**:

  - Download Git from [https://git-scm.com/](https://git-scm.com/).
  - Verify installation:
    ```bash
    git --version
    ```

- **Basic Git Commands**:
  ```bash
  git init           # Initialize a repository
  git add .          # Stage changes
  git commit -m "Message"  # Commit changes
  git remote add origin <repo-URL> # Connect to remote repo
  git push -u origin main  # Push changes
  ```

---

#### **12. Using GitHub Collaboratively**

- **Forking and Cloning**:

  - Fork a repository on GitHub.
  - Clone it:
    ```bash
    git clone <repository-URL>
    ```

- **Pull Requests and Merge Conflicts**:
  - Create pull requests and demonstrate resolving a merge conflict.

---

### **Hands-On Tasks**

---

#### **1. Install Python and Set Up VS Code**

1. **Install Python**:

   - Download Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - During installation, check the box **"Add Python to PATH"**.
   - After installation, verify by opening a terminal and running:
     ```bash
     python --version
     ```
   - Output should display the installed Python version.

2. **Install VS Code**:
   - Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
   - Open VS Code, go to the Extensions Marketplace, and install the **Python Extension** (by Microsoft).

---

#### **2. Create and Activate a Virtual Environment**

1. Open a terminal and navigate to your project directory.
2. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source myenv/bin/activate
     ```

---

#### **3. Write a Script to Calculate the Area of a Rectangle**

1. Create a file named `rectangle_area.py`:

   ```python
   length = float(input("Enter the length of the rectangle: "))
   width = float(input("Enter the width of the rectangle: "))
   area = length * width
   print(f"The area of the rectangle is: {area}")
   ```

2. Save the file and run it using:
   ```bash
   python rectangle_area.py
   ```

---

#### **4. Debug a Faulty Script with Syntax Errors**

1. Faulty Script Example:
   ```python
   print("Welcome to the Debugging Task")
   x = input("Enter a number: ")
   y = input("Enter another number: ")
   z = x + y
   print("Sum is: " + z)
   ```
2. Debug and Fix:
   - Identify the issue: `x` and `y` are strings; they need to be converted to integers or floats before adding.
   - Correct Script:
     ```python
     print("Welcome to the Debugging Task")
     x = float(input("Enter a number: "))
     y = float(input("Enter another number: "))
     z = x + y
     print(f"Sum is: {z}")
     ```

---

#### **5. Create a Greeting Program**

1. Create a file named `greeting.py`:

   ```python
   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python.")
   ```

2. Run the script:
   ```bash
   python greeting.py
   ```

---

#### **6. Write a Program to Add Two Numbers**

1. Create a file named `add_two_numbers.py`:
   ```python
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   result = num1 + num2
   print(f"The sum is: {result}")
   ```

---

#### **7. Experiment with Arithmetic Operations**

1. Create a file named `arithmetic_operations.py`:

   ```python
   a = int(input("Enter the first number: "))
   b = int(input("Enter the second number: "))

   print(f"Addition: {a + b}")
   print(f"Subtraction: {a - b}")
   print(f"Multiplication: {a * b}")
   print(f"Division: {a / b}")
   print(f"Modulus: {a % b}")
   ```

---

#### **8. Write a Script to Swap Two Variables**

1. Create a file named `swap_variables.py`:

   ```python
   x = input("Enter the first value: ")
   y = input("Enter the second value: ")

   # Swap
   x, y = y, x

   print(f"After swapping: x = {x}, y = {y}")
   ```

---

#### **9. Create a Python Script to Check Python’s Version**

1. Create a file named `check_version.py`:

   ```python
   import sys
   print("Python Version:", sys.version)
   ```

2. Run the script:
   ```bash
   python check_version.py
   ```

---

#### **10. Execute a Python File in VS Code**

1. Open any script in VS Code, such as `greeting.py`.
2. Run the script by:
   - Pressing **F5** (if configured).
   - Clicking the green play button in the top-right corner.

---

#### **11. Initialize a Git Repository and Commit the Scripts**

1. In your project folder, initialize a Git repository:
   ```bash
   git init
   ```
2. Add all files:
   ```bash
   git add .
   ```
3. Commit the changes:
   ```bash
   git commit -m "Initial commit with basic Python scripts"
   ```

---

#### **12. Push the Repository to GitHub**

1. Create a new repository on GitHub (e.g., "python-training-day1").
2. Link the local repository to GitHub:
   ```bash
   git remote add origin <repository-URL>
   git branch -M main
   git push -u origin main
   ```

---

#### **13. Fork a Training Repository and Clone It Locally**

1. Fork a repository provided by the trainer.
2. Clone the forked repository:
   ```bash
   git clone <forked-repository-URL>
   ```

---

#### **14. Push the Day’s Scripts to a GitHub Repository**

1. Add the scripts to your forked repository.
2. Push the changes:
   ```bash
   git add .
   git commit -m "Added Day 1 scripts"
   git push
   ```

---

#### **15. Collaborate with Peers on GitHub**

1. Create a Pull Request:
   - Make changes to your forked repository and submit a pull request to the original repository.
2. **Resolve a Simulated Merge Conflict**:
   - Work with peers to create conflicting changes in the same file.
   - Pull the latest changes:
     ```bash
     git pull origin main
     ```
   - Resolve the conflict manually and commit the changes:
     ```bash
     git add .
     git commit -m "Resolved merge conflict"
     git push
     ```
