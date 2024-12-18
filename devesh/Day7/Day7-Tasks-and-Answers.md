### **Day 7: APIs and Data Processing**

**Objective**: Master consuming APIs and processing data programmatically.

---

### **Topics Covered**

#### **1. Introduction to APIs and JSON**

- **APIs (Application Programming Interfaces)**:

  - **Definition**: APIs allow applications to communicate with each other by using a set of rules. They enable functionalities like retrieving data, posting data, and managing resources on a server.
  - **Why APIs?**: They allow integration with external services like weather data, social media, or financial data, without the need to build those functionalities from scratch.

- **JSON (JavaScript Object Notation)**:
  - **What is JSON?**: JSON is a lightweight data format that is easy to read and write for humans and is easily parseable by machines. It’s a common format used for data interchange in APIs.
  - **Example JSON Structure**:
    ```json
    {
      "name": "John Doe",
      "age": 30,
      "is_student": false,
      "skills": ["Python", "JavaScript", "HTML"]
    }
    ```

#### **2. Using the `requests` Library to Interact with APIs**

- **Why `requests`?**:
  - The `requests` library is simple to use and handles the complexities of making HTTP requests, like cookies, headers, and connections.
- **Sending HTTP Requests**:

  - **GET Request**:

    ```python
    import requests

    url = "https://api.example.com/data"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
    ```

  - **POST Request**:

    ```python
    url = "https://api.example.com/data"
    payload = {'name': 'Alice', 'age': 25}
    response = requests.post(url, json=payload)

    if response.status_code == 201:  # Created
        print("Data successfully added.")
    ```

- **Error Handling**:
  - Using `response.raise_for_status()` to raise an exception for HTTP errors.
    ```python
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    ```

#### **3. Reading and Writing JSON Data**

- **Reading JSON**:

  - Load JSON from a file:

    ```python
    import json

    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    ```

- **Writing JSON**:

  - Write data to a file:

    ```python
    data = {"name": "Alice", "age": 25, "is_student": True}

    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)  # Pretty print with indentation
    ```

#### **4. Authentication Mechanisms (API Keys, OAuth)**

- **API Keys**:

  - Some APIs require an API key for authentication:
    ```python
    headers = {'Authorization': 'Bearer YOUR_API_KEY'}
    response = requests.get(url, headers=headers)
    ```

- **OAuth**:

  - OAuth is used for secure authentication.

    ```python
    auth_url = 'https://api.example.com/oauth/authorize'
    token_url = 'https://api.example.com/oauth/token'
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'

    # Step 1: Redirect to the authorization URL
    auth_response = requests.get(auth_url, params={'client_id': client_id})

    # Step 2: Exchange authorization code for access token
    token_data = {
        'code': auth_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code'
    }
    token_response = requests.post(token_url, data=token_data)

    access_token = token_response.json()['access_token']
    ```

#### **5. Handling API Rate Limits and Errors**

- **Rate Limits**:

  - APIs often impose limits on the number of requests you can make:

    ```python
    import time

    for i in range(5):  # Try 5 times
        response = requests.get(url)
        if response.status_code == 429:  # Too Many Requests
            print("Rate limit exceeded. Retrying...")
            time.sleep(10)  # Wait before retrying
    ```

- **Error Handling**:
  - Implement robust error handling to manage unexpected issues such as network failures, timeouts, or server errors:
    ```python
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    ```

#### **6. Parsing and Filtering JSON Responses**

- **Parsing JSON**:

  - Extract specific data from the JSON response:

    ```python
    response = requests.get(url)
    data = response.json()

    # Access specific fields
    print(data['name'])
    print(data['age'])
    ```

- **Filtering Data**:
  - Extract items based on specific conditions:
    ```python
    for item in data['items']:
        if item['price'] > 100:
            print(item['name'], item['price'])
    ```

#### **7. Working with Real-World APIs**

- **Weather API**:

  - Retrieve current weather data:
    ```python
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": "London", "appid": "YOUR_API_KEY"}
    response = requests.get(weather_url, params=params)
    print(response.json())
    ```

- **Finance API**:
  - Fetch stock market data:
    ```python
    finance_url = "https://api.example.com/stock"
    params = {"symbol": "AAPL", "apikey": "YOUR_API_KEY"}
    response = requests.get(finance_url, params=params)
    print(response.json())
    ```

#### **8. Introduction to `pandas` for Data Processing**

- **Why `pandas`?**:
  - `pandas` is essential for data manipulation, allowing you to handle structured data like JSON and CSV files with ease.
- **Basic Operations**:

  - **Creating DataFrames**:

    ```python
    import pandas as pd

    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    print(df)
    ```

  - **Viewing Data**:
    ```python
    print(df.head())  # Display the first few rows of the DataFrame
    print(df.tail())  # Display the last few rows of the DataFrame
    ```

- **Filtering Data**:

  - Select rows based on conditions:
    ```python
    filtered_df = df[df['Age'] > 25]
    print(filtered_df)
    ```

- **Grouping Data**:
  - Group data by a column and perform aggregation:
    ```python
    grouped_df = df.groupby('Age').mean()
    print(grouped_df)
    ```

#### **9. Filtering and Grouping Data in `pandas`**

- **Filtering Data**:

  - Extract rows where conditions are met:

    ```python
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 35, 45],
        'city': ['New York', 'Chicago', 'Los Angeles']
    }
    df = pd.DataFrame(data)

    # Filter by age greater than 30
    filtered_df = df[df['age'] > 30]
    print(filtered_df)
    ```

- **Grouping and Aggregating Data**:
  - Group data by a column and apply functions:
    ```python
    grouped_df = df.groupby('city').mean()
    print(grouped_df)
    ```

#### **10. Exporting Processed Data to Excel or CSV**

- **Exporting to CSV**:

  - Write DataFrames to a CSV file:
    ```python
    df.to_csv('output.csv', index=False)  # Write without index
    ```

- **Exporting to Excel**:
  - Write DataFrames to an Excel file:
    ```python
    df.to_excel('output.xlsx', index=False)  # Write without index
    ```

---

### **Hands-On Tasks**

---

1. **Fetch data from a public API and print the response**:

   - **Task**: Write a Python script to send a GET request to the OpenWeatherMap API and print the JSON response.
   - **Example**:

     ```python
     import requests

     city = "London"
     api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

     response = requests.get(base_url)
     if response.status_code == 200:
         print(response.json())  # Print the JSON response
     else:
         print(f"Failed to fetch data: {response.status_code}")
     ```

2. **Parse and extract specific fields from an API response**:

   - **Task**: Write a script to parse the JSON response from the OpenWeatherMap API and extract fields like temperature, humidity, and weather description.
   - **Example**:

     ```python
     data = response.json()
     temperature = data['main']['temp']
     humidity = data['main']['humidity']
     weather_description = data['weather'][0]['description']

     print(f"Temperature: {temperature}K")
     print(f"Humidity: {humidity}%")
     print(f"Weather: {weather_description}")
     ```

3. **Write a script to fetch and display weather data for a given city**:

   - **Task**: Modify the script to take a city name as input and fetch weather data for that city.
   - **Example**:

     ```python
     city = input("Enter city name: ")
     api_key = "your_api_key_here"
     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

     response = requests.get(base_url)
     if response.status_code == 200:
         data = response.json()
         temperature = data['main']['temp']
         humidity = data['main']['humidity']
         weather_description = data['weather'][0]['description']

         print(f"Weather in {city}: {weather_description}")
         print(f"Temperature: {temperature}K")
         print(f"Humidity: {humidity}%")
     else:
         print(f"Failed to get weather data for {city}. Status code: {response.status_code}")
     ```

4. **Build a script to download stock market data from an API**:

   - **Task**: Write a script to fetch stock market data for a given stock symbol using a financial API like Alpha Vantage.
   - **Example**:

     ```python
     import requests

     stock_symbol = "AAPL"  # Apple Inc.
     api_key = "your_api_key_here"  # Replace with your Alpha Vantage API key
     base_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}"

     response = requests.get(base_url)
     if response.status_code == 200:
         data = response.json()
         time_series = data['Time Series (5min)']
         latest_time = max(time_series.keys())
         latest_data = time_series[latest_time]

         print(f"Latest data for {stock_symbol}:")
         print(f"Time: {latest_time}")
         print(f"Open: {latest_data['1. open']}")
         print(f"High: {latest_data['2. high']}")
         print(f"Low: {latest_data['3. low']}")
         print(f"Close: {latest_data['4. close']}")
     else:
         print(f"Failed to fetch stock data for {stock_symbol}. Status code: {response.status_code}")
     ```

5. **Handle rate limits in API requests using `time.sleep`**:

   - **Task**: Modify the script to include a delay if an API request fails due to a rate limit.
   - **Example**:

     ```python
     import requests
     import time

     api_key = "your_api_key_here"
     base_url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"

     for i in range(1, 6):
         response = requests.get(base_url)
         if response.status_code == 200:
             print(response.json())
         else:
             print(f"Failed to fetch data: {response.status_code}. Retrying...")
             time.sleep(5)  # Wait for 5 seconds before retrying
     ```

6. **Write a script to process JSON data and save it as a CSV file**:

   - **Task**: Parse a JSON response from an API and write selected data fields to a CSV file.
   - **Example**:

     ```python
     import csv

     data = response.json()
     filename = "weather_data.csv"

     with open(filename, 'w', newline='') as csvfile:
         fieldnames = ['city', 'temperature', 'humidity', 'weather']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

         writer.writeheader()
         writer.writerow({
             'city': data['name'],
             'temperature': data['main']['temp'],
             'humidity': data['main']['humidity'],
             'weather': data['weather'][0]['description']
         })
     ```

7. **Use pandas to filter rows in a dataset**:

   - **Task**: Use pandas to filter and manipulate a dataset fetched from an API.
   - **Example**:

     ```python
     import pandas as pd

     data = response.json()
     df = pd.DataFrame(data['list'])  # Assuming 'list' is the key for weather data entries

     # Filter rows where temperature is above a certain value
     filtered_df = df[df['main']['temp'] > 300]
     print(filtered_df)
     ```

8. **Create a summary report of sales data using pandas**:

   - **Task**: Aggregate sales data to create a summary report.
   - **Example**:

     ```python
     sales_data = {
         'product': ['Product A', 'Product B', 'Product C'],
         'sales': [100, 150, 120],
         'quantity': [20, 30, 25]
     }

     df = pd.DataFrame(sales_data)
     summary = df.groupby('product').agg(total_sales=('sales', 'sum'), total_quantity=('quantity', 'sum'))
     print(summary)
     ```

9. **Fetch real-time exchange rates from an API and convert currencies**:

   - **Task**: Use an API to get real-time exchange rates and convert between currencies.
   - **Example**:

     ```python
     import requests

     base_currency = "USD"
     target_currency = "EUR"
     api_key = "your_api_key_here"  # Replace with your exchange rate API key
     base_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

     response = requests.get(base_url)
     if response.status_code == 200:
         data = response.json()
         exchange_rate = data['rates'][target_currency]
         amount_in_usd = 100
         converted_amount = amount_in_usd * exchange_rate
         print(f"{amount_in_usd} USD is equal to {converted_amount:.2f} {target_currency}")
     else:
         print(f"Failed to fetch exchange rates. Status code: {response.status_code}")
     ```

10. **Automate sending API requests using a loop**:

- **Task**: Write a script that sends a batch of API requests to an endpoint in a loop.
- **Example**:

  ```python
  import requests
  import time

  api_key = "your_api_key_here"
  base_url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"

  for i in range(1, 6):  # Loop through 5 different cities
      response = requests.get(base_url)
      if response.status_code == 200:
          data = response.json()
          print(f"Data for city {i}: {data}")
      else:
          print(f"Failed to fetch data for city {i}: {response.status_code}")
          time.sleep(5)  # Wait for 5 seconds before retrying
  ```
