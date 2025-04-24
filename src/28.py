import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # Replace with the actual URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: find a specific element on the page
element = soup.find('div', {'class': 'my-class'})
if element:
    print(element.get_text())
else:
    print("Element not found")
