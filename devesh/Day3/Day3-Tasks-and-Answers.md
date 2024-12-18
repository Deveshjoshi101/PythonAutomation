## **Day 2: Control Structures & Functions**

---

### **Objective**

The goal of Day 1 is to familiarize trainees with the essential tools and concepts required for Python programming and collaborative software development. By the end of the day, trainees should be able to write basic Python programs, execute scripts, and manage their code using Git and GitHub.

---

## **Topics Covered**

---

#### 1. **Introduction to Lists and Their Methods**

- **Definition**: A list is an ordered, mutable (changeable) collection of elements. It can hold elements of different data types.
- **Examples**:
  ```python
  fruits = ["apple", "banana", "cherry"]
  numbers = [1, 2, 3, 4, 5]
  mixed = [1, "hello", 3.5, True]
  ```
- **Common Methods**:
  - `append(item)`: Adds an item to the end of the list.
    ```python
    fruits.append("orange")  # ["apple", "banana", "cherry", "orange"]
    ```
  - `pop(index)`: Removes and returns the item at the specified index.
    ```python
    fruits.pop(1)  # Removes "banana", resulting in ["apple", "cherry"]
    ```
  - `insert(index, item)`: Inserts an item at the specified position.
    ```python
    fruits.insert(1, "grape")  # ["apple", "grape", "cherry"]
    ```
  - `remove(item)`: Removes the first occurrence of the specified item.
    ```python
    fruits.remove("apple")  # ["grape", "cherry"]
    ```
  - `sort()`: Sorts the list in ascending order.
    ```python
    numbers.sort()  # [1, 2, 3, 4, 5]
    ```

---

#### 2. **List Slicing and Comprehensions**

- **Slicing**:
  - Extract a portion of a list using `[start:stop:step]`.
  - Examples:
    ```python
    nums = [10, 20, 30, 40, 50]
    print(nums[1:4])     # [20, 30, 40]
    print(nums[:3])      # [10, 20, 30]
    print(nums[::2])     # [10, 30, 50]
    ```
- **List Comprehensions**:
  - A concise way to create lists.
  - Syntax: `[expression for item in iterable if condition]`.
  - Examples:
    ```python
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
    ```

---

#### 3. **Tuples: Creation and Immutability**

- **Definition**: Tuples are immutable (cannot be changed) collections.
- **Creation**:
  ```python
  my_tuple = (1, 2, 3)
  another_tuple = 4, 5, 6  # Implicit tuple creation
  ```
- **Advantages**:
  - Faster than lists.
  - Used to store fixed data (e.g., coordinates).
- **Accessing Elements**:
  ```python
  print(my_tuple[1])  # 2
  ```
- **Immutability**:
  ```python
  my_tuple[1] = 10  # Error: tuples are immutable
  ```

---

#### 4. **Sets and Set Operations**

- **Definition**: Sets are unordered collections of unique elements.
- **Operations**:
  - `union()`: Combines all unique elements from both sets.
    ```python
    print({1, 2} | {2, 3})  # {1, 2, 3}
    ```
  - `intersection()`: Returns common elements.
    ```python
    print({1, 2} & {2, 3})  # {2}
    ```
  - `difference()`: Elements in the first set but not the second.
    ```python
    print({1, 2, 3} - {2, 3})  # {1}
    ```

---

#### 5. **Creating Dictionaries and Accessing Elements**

- **Definition**: Dictionaries store data as key-value pairs.
- **Creation**:
  ```python
  person = {"name": "Alice", "age": 25}
  ```
- **Accessing Elements**:
  ```python
  print(person["name"])  # Alice
  print(person.get("age"))  # 25
  ```

---

#### 6. **Adding, Updating, and Deleting Dictionary Items**

- **Adding**:
  ```python
  person["city"] = "New York"
  ```
- **Updating**:
  ```python
  person["age"] = 26
  ```
- **Deleting**:
  ```python
  del person["city"]
  ```

---

#### 7. **Iterating Through Lists, Tuples, and Dictionaries**

- **Lists**:
  ```python
  for item in [1, 2, 3]:
      print(item)
  ```
- **Tuples**:
  ```python
  for item in (1, 2, 3):
      print(item)
  ```
- **Dictionaries**:
  ```python
  for key, value in person.items():
      print(key, value)
  ```

---

#### 8. **Checking Membership Using `in` and `not in`**

- **Lists and Tuples**:
  ```python
  print(2 in [1, 2, 3])  # True
  print(4 not in (1, 2, 3))  # True
  ```
- **Dictionaries**:
  ```python
  print("name" in person)  # True
  ```

---

#### 9. **Nested Data Structures**

- **Lists of Dictionaries**:
  ```python
  students = [{"name": "Alice"}, {"name": "Bob"}]
  print(students[0]["name"])  # Alice
  ```
- **Dictionaries with Lists**:
  ```python
  person = {"name": "Alice", "grades": [85, 90, 95]}
  print(person["grades"][1])  # 90
  ```

---

#### 10. **Converting Between Data Types**

- **List to Set**:
  ```python
  my_list = [1, 2, 2, 3]
  my_set = set(my_list)  # {1, 2, 3}
  ```
