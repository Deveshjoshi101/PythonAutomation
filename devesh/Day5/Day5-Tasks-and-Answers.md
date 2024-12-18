### **Day 5: Libraries for Automation**

---

#### **Objective**

Learn to utilize Python libraries to automate tasks effectively and efficiently.

---

### **Topics Covered in Detail**

---

#### **1. Using `os` for File and Directory Operations**

The `os` module provides functions to interact with the operating system.

**Common Uses**:

- Create, rename, or delete directories.
- Get the current working directory (`os.getcwd()`).
- List files in a directory (`os.listdir()`).

**Example**:

```python
import os

# Get the current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
os.mkdir('new_folder')

# List files in a directory
print("Files:", os.listdir('.'))

# Rename a directory
os.rename('new_folder', 'renamed_folder')

# Delete a directory
os.rmdir('renamed_folder')
```

---

#### **2. Introduction to `shutil` for File Copying and Archiving**

The `shutil` module handles higher-level file operations, such as copying and archiving files or directories.

**Example**:

```python
import shutil

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Move a file
shutil.move('source.txt', 'backup/')

# Create a zip archive
shutil.make_archive('archive', 'zip', 'backup')
```

---

#### **3. `argparse` for Command-Line Arguments**

The `argparse` module simplifies the process of creating user-friendly command-line tools.

**Example**:

```python
import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('--number', type=int, help="Provide a number")
args = parser.parse_args()

print(f"You entered the number: {args.number}")
```

**Run in terminal**:

```bash
python script.py --number 10
```

---

#### **4. Using `datetime` for Timestamps and Scheduling**

The `datetime` module provides tools to work with dates and times.

**Example**:

```python
from datetime import datetime, timedelta

# Current timestamp
now = datetime.now()
print("Current Time:", now)

# Add 5 days to the current date
future_date = now + timedelta(days=5)
print("Future Date:", future_date)

# Format dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
```

---

#### **5. Automating Tasks with `schedule`**

The `schedule` library helps schedule tasks at regular intervals.

**Installation**:

```bash
pip install schedule
```

**Example**:

```python
import schedule
import time

def task():
    print("Task executed!")

# Schedule the task to run every minute
schedule.every(1).minute.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

#### **6. File Matching with `glob`**

The `glob` module matches file patterns in directories.

**Example**:

```python
import glob

# Match all `.txt` files
txt_files = glob.glob('*.txt')
print("Text Files:", txt_files)

# Match files starting with "data_"
data_files = glob.glob('data_*.csv')
print("Data Files:", data_files)
```

---

#### **7. Introduction to `subprocess` for Running Shell Commands**

The `subprocess` module allows running shell commands directly from Python.

**Example**:

```python
import subprocess

# Run a shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

---

#### **8. Reading and Writing Excel Files with `openpyxl`**

The `openpyxl` library is used to manipulate Excel files.

**Installation**:

```bash
pip install openpyxl
```

**Example**:

```python
from openpyxl import Workbook, load_workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active
sheet.title = "Sample Sheet"

# Add data to cells
sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet.append(["Alice", 25])
sheet.append(["Bob", 30])

# Save the workbook
wb.save("sample.xlsx")

# Load and read from an existing workbook
wb = load_workbook("sample.xlsx")
sheet = wb.active
for row in sheet.iter_rows(values_only=True):
    print(row)
```

---

#### **9. Introduction to `pyautogui` for GUI Automation**

The `pyautogui` library allows automating GUI interactions like mouse clicks and keystrokes.

**Installation**:

```bash
pip install pyautogui
```

**Example**:

```python
import pyautogui

# Get the screen size
screen_width, screen_height = pyautogui.size()
print("Screen Size:", screen_width, screen_height)

# Move the mouse
pyautogui.moveTo(100, 100, duration=1)

# Click the mouse
pyautogui.click()

# Type text
pyautogui.typewrite("Hello, World!")
```

---

#### **10. Managing JSON Data with `json`**

The `json` module is used for encoding and decoding JSON data.

**Example**:

