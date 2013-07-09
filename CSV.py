# Program to re-order and remove columns from CSV data.
# Author: Ian D. Davies
# Date: June 24th, 2013
# ---------------------------------------------------------------------
# Last Updated: July 5, 2013
# Reason: Change some variable names to make them more generic.

import clipboard
import console
import csv

text = clipboard.get()
csvLines = text.splitlines()
row = len(csvLines)

cvs_data = csv.reader(csvLines)
headers = next(cvs_data)
for row in cvs_data:
	csv_line = row[2].strip(' ') + ', ' + row[5].strip(' ') + ', ' + row[4].strip(' ')
	print csv_line
  
print 'done.'
