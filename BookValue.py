# 2023-11-30
# Calculate Shakepay crypto book value from the 
# transaction summary CSV file.
import csv
import clipboard

with open('Data/transactions_summary.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    book_value = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
   
        if row["Transaction Type"] == "purchase/sale":
            line_count += 1
            book_value += int(row["Amount Debited"])
    print(f'\nProcessed {line_count} lines.')
    print(f'Book value ${book_value}.')
    clipboard.set(str(book_value))