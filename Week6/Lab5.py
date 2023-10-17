# Lab4
# Author: 

"""_summary_
This lab is designed to get you familiar with Python virtual environments as well as import statments to use external libraries.
"""

# 1. Create a virtual environment called "venv" in the current directory. (Type command here in comments)

#run in terminal: python -m venv venv

# 2. Activate the virtual environment. (Type command here in comments)

#run in terminal: source venv/bin/activate

# 3. Install the requests library. (Type command here in comments)

#pip install requests


# 4. import requests library here

import requests

# 5. Use the requests library to make a GET request to https://api.github.com/events


url = "https://api.github.com/events"

# 6. Print out the status code of the response.
response = requests.get(url)

print(f"Status Code: {response.status_code}")


# 7. Print out the content of the response.

if response.status_code == 200:
    # Print the content of the response
    print("Response Content:")
    print(response.text)

# 8. Print out the headers of the response.

if response.status_code == 200:
  
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

# 9. Deactivate the virtual environment. (Type command here in comments)

#deactivate