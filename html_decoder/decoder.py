from bs4 import BeautifulSoup
import requests
import sys

# This is the url that I was to scrape
page_link = 'https://www.nytimes.com/'

# This will fetch the contents of the wepage
page_response = requests.get(page_link, timeout=5)

#This will prase the html content of the webpage
page_content = BeautifulSoup(page_response.content, "html.parser")

headerContent = []
for i in range(0, 27):
    headers = page_content.find_all("h2")[i].text
    headerContent.append(headers)

listItems = []
for i in range(0, 195):
  items = page_content.find_all("li")[i].text
  listItems.append(items)

def printItems():
  print("There are all the headers: ")
  for index, i in enumerate(headerContent, start = 1):
    print(str(index) + ": " + str(i))
  print("There are all the list content items: ")
  for index, i in enumerate(listItems, start = 1):
    print(str(index) + ": " + str(i))

printItems()