```python
import json

# Serialize Python object to JSON
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
json_data = json.dumps(data, indent=4)
print(json_data)

# Write JSON data to a file
with open('data.json', 'w') as file:
    file.write(json_data)

# Read JSON data from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

---

### **Hands-On Tasks**

---

#### **1. Write a Script to Rename Files Based on a Pattern**

Use the `os` module to rename files in a directory according to a specific pattern.

**Example**:  
Rename all `.txt` files to `file_1.txt`, `file_2.txt`, etc.

```python
import os

# Directory containing files
directory = './files'

# List all files in the directory
files = os.listdir(directory)

# Rename files with a specific pattern
for i, file in enumerate(files, start=1):
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory, f"file_{i}.txt")
    os.rename(old_path, new_path)
    print(f"Renamed {file} to file_{i}.txt")
```

---

#### **2. Automate Archiving Old Files into a ZIP Folder**

Use the `shutil` module to create a ZIP archive of files older than a specified date.

**Example**:

```python
import os
import shutil
import time

directory = './files'
archive_name = 'old_files'

# Get the current time
current_time = time.time()

# Archive files older than 7 days
with shutil.ZipFile(f"{archive_name}.zip", 'w') as archive:
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and current_time - os.path.getmtime(file_path) > 7 * 86400:
            archive.write(file_path, arcname=file)
            os.remove(file_path)
            print(f"Archived and removed {file}")
```

---

#### **3. Write a Program to Delete Files Older Than a Specified Date**

Delete files older than 30 days.

**Example**:

```python
import os
import time

directory = './files'
threshold = 30 * 86400  # 30 days in seconds

# Get current time
current_time = time.time()

# Delete files older than threshold
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path) and current_time - os.path.getmtime(file_path) > threshold:
        os.remove(file_path)
        print(f"Deleted {file}")
```

---

#### **4. Schedule a Python Script to Run Daily Using `schedule`**

Run a script every day at a specific time.

**Example**:

```python
import schedule
import time

def daily_task():
    print("Running daily task!")

# Schedule the task
schedule.every().day.at("10:00").do(daily_task)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

#### **5. Write a Script to Copy Files from One Folder to Another**

Use `shutil.copy()` to copy files.

**Example**:

```python
import os
import shutil

source = './source_folder'
destination = './destination_folder'

# Copy all files from source to destination
for file in os.listdir(source):
    source_path = os.path.join(source, file)
    destination_path = os.path.join(destination, file)
    if os.path.isfile(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied {file} to {destination}")
```

---

#### **6. Create a Program to Extract Specific Rows from an Excel Sheet**

Use `openpyxl` to read and filter Excel data.

**Example**:  
Extract rows where the "Score" is greater than 80.

```python
from openpyxl import load_workbook

# Load the workbook
workbook = load_workbook('students.xlsx')
sheet = workbook.active

# Extract rows
for row in sheet.iter_rows(values_only=True):
    if row[1] > 80:  # Assuming the "Score" is in the second column
        print(row)
```

---

#### **7. Write a Program to Automate Mouse Clicks Using `pyautogui`**

Automate repetitive mouse clicks at specific coordinates.

**Example**:

```python
import pyautogui
import time

# Wait 5 seconds to position the mouse
time.sleep(5)

# Click 10 times at the current mouse position
for _ in range(10):
    pyautogui.click()
    time.sleep(1)
```

---

#### **8. Build a Script to Find and Delete Duplicate Files in a Directory**

Use file hashes to identify duplicates.

**Example**:

```python
import os
import hashlib

def get_file_hash(file_path):
    with open(file_path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()

directory = './files'
hash_map = {}

# Find and delete duplicates
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        file_hash = get_file_hash(file_path)
        if file_hash in hash_map:
            os.remove(file_path)
            print(f"Deleted duplicate: {file}")
        else:
            hash_map[file_hash] = file
```

---

#### **9. Implement a Script to Execute a Shell Command and Capture Its Output**

Run a shell command and print its output.

**Example**:

```python
import subprocess

# Run a shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

---

#### **10. Parse a JSON File and Modify Its Contents Programmatically**

Modify a JSON file to add a new key-value pair.

**Example**:

```python
import json

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Modify data
data['new_key'] = 'new_value'

# Save changes back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Modified JSON:", data)
```