- **Set to List**:
  ```python
  my_set = {1, 2, 3}
  my_list = list(my_set)  # [1, 2, 3]
  ```
- **Tuple to List**:
  ```python
  my_tuple = (1, 2, 3)
  my_list = list(my_tuple)  # [1, 2, 3]
  ```

---

### **Hands-On Tasks**

---

#### **1. Write a Program to Sort a List in Ascending Order**

- **Objective**: Use Python’s `sort()` method to arrange elements in a list in ascending order.
- **Example**:
  ```python
  numbers = [5, 2, 8, 1, 3]
  numbers.sort()
  print("Sorted List:", numbers)
  ```
- **Output**:
  ```
  Sorted List: [1, 2, 3, 5, 8]
  ```

---

#### **2. Create a Script to Remove Duplicates from a List Using Sets**

- **Objective**: Use a set to eliminate duplicate elements.
- **Example**:
  ```python
  items = [1, 2, 2, 3, 4, 4, 5]
  unique_items = list(set(items))
  print("List without duplicates:", unique_items)
  ```
- **Output**:
  ```
  List without duplicates: [1, 2, 3, 4, 5]
  ```

---

#### **3. Write a Program to Access and Modify Dictionary Values**

- **Objective**: Retrieve and update key-value pairs in a dictionary.
- **Example**:

  ```python
  student = {"name": "Alice", "age": 20, "grade": "B"}

  # Access values
  print("Name:", student["name"])

  # Modify values
  student["grade"] = "A"
  print("Updated Dictionary:", student)
  ```

- **Output**:
  ```
  Name: Alice
  Updated Dictionary: {'name': 'Alice', 'age': 20, 'grade': 'A'}
  ```

---

#### **4. Create a Tuple of Numbers and Calculate Their Sum**

- **Objective**: Use the `sum()` function to calculate the sum of elements in a tuple.
- **Example**:
  ```python
  numbers = (10, 20, 30, 40)
  total = sum(numbers)
  print("Sum of tuple elements:", total)
  ```
- **Output**:
  ```
  Sum of tuple elements: 100
  ```

---

#### **5. Implement a Script to Find the Most Frequent Word in a List**

- **Objective**: Use a dictionary to count word occurrences and determine the most frequent word.
- **Example**:

  ```python
  words = ["apple", "banana", "apple", "orange", "banana", "apple"]
  word_count = {}

  for word in words:
      word_count[word] = word_count.get(word, 0) + 1

  most_frequent = max(word_count, key=word_count.get)
  print("Most frequent word:", most_frequent)
  ```

- **Output**:
  ```
  Most frequent word: apple
  ```

---

#### **6. Write a Program to Merge Two Dictionaries**

- **Objective**: Combine the contents of two dictionaries.
- **Example**:

  ```python
  dict1 = {"a": 1, "b": 2}
  dict2 = {"c": 3, "d": 4}

  # Merging dictionaries
  merged_dict = {**dict1, **dict2}
  print("Merged Dictionary:", merged_dict)
  ```

- **Output**:
  ```
  Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  ```

---

#### **7. Create a Set and Perform Union and Intersection Operations**

- **Objective**: Use sets to demonstrate `union` and `intersection`.
- **Example**:

  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}

  union_set = set1 | set2
  intersection_set = set1 & set2

  print("Union:", union_set)
  print("Intersection:", intersection_set)
  ```

- **Output**:
  ```
  Union: {1, 2, 3, 4, 5}
  Intersection: {3}
  ```

---

#### **8. Write a Program to Count Occurrences of Each Word in a String**

- **Objective**: Use a dictionary to track word counts in a sentence.
- **Example**:

  ```python
  sentence = "this is a test this is only a test"
  words = sentence.split()
  word_count = {}

  for word in words:
      word_count[word] = word_count.get(word, 0) + 1

  print("Word Occurrences:", word_count)
  ```

- **Output**:
  ```
  Word Occurrences: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
  ```

---

#### **9. Build a Script to Find the Second Largest Number in a List**

- **Objective**: Use Python’s sorting and indexing to find the second largest element.
- **Example**:
  ```python
  numbers = [10, 20, 4, 45, 99]
  unique_numbers = list(set(numbers))  # Remove duplicates
  unique_numbers.sort()
  second_largest = unique_numbers[-2]
  print("Second Largest Number:", second_largest)
  ```
- **Output**:
  ```
  Second Largest Number: 45
  ```

---

#### **10. Create a Nested Dictionary to Store Student Grades**

- **Objective**: Use a dictionary of dictionaries to represent student data.
- **Example**:

  ```python
  students = {
      "Alice": {"Math": 90, "Science": 85},
      "Bob": {"Math": 75, "Science": 80},
      "Charlie": {"Math": 95, "Science": 92}
  }

  for student, grades in students.items():
      print(f"{student}'s Grades:")
      for subject, grade in grades.items():
          print(f"  {subject}: {grade}")
  ```

- **Output**:
  ```
  Alice's Grades:
    Math: 90
    Science: 85
  Bob's Grades:
    Math: 75
    Science: 80
  Charlie's Grades:
    Math: 95
    Science: 92
  ```
