#!/usr/bin/python3

import re
import argparse

# Function to check each line based on the given conditions
def check_line(line, min_length, max_length, min_specials, min_numbers, min_uc, min_lc):
    line_length = len(line)

    # Check the length of the line
    if line_length < min_length or line_length > max_length:
        return False

    # Count the number of digits, special characters, uppercase and lowercase characters
    num_digits = sum(char.isdigit() for char in line)
    num_specials = sum(re.search(r'[\W_]', char) is not None for char in line)
    num_uc = sum(char.isupper() for char in line)
    num_lc = sum(char.islower() for char in line)

    # Validate the line against the conditions
    if any([
        min_numbers > num_digits,
        min_specials > num_specials,
        min_uc > num_uc,
        min_lc > num_lc
    ]):
        return False

    return True

# Function to filter the wordlist file
def filter_wordlist(input_file, output_file, min_length, max_length, min_specials, min_numbers, min_uc, min_lc, verbose):
    input_lines = 0
    output_lines = 0

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            input_lines += 1
            line = line.strip()

            if check_line(line, min_length, max_length, min_specials, min_numbers, min_uc, min_lc):
                output_lines += 1
                outfile.write(f"{line}\n")
            elif verbose:
                print(f"Removed: {line}")

    print(f"Total lines in the original file: {input_lines}")
    print(f"Total lines in the output file: {output_lines}")

# Main function to handle command-line arguments and call other functions
def main():
    parser = argparse.ArgumentParser(description="Filter a wordlist based on various conditions.")
    parser.add_argument('-i', '--input', required=True, help="Input wordlist file")
    parser.add_argument('-o', '--output', required=False, help="Output wordlist file (optional)")
    parser.add_argument('-min', '--min_length', type=int, default=8, help="Minimum word length (default 8)")
    parser.add_argument('-max', '--max_length', type=int, default=20, help="Maximum word length (default 20)")
    parser.add_argument('-sn', '--min_specials', type=int, default=1, help="Minimum number of special characters required (default 1)")
    parser.add_argument('-nn', '--min_numbers', type=int, default=1, help="Minimum number of digits required (default 1)")
    parser.add_argument('-uc', '--min_uppercase', type=int, default=1, help="Minimum number of uppercase characters required (default 1)")
    parser.add_argument('-lc', '--min_lowercase', type=int, default=1, help="Minimum number of lowercase characters required (default 1)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose mode, shows each removed line (default False)")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else f"{input_file.split('.')[0]}_checked.txt"
    if output_file.startswith('_'):
        output_file = "checked-output.txt"

    filter_wordlist(input_file, output_file, args.min_length, args.max_length, args.min_specials, args.min_numbers, args.min_uppercase, args.min_lowercase, args.verbose)

if __name__ == "__main__":
    main()

