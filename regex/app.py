import re

txt = "The rain in Spain"

# todo:- findall() function returns a list containing all matches
x = re.findall("ai", txt)
print(x)

# todo:- search() function searches the string for a match, and returns a Match object if there is a match
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
x = re.search("Portugal", txt)
print(x)


