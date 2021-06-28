from datetime import datetime

year =[]
for i in range(2000,datetime.now().year +1):
    year.append((i,i))
print(year)