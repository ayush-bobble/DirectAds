import csv
import chardet
import subprocess
import sys

filename = "search_queries_with_categories.csv"

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

try:
    # Detect the file encoding
    file_encoding = detect_encoding(filename)

    with open(filename, 'r', encoding=file_encoding) as rf:
        reader = csv.reader(rf, delimiter=',')
        
        header = next(reader, None)
        print(header)
        
        # Read and print all values of the second column
        all_values = [row[0] for row in reader if len(row[0]) > 0]
        print(all_values)

        second_column_values = []

        for value in all_values:
            second_column_values.extend(list(value.split(',')))

        second_column_values = [value.strip() for value in second_column_values]
 
        if second_column_values:
            print("Values of the second column:")
            print(second_column_values)
        else:
            print("The CSV file does not have values in the second column.")

except UnicodeDecodeError:
    print("Error decoding the file. Try specifying a different encoding or manually inspect the file.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except IndexError:
    print("Index out of range. Make sure the second column exists in each row.")

device = "RZ8M214NNBA"

# Prepare environment variables for maestro command
for i, word in enumerate(second_column_values):
    env_vars = ['-e', f'WORD={word}']
    if i == 0:
        # run the original script for the first env variable
        subprocess.run(["maestro", "--device="+device,"test"] + env_vars + ["browser_start.yaml"])
        print("Suggestion testing successful for the first env variable")
    else:
        # run a different script for the remaining env variables
        subprocess.run(["maestro", "--device="+device,"test"] + env_vars + ["browser_type.yaml"])
        print(f"Suggestion testing successful for env variable {i+1}")