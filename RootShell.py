# SETTINGS
advanced=False
displayTime=True
# CODE

from datetime import date
today = date.today()
from cmd import Cmd
print('Imported CMD')
import os
print('Imported OS')
import sys
print('Imported System')

if displayTime==True:
	print(f'RootShell v1.0.0 ({today.strftime("%B %d, %Y")} at {today.strftime("%H:%M:%S)}")}')
if displayTime==False:
	print('RootShell v1.0.0')

while 1:
	if advanced==True:
		x = input(f'{os.getcwd()} > ')
	else:
		x = input('RootShell > ')

	try:
		y = eval(x)
		if y: print(y)
	except:
		try:
			exec(x)
		except Exception as e:
			print("error:", e)
