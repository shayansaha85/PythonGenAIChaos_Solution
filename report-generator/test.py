import csv

import pandas as pd

def parse_flat_output_to_csv(flat_output_path, csv_output_path): 

    # Read the flat output file (assuming it's a text file with newline-separated records)
    with open(flat_output_path, 'r') as flat_file:
        flat_data = flat_file.read().strip().split('\n')

    # Split each line into fields (assuming fields are separated by a delimiter, e.g., tab or comma)
    parsed_data = [line.split('\t') for line in flat_data]  # Replace '\t' with your delimiter if needed

    # Convert the parsed data to a DataFrame
    df = pd.DataFrame(parsed_data)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_output_path, index=False, header=False)  # Set index and header to False if not needed

    return csv_output_path

# Example usage:


flat_output_path = 'raj_file.txt'  # Replace with your flat output file path

csv_output_path = 'output.csv'  # Replace with your desired CSV output file path

result_path = parse_flat_output_to_csv(flat_output_path, csv_output_path)

print(f'CSV file saved at: {result_path}')