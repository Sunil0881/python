import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Find all the images on the page
images = []
for img in soup.find_all("img"):
    images.append(img.get("src"))

# Find the page title
title = soup.title.string

# Print the result
print("Links:")
for link in links:
    print(link)

print("\nImages:")
for image in images:
    print(image)

print("\nTitle:")
print(title)
