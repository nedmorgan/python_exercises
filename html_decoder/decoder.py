from bs4 import BeautifulSoup
import requests
import simplejson as json

# This is the url that I want to scrape
page_link = 'https://www.nytimes.com/'

# This will fetch the contents of the wepage
page_response = requests.get(page_link, timeout=5)

#This will prase the html content of the webpage
page_content = BeautifulSoup(page_response.content, "html.parser")

headerContent = []
for i in range(0, 32):
    headers = page_content.find_all("h2")[i].text
    headerContent.append({"header": headers})

listItems = []
for i in range(0, 201):
  items = page_content.find_all("li")[i].text
  listItems.append(items)

def set_default(obj):
  if isinstance(obj, set):
      return list(obj)
  raise TypeError

data = json.dumps({'headers': headerContent}, separators=(',', ':'), indent=4 * ' ', default=set_default)

with open('data.json', 'w') as fp:
    json.dump(data, fp)

# print(headerContent)

# def printItems():
#   print("There are all the headers: ")
#   for index, i in enumerate(headerContent, start = 1):
#     print(str(index) + ": " + str(i))
#   print("There are all the list content items: ")
#   for index, i in enumerate(listItems, start = 1):
#     print(str(index) + ": " + str(i))

# printItems()

