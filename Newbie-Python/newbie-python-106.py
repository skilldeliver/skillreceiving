from datetime import datetime
from datetime import timedelta
date = datetime.strptime(input(), '%d-%m-%Y')
date = date + timedelta(days = 1000)
print(datetime.strftime(date, '%d-%m-%Y'))




