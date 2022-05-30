from datetime import date
from datetime import datetime

today = date.today()
  
# dd/mm/YY

date1 = today.strftime("%d/%m/%Y")
print("date1 =", date1)
  
# Textual month, day and year	

date2 = today.strftime("%B %d, %Y")
print("date2 =", date2)
  
# mm/dd/y

date3 = today.strftime("%m/%d/%y")
print("date3 =", date3)
  
# Month abbreviation, day and year	

date4 = today.strftime("%b-%d-%Y")
print("date4 =", date4)

# Current date and time object

now = datetime.now()
   
print("now() time =", now)
  
# dd/mm/YY H:M:S

currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")
print("Current Date and Time =", currentDateTime)