#!/usr/bin/env python

__author__ = "Jeremiah Roe (C1ph3rFlux)"
__copyright__ = "Copyright 2021, Jeremiah Roe"
__credits__ = ["Jeremiah Roe, Maybe You?"]
__license__ = "MIT"
__version__ = "N/A"
__maintainer__ = "Jeremiah Roe (C1ph3rFlux)"
__email__ = "c1ph3rflux@gmail.com"

from datetime import datetime
import os

# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# run network speedtest (Need to edit for your location of "speedtest-cli")
os.system("/Add/Location/Of/Your/Installation/Of/speedtest-cli")

# insert line break
print('\n'*1)
