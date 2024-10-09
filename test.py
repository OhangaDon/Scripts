import re

def extract_info(line):
    # Regular expressions to extract the name, SSN, DOB, and full address
    name_pattern = r'\|([A-Z\s]+)\|'
    ssn_pattern = r'\|(\d{9})\|'
    dob_pattern = r'\|(\d{4}-\d{2}-\d{2})\|'
    address_pattern = r'\|(\d{1,5} [\w\s]+ AVE \d{1}|\d{1,5} [\w\s]+)\|([A-Z\s]+ [A-Z]{2} \d{5}-\d{4})'

    # Finding all matches in the line
    name = re.search(name_pattern, line)
    ssn = re.search(ssn_pattern, line)
    dob = re.search(dob_pattern, line)
    address = re.search(address_pattern, line)

    # Extract and clean up the matched information
    return {
        'Name': name.group(1).strip() if name else None,
        'SSN': ssn.group(1) if ssn else None,
        'DOB': dob.group(1) if dob else None,
        'Address': f"{address.group(1)}|{address.group(2)}" if address else None,
    }

def process_file(input_file, output_file):
    # Read the input file line by line
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Open the output file to write the results
    with open(output_file, 'w') as file:
        for line in lines:
            # Extract information from each line
            info = extract_info(line)
            
            # Check if all fields are extracted
            if info['Name'] and info['SSN'] and info['DOB'] and info['Address']:
                file.write(f"Name: {info['Name']}\n")
                file.write(f"SSN: {info['SSN']}\n")
                file.write(f"DOB: {info['DOB']}\n")
                file.write(f"Address: {info['Address']}\n")
                file.write("----------------------------------\n\n")

# Example usage
input_file = 'fullz.txt'  # Replace with the path to your input text file
output_file = 'output2.txt'  # Replace with the desired output text file

process_file(input_file, output_file)
