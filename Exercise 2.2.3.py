# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:39:18 2020

@author: dougb
"""

elapsedSecs = 2 * ((8 * 60) + 15) + 3 * ((7 * 60) + 12)
# total run time in seconds

elapsedMins = elapsedSecs / 60
# total run time in minutes

elapsedMinsInt = int(elapsedMins)
# just the number of minutes without additioal seconds

additionalSecsInt = int(((elapsedMins - int(elapsedMins)) * 60))
# additional fractional minute expressed as seconds

finishMinute = 52 + elapsedMinsInt - 60
# the run started at 52 minutes after the hour

def timeFunction():
    if additionalSecsInt < 10:
        print("8:" + str(finishMinute) + ":0" + str(additionalSecsInt))
    if additionalSecsInt > 10:
        print("8:" + str(finishMinute) + ":" + str(additionalSecsInt))

timeFunction()
