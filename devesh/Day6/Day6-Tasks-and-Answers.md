### **Day 6: Web Scraping with Python**

Web scraping is the process of extracting data from websites, which can be highly useful for automation and data analysis. This session introduces the fundamental concepts, tools, and techniques for scraping websites using Python.

---

### **Topics Covered**

---

#### **1. Introduction to Web Scraping and Its Legal Considerations**

- **Definition**: Web scraping involves programmatically extracting data from websites.
- **Legal Considerations**: Always ensure you respect the terms of service of the website you’re scraping. Avoid scraping personal or sensitive information, and use polite scraping practices (e.g., obey `robots.txt`).

---

#### **2. Overview of the `requests` Library**

- The `requests` library is used to send HTTP requests and fetch web pages.

**Example**: Fetch a webpage’s HTML.

```python
import requests

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)  # Prints the HTML of the page
else:
    print(f"Failed to fetch page: {response.status_code}")
```

---

#### **3. HTML Basics: Tags, Elements, and Attributes**

- **HTML Structure**:
  ```html
  <html>
    <head>
      <title>Page Title</title>
    </head>
    <body>
      <h1 class="title">Welcome</h1>
      <p id="description">This is a description.</p>
    </body>
  </html>
  ```
- **Key Concepts**:
  - Tags: `<h1>`, `<p>`, `<a>`, etc.
  - Attributes: `class`, `id`, `href`, etc.

---

#### **4. Parsing HTML with `BeautifulSoup`**

The `BeautifulSoup` library simplifies HTML parsing.

**Example**:

```python
from bs4 import BeautifulSoup

html = '<h1 class="title">Welcome</h1><p id="description">This is a description.</p>'
soup = BeautifulSoup(html, 'html.parser')

print(soup.h1.text)  # Outputs: Welcome
print(soup.find('p').text)  # Outputs: This is a description.
```

---

#### **5. Extracting Data Using Tags, Classes, and IDs**

Use methods like `find`, `find_all`, and CSS selectors to extract specific elements.

**Example**: Extract all links.

```python
html = '<a href="https://example.com">Example</a><a href="https://another.com">Another</a>'
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
for link in links:
    print(link['href'])  # Prints each link's href
```

---

#### **6. Handling Pagination in Web Scraping**

Pagination involves navigating through multiple pages of a website.

**Example**: Scrape multiple pages by iterating through page URLs.

```python
base_url = 'https://example.com/page='
for page in range(1, 6):  # Pages 1 to 5
    url = f"{base_url}{page}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Scraping page {page}")
```

---

#### **7. Writing Scraped Data to CSV Files**

Use the `csv` module to save extracted data for analysis.

**Example**:

```python
import csv

data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to output.csv")
```

---

#### **8. Introduction to `selenium` for Dynamic Pages**

Some websites use JavaScript to load content, requiring a browser automation tool like `selenium`.

**Example**:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://example.com')

# Extract dynamic content
content = driver.find_element('css selector', '.dynamic-class').text
print(content)

driver.quit()
```

---

#### **9. Error Handling in Web Scraping**

Gracefully handle errors like timeouts, invalid URLs, or missing elements.

**Example**:

```python
import requests

try:
    response = requests.get('https://invalid-url.com', timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
```

---

#### **10. Using `time` and `random` to Avoid Detection**

Avoid detection by introducing delays between requests.

**Example**:

```python
import time
import random

urls = ['https://example.com/page1', 'https://example.com/page2']

for url in urls:
    response = requests.get(url)
    print(f"Scraped {url}")
    time.sleep(random.uniform(1, 3))  # Random delay between 1-3 seconds
```

---

### **Hands-On Tasks**

---

#### **1. Write a Script to Fetch HTML Content from a URL**

Use the `requests` library to fetch HTML content from a webpage.

**Script**:

```python
import requests

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)  # Prints the HTML content
else:
    print(f"Failed to fetch the webpage: {response.status_code}")
```

---

#### **2. Parse and Extract Titles from a Sample Webpage**

Use `BeautifulSoup` to parse the HTML and extract the `<title>` tag.

**Script**:

```python
from bs4 import BeautifulSoup

html = '<html><head><title>Sample Title</title></head><body></body></html>'
soup = BeautifulSoup(html, 'html.parser')

title = soup.title.text
print(f"Page Title: {title}")
```

---

#### **3. Scrape and Save Product Data from an E-Commerce Site**

Extract product names and prices from an e-commerce webpage.

**Script**:

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='product')

for product in products:
    name = product.find('h2').text
    price = product.find('span', class_='price').text
    print(f"Product: {name}, Price: {price}")
```

---

#### **4. Build a Script to Scrape Quotes and Authors from a Webpage**

Scrape quotes and authors from a quotes website.

**Script**:

```python
url = 'https://example.com/quotes'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" - {author}')
```

---

#### **5. Handle Pagination to Scrape Multiple Pages**

Iterate through pages to scrape data.

**Script**:

```python
base_url = 'https://example.com/products?page='
for page in range(1, 6):  # Pages 1 to 5
    url = f"{base_url}{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='product')
    for product in products:
        name = product.find('h2').text
        price = product.find('span', class_='price').text
        print(f"Page {page}: {name}, {price}")
```

---

#### **6. Write Scraped Data to a CSV File**

Save extracted data to a CSV file using the `csv` module.

**Script**:

```python
import csv

data = [
    ['Product Name', 'Price'],
    ['Sample Product 1', '$10'],
    ['Sample Product 2', '$20'],
]

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data saved to products.csv")
```

---

#### **7. Scrape Image URLs from a Website and Download Them**

Extract image URLs and download the images.

**Script**:

```python
import requests
from bs4 import BeautifulSoup
import os

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
os.makedirs('images', exist_ok=True)

for img in images:
    img_url = img['src']
    img_data = requests.get(img_url).content
    img_name = os.path.basename(img_url)

    with open(f'images/{img_name}', 'wb') as file:
        file.write(img_data)
        print(f"Downloaded: {img_name}")
```

---

#### **8. Automate Login to a Website Using `selenium`**

Use `selenium` to automate login.

**Script**:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://example.com/login')

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys('your_username')
password.send_keys('your_password')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

print("Login successful")
driver.quit()
```

---

#### **9. Handle Errors and Retry Failed Requests in a Script**

Use `try-except` blocks to handle errors and retry requests.

**Script**:

```python
import requests
import time

url = 'https://example.com'
retries = 3

for attempt in range(retries):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("Page fetched successfully")
        break
    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt + 1}: Failed ({e})")
        time.sleep(2)
else:
    print("All retries failed")
```

---

#### **10. Build a Script to Scrape Weather Data from a Weather Website**

Extract and display weather information.

**Script**:

```python
url = 'https://example.com/weather'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

weather_data = soup.find('div', class_='weather')
temperature = weather_data.find('span', class_='temp').text
condition = weather_data.find('span', class_='condition').text

print(f"Temperature: {temperature}, Condition: {condition}")
```
