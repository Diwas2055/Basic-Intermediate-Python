# List Article  from DEV API 
from pprint import pprint
import sys
import requests
import json

limit=input("Enter the limit: ")

list_articles=requests.get(f"https://dev.to/api/articles?per_page={limit}")
list_articles=list_articles.json()

print("Number of Articles",len(list_articles))

# for list_article in list_articles:

# The above code is creating a json file with the list of articles.
with open('web-scrapping/article.json', 'w') as json_file:
  json.dump(list_articles, json_file)
  json_file.close()
  print("File created in Json format")