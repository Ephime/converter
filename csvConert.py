import csv
import json

with open(r'C:\Users\eugen\OneDrive\Desktop\Untitled-1.json', 'r') as file:
    data = json.load(file)

with open('filename.csv', 'w', newline='') as csvfile:
    fieldnames = ['x','y', 'z']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow({
            'x': entry['x'],
            'y': entry['y'],
            'z': entry['z']
        })

print("CSV file created successfully.")
