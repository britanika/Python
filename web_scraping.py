import requests
from bs4 import BeautifulSoup
import json

# Make an HTTP request to the website
response = requests.get('https://www.example.com/')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract desired data (e.g., titles and links)
data = []
for item in soup.find_all('a'):
    data.append({
        'title': item.text,
        'link': item.get('href')
    })

# Write data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
