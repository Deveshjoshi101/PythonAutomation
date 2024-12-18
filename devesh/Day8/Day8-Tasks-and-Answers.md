### **Day 8: GUI Automation with Selenium**

**Objective**: Learn to automate web-based tasks using Selenium.

**Topics Covered:**

1. **Introduction to Selenium and web drivers**:

   - **What is Selenium**: Selenium is an open-source tool used for automating web applications. It allows you to control web browsers through a programming interface. Selenium supports multiple browsers, including Chrome, Firefox, and Safari, and can automate web applications across various operating systems.
   - **Components of Selenium**:
     - **WebDriver**: Acts as the bridge between Selenium and the browser, sending commands and retrieving results.
     - **Selenium Grid**: Allows running tests on different browsers and operating systems simultaneously.
     - **Selenium IDE**: A browser extension that records and plays back user actions.
   - **Why use Selenium**: Automation of web tasks, browser testing, crawling, and integration with CI/CD pipelines for automated testing.
   - **Example**:

     ```python
     from selenium import webdriver

     driver = webdriver.Chrome(executable_path='path_to_chromedriver')
     ```

2. **Setting up Selenium with ChromeDriver**:

   - **Downloading and installing ChromeDriver**:
     - Visit the official ChromeDriver website and download the appropriate version for your Chrome browser version.
     - Place the downloaded ChromeDriver executable in a suitable directory (e.g., the script's directory).
   - **Path configuration**:
     - Configure the path to the ChromeDriver executable in your script to enable Selenium to find it.
   - **Starting the web driver**:
     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     ```

3. **Locating elements using `id`, `class`, `name`, and XPath**:

   - **Finding elements by `id`**:
     - The `id` attribute uniquely identifies an HTML element.
     - Example:
       ```python
       element = driver.find_element_by_id('element_id')
       ```
   - **Finding elements by `class`**:
     - The `class` attribute allows you to locate elements with a specific class name.
     - Example:
       ```python
       element = driver.find_element_by_class_name('element_class')
       ```
   - **Finding elements by `name`**:
     - The `name` attribute can be used to locate elements by their name attribute.
     - Example:
       ```python
       element = driver.find_element_by_name('element_name')
       ```
   - **Finding elements using XPath**:
     - XPath allows you to locate elements based on their attributes and hierarchy.
     - **Absolute XPath**: Navigates from the root of the XML to the desired element.
       ```python
       element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/a')
       ```
     - **Relative XPath**: Uses `//` to start searching anywhere in the document.
       ```python
       element = driver.find_element_by_xpath('//div[@class="example_class"]/a')
       ```

4. **Interacting with input fields, buttons, and dropdowns**:

   - **Sending text to input fields**:
     - To enter text into input fields, use the `send_keys()` method.
     ```python
     input_field = driver.find_element_by_name('username')
     input_field.send_keys('test_user')
     ```
   - **Clicking buttons**:
     - To click a button, use the `click()` method.
     ```python
     submit_button = driver.find_element_by_name('submit')
     submit_button.click()
     ```
   - **Selecting options in dropdowns**:

     - Use the `Select` class to work with dropdown menus.

     ```python
     from selenium.webdriver.support.ui import Select

     dropdown = Select(driver.find_element_by_name('dropdown_name'))
     dropdown.select_by_value('option_value')
     ```

5. **Handling alerts and popups**:

   - **Switching to alerts**:
     - Selenium handles JavaScript alerts through the `switch_to.alert` method.
     ```python
     alert = driver.switch_to.alert
     alert.accept()  # Accept the alert
     alert.dismiss()  # Dismiss the alert
     ```
   - **Working with confirm dialogs**:
     - Similar to alerts but requires interaction for confirmation.
     ```python
     confirm = driver.switch_to.alert
     confirm.dismiss()  # Dismiss the dialog
     ```

6. **Automating form submissions**:

   - **Filling out forms**:

     - Locate form elements using their names or IDs and send keys to each field.

     ```python
     username_field = driver.find_element_by_name('username')
     password_field = driver.find_element_by_name('password')
     submit_button = driver.find_element_by_name('login')

     username_field.send_keys('test_user')
     password_field.send_keys('secure_password')
     submit_button.click()
     ```

7. **Extracting data from dynamic pages**:

   - **Handling dynamic content**:

     - Use `WebDriverWait` and `expected_conditions` to wait for elements to become visible before interacting with them.

     ```python
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC

     data_element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, 'dynamic_element_id'))
     )
     print(data_element.text)
     ```

   - **Scrolling to load content**:
     - Use JavaScript to scroll down and load more content.
     ```python
     driver.execute_script("arguments[0].scrollIntoView();", data_element)
     ```

8. **Taking screenshots of web pages**:

   - **Capturing screenshots**:
     - Selenium allows you to take screenshots of web pages.
     ```python
     driver.save_screenshot('screenshot.png')
     ```

9. **Waiting for elements with `time.sleep` and `WebDriverWait`**:

   - **Using `time.sleep`**:
     - Delays the script execution for a given number of seconds.
     ```python
     time.sleep(5)  # Wait for 5 seconds
     ```
   - **Using `WebDriverWait`**:
     - Waits for a specific condition to be met before proceeding.
     ```python
     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, 'element_id'))
     )
     ```

10. **Error handling and debugging in Selenium scripts**:

- **Exception handling**:
  - Use try-except blocks to catch exceptions and handle them gracefully.
  ```python
  try:
      driver.find_element_by_name('missing_element').click()
  except NoSuchElementException:
      print("Element not found")
  ```
- **Debugging tips**:
  - Print stack traces for better error analysis.
  - Use `driver.get_log('browser')` to view browser logs.
  - Implement try-except blocks to catch and handle exceptions effectively.

---

### **Hands-On Tasks:**

---

1. **Automate a Google search and extract results**:

   - **Objective**: Write a script to automate a Google search and extract the search results.
   - **Example**:

     ```python
     from selenium import webdriver
     from selenium.webdriver.common.keys import Keys

     # Setup the driver
     driver = webdriver.Chrome('path_to_chromedriver')

     # Open Google
     driver.get('https://www.google.com')

     # Find the search input field, enter a query, and submit
     search_box = driver.find_element_by_name('q')
     search_box.send_keys('OpenAI ChatGPT')
     search_box.send_keys(Keys.RETURN)

     # Extract search results
     results = driver.find_elements_by_css_selector('h3 > a')
     for result in results[:5]:  # Limit to first 5 results for example
         print(result.get_attribute('href'))  # Print the link
         print(result.text)  # Print the title

     driver.quit()
     ```

2. **Fill and submit a sample web form automatically**:

   - **Objective**: Automate filling out and submitting a sample web form.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/contact-form')

     # Locate form elements
     name_field = driver.find_element_by_name('name')
     email_field = driver.find_element_by_name('email')
     submit_button = driver.find_element_by_name('submit')

     # Fill out the form
     name_field.send_keys('John Doe')
     email_field.send_keys('johndoe@example.com')
     submit_button.click()

     driver.quit()
     ```

3. **Write a script to log in to a website and scrape user-specific data**:

   - **Objective**: Automate the login process and extract user-specific information after logging in.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/login')

     # Locate login fields and submit credentials
     username_field = driver.find_element_by_name('username')
     password_field = driver.find_element_by_name('password')
     login_button = driver.find_element_by_name('login')

     username_field.send_keys('test_user')
     password_field.send_keys('secure_password')
     login_button.click()

     # Scrape user-specific data after login
     user_data = driver.find_element_by_id('user_data').text
     print(user_data)

     driver.quit()
     ```

4. **Automate selecting options from a dropdown menu**:

   - **Objective**: Select options from a dropdown menu on a webpage.
   - **Example**:

     ```python
     from selenium.webdriver.support.ui import Select

     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/dropdown-page')

     dropdown = Select(driver.find_element_by_name('options'))
     dropdown.select_by_value('option_value')

     driver.quit()
     ```

5. **Handle a JavaScript alert and close it**:

   - **Objective**: Write a script to handle JavaScript alerts on a webpage.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/alert-page')

     # Trigger alert
     trigger_alert_button = driver.find_element_by_name('trigger_alert')
     trigger_alert_button.click()

     # Handle the alert
     alert = driver.switch_to.alert
     alert.accept()  # Accept the alert

     driver.quit()
     ```

6. **Scrape dynamic content from an infinite scroll webpage**:

   - **Objective**: Automate scrolling and scraping content from an infinite scroll webpage.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/infinite-scroll-page')

     while True:
         last_height = driver.execute_script('return document.body.scrollHeight')
         driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
         time.sleep(2)  # Wait for new content to load

         new_height = driver.execute_script('return document.body.scrollHeight')
         if new_height == last_height:
             break

     # Extract dynamic content
     elements = driver.find_elements_by_class_name('dynamic-content')
     for element in elements:
         print(element.text)

     driver.quit()
     ```

7. **Take a screenshot of a webpage using Selenium**:

   - **Objective**: Capture a screenshot of a webpage.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/screenshot-page')

     # Take a screenshot
     driver.save_screenshot('screenshot.png')

     driver.quit()
     ```

8. **Build a script to extract table data from a webpage**:

   - **Objective**: Extract data from a table on a webpage.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/table-page')

     table = driver.find_element_by_tag_name('table')
     rows = table.find_elements_by_tag_name('tr')

     for row in rows:
         columns = row.find_elements_by_tag_name('td')
         for col in columns:
             print(col.text)

     driver.quit()
     ```

9. **Automate file downloads using Selenium**:

   - **Objective**: Automate downloading files from a webpage.
   - **Steps**:
     1. Click on the download link/button.
     2. Wait for the download to complete.
   - **Example**:

     ```python
     driver = webdriver.Chrome('path_to_chromedriver')
     driver.get('https://example.com/download-page')

     download_link = driver.find_element_by_link_text('Download File')
     download_link.click()

     # Wait for the file to download
     time.sleep(5)  # Adjust the sleep time as needed

     driver.quit()
     ```

10. **Implement error handling for missing web elements**:

- **Objective**: Write a script to handle cases where a web element is not found.
- **Steps**:
  1.  Use try-except blocks to catch `NoSuchElementException`.
  2.  Provide a fallback or log an error message.
- **Example**:

  ```python
  driver = webdriver.Chrome('path_to_chromedriver')
  driver.get('https://example.com/page-with-element')

  try:
      element = driver.find_element_by_name('missing_element')
      element.click()
  except NoSuchElementException:
      print("Element not found on the page")

  driver.quit()
  ```
