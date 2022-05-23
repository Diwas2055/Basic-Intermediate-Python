import html


# ? html.unescape:- Converting HTML entities to their corresponding characters.
print(html.unescape('&pound;682m'))
print(html.unescape('&copy; 2010'))

# Beautiful Soup 4
# Importing the BeautifulSoup class from the bs4 module.
from bs4 import BeautifulSoup
soup = BeautifulSoup("<strong>Some</strong> bad <b>HTML</b>", "html.parser")
# Removing all the HTML tags and returning the text.
print(soup.get_text())