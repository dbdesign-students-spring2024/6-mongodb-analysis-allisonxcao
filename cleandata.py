import csv

input_file_path = 'data/listings.csv'
output_file_path = 'data/clean_listings.csv'

with open(input_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = [row for row in reader] 

redundant = set()
empty = set()
for index, header in enumerate(headers):
    column_data = {row[index] for row in data}
    if len(column_data) == 1:
        redundant.add(header)
    elif all(not cell.strip() for cell in column_data):
        empty.add(header)

columns_to_remove = redundant | empty | {'description', 'host about'}

remove_indexes = [headers.index(col) for col in columns_to_remove if col in headers]
cleaned_headers = [header for index, header in enumerate(headers) if index not in remove_indexes]
cleaned_data = [
    [cell for index, cell in enumerate(row) if index not in remove_indexes]
    for row in data
]

with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(cleaned_headers)
    writer.writerows(cleaned_data)

