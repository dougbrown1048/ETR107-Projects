# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:46:52 2020

@author: dougb
"""

import time

days = (time.time()/60/60//24)

hours = ((time.time()/60//60) - days * 24)

minutes = (((time.time()//60)) - (days * 24 * 60 + hours * 60))

seconds = int((time.time() - (days *24 * 60 * 60 + hours * 60 * 60 + minutes * 60)))

print("The current time is: " + str(hours) + " hours " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
print("It is " + str(days) + " days since the beginning of the epoch.")
