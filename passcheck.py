#!/usr/bin/python3

import re
import argparse

# Function to check each line based on the given conditions
def check_line(line, min_length, min_specials, min_numbers):
    # Check if the line is shorter than the minimum length
    if len(line) < min_length:
        return False

    # Count the number of digits in the line
    num_digits = sum(char.isdigit() for char in line)

    # Count the number of special characters in the line (including '_')
    num_specials = sum(re.search(r'[\W_]', char) is not None for char in line)

    # Check if the line meets the minimum number of digits and special characters
    if min_numbers > num_digits or min_specials > num_specials:
        return False

    return True

# Function to filter the wordlist file
def filter_wordlist(input_file, output_file, min_length, min_specials, min_numbers, verbose):
    input_lines = 0  # Counter for lines in the input file
    output_lines = 0  # Counter for lines in the output file

    # Open both the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            input_lines += 1  # Increment input line counter
            line = line.strip()  # Remove leading/trailing whitespaces

            # Check if the line meets all the conditions
            if check_line(line, min_length, min_specials, min_numbers):
                output_lines += 1  # Increment output line counter
                outfile.write(f"{line}\n")  # Write the line to the output file
            elif verbose:  # If in verbose mode, print removed lines
                print(f"Removed: {line}")

    # Print the total number of lines in both files
    print(f"Total lines in the original file: {input_lines}")
    print(f"Total lines in the output file: {output_lines}")

# Main function to handle command-line arguments and call other functions
def main():
    # Initialize argument parser and define arguments
    parser = argparse.ArgumentParser(description="Filter a wordlist based on various conditions.")
    parser.add_argument('-i', '--input', required=True, help="Input wordlist file")
    parser.add_argument('-o', '--output', required=False, help="Output wordlist file (optional)")
    parser.add_argument('-l', '--length', type=int, default=8, help="Minimum word length (default 8)")
    parser.add_argument('-sn', '--min_specials', type=int, default=1, help="Minimum number of special characters required (default 1)")
    parser.add_argument('-nn', '--min_numbers', type=int, default=1, help="Minimum number of digits required (default 1)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose mode, shows each removed line (default False)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Determine the output file name
    input_file = args.input
    output_file = args.output if args.output else f"{input_file.split('.')[0]}_checked.txt"
    if output_file.startswith('_'):
        output_file = "checked-output.txt"

    # Call the function to filter the wordlist
    filter_wordlist(input_file, output_file, args.length, args.min_specials, args.min_numbers, args.verbose)

# Entry point of the script
if __name__ == "__main__":
    main()

