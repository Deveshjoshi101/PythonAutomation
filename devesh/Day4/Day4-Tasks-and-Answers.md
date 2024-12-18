### **Day 4: File Handling**

File handling is an essential skill in Python, enabling interaction with various types of files for reading, writing, and data processing.

---

### **Topics Covered**

#### **1. Opening and Closing Files with `open()` and `close()`**

- Files can be opened using the `open()` function and closed explicitly using `close()`.
- Syntax:
  ```python
  file = open('example.txt', 'r')  # Open in read mode
  content = file.read()
  print(content)
  file.close()
  ```
- **Important**: Always close a file after using it to free up system resources.

---

#### **2. Using `with` for File Handling**

- The `with` statement ensures files are automatically closed after their block of code is executed.
- Syntax:
  ```python
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
  # File is automatically closed here.
  ```

---

#### **3. Reading Files Line by Line**

- Reading large files line by line prevents excessive memory usage.
- Example:
  ```python
  with open('example.txt', 'r') as file:
      for line in file:
          print(line.strip())  # Remove extra newlines
  ```

---

#### **4. Writing to Files and Appending Content**

- **Writing**: Overwrites the file or creates a new one if it doesn’t exist.
  ```python
  with open('example.txt', 'w') as file:
      file.write("This is a new line.\n")
  ```
- **Appending**: Adds content to the end of an existing file.
  ```python
  with open('example.txt', 'a') as file:
      file.write("This is an additional line.\n")
  ```

---

#### **5. Working with CSV Files Using the `csv` Module**

- CSV files are commonly used for structured data. Python’s `csv` module makes handling them simple.
- Reading CSV:

  ```python
  import csv

  with open('data.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
          print(row)
  ```

- Writing CSV:
  ```python
  with open('data.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Name', 'Age'])
      writer.writerow(['Alice', 30])
  ```

---

#### **6. Handling File Paths with `os`**

- The `os` module helps manage file paths and directories.
- Example:

  ```python
  import os

  current_directory = os.getcwd()  # Get current working directory
  print("Current Directory:", current_directory)

  new_path = os.path.join(current_directory, 'example.txt')
  print("File Path:", new_path)
  ```

---

#### **7. Error Handling During File Operations (`try-except`)**

- Files may not exist or access permissions could fail; handle such issues gracefully.
- Example:
  ```python
  try:
      with open('nonexistent.txt', 'r') as file:
          content = file.read()
  except FileNotFoundError:
      print("File not found!")
  except PermissionError:
      print("Permission denied!")
  ```

---

#### **8. File Modes (`r`, `w`, `a`, `rb`, etc.)**

- File modes define how the file is opened.
  - `'r'`: Read-only.
  - `'w'`: Write (overwrite).
  - `'a'`: Append.
  - `'rb'`: Read binary.
  - `'wb'`: Write binary.
- Example:
  ```python
  with open('example.txt', 'rb') as file:
      content = file.read()
      print(content)
  ```

---

#### **9. Reading Large Files Efficiently**

- Use `readlines()` or process files in chunks to handle large files.
- Example:
  ```python
  with open('large_file.txt', 'r') as file:
      while chunk := file.read(1024):  # Read in 1KB chunks
          print(chunk)
  ```

---

#### **10. Checking File Existence with `os.path`**

- Use `os.path` to verify file existence before performing operations.
- Example:

  ```python
  import os

  if os.path.exists('example.txt'):
      print("File exists!")
  else:
      print("File does not exist.")
  ```

---

### **Key Notes**

- File operations must handle edge cases such as missing files or insufficient permissions.
- Use `with` whenever possible to simplify file management and avoid forgetting to close files.

---

### **Hands-On Tasks**

---

#### **1. Write a Program to Create and Write Content to a Text File**

**Objective**: Create a new file and write content into it.

**Steps**:

1. Use `open()` or `with` in write mode (`'w'`).
2. Write multiple lines to the file.

**Code Example**:

```python
with open('example.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
print("File created and content written.")
```

---

#### **2. Read a File and Count the Number of Lines and Words**

**Objective**: Analyze the contents of a file.

**Steps**:

1. Read the file content.
2. Split the content into lines and words to count them.

**Code Example**:

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    word_count = sum(len(line.split()) for line in lines)
    print(f"Number of lines: {len(lines)}")
    print(f"Number of words: {word_count}")
```

---

#### **3. Implement a Script to Merge Two Text Files**

**Objective**: Combine the content of two files into one.

**Steps**:

1. Open both files and read their content.
2. Write the combined content into a new file.

**Code Example**:

```python
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()

with open('merged_file.txt', 'w') as merged:
    merged.write(content1)
    merged.write("\n")
    merged.write(content2)
print("Files merged successfully.")
```

---

#### **4. Write a Program to Delete Specific Lines from a File**

**Objective**: Remove unwanted lines from a file.

**Steps**:

1. Read the file content into a list.
2. Exclude specific lines.
3. Write the modified content back to the file.

**Code Example**:

```python
line_to_remove = 2  # Line number to remove
with open('example.txt', 'r') as file:
    lines = file.readlines()

with open('example.txt', 'w') as file:
    for i, line in enumerate(lines, start=1):
        if i != line_to_remove:
            file.write(line)
print(f"Line {line_to_remove} removed.")
```

---

#### **5. Create a CSV File and Write Student Records into It**

**Objective**: Save structured data into a CSV file.

**Steps**:

1. Use the `csv` module.
2. Write headers and rows into the file.

**Code Example**:

```python
import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 20, 'A'])
    writer.writerow(['Bob', 22, 'B'])
print("CSV file created with student records.")
```

---

#### **6. Write a Program to Read a CSV File and Display Its Contents**

**Objective**: Extract and print data from a CSV file.

**Code Example**:

```python
import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

#### **7. Build a Script to Rename Files in a Folder**

**Objective**: Automate renaming of files in a directory.

**Steps**:

1. Use the `os` module to list files.
2. Rename files in a loop.

**Code Example**:

```python
import os

folder_path = './files'
for i, filename in enumerate(os.listdir(folder_path)):
    new_name = f"file_{i + 1}.txt"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
print("Files renamed successfully.")
```

---

#### **8. Write a Program to Extract File Extensions from File Names**

**Objective**: Identify the file types based on extensions.

**Code Example**:

```python
files = ['report.docx', 'image.png', 'data.csv', 'script.py']

for file in files:
    extension = file.split('.')[-1]
    print(f"File: {file}, Extension: {extension}")
```

---

#### **9. Create a Script to Find the Largest File in a Directory**

**Objective**: Identify the largest file based on size.

**Code Example**:

```python
import os

folder_path = './files'
largest_file = None
largest_size = 0

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        if size > largest_size:
            largest_size = size
            largest_file = file

print(f"Largest file: {largest_file} with size: {largest_size} bytes.")
```

---

#### **10. Implement Error Handling for Non-Existent Files**

**Objective**: Gracefully handle errors when working with files.

**Code Example**:

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied.")
```
