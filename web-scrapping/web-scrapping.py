from pprint import pprint
import sys
import requests
import json

# List Article  from DEV API 
limit=input("Enter the limit: ")
list_articles=requests.get(f"https://dev.to/api/articles?per_page={limit}")
list_articles=list_articles.json()

print("Number of Articles",len(list_articles))

# for list_article in list_articles:

with open('web-scrapping/article.json', 'w') as json_file:
  json.dump(list_articles, json_file)
  json_file.close()
  print("File created in Json format")