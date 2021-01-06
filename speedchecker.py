from datetime import datetime
import os

# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# run network speedtest
os.system("/usr/local/Cellar/speedtest-cli/2.1.2/bin/speedtest-cli")

# insert line break
print('\n'*1)
