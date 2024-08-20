# Wordlist Filter Script

This Python script is designed to filter a wordlist based on various conditions such as word length, number of special characters, digits, uppercase, and lowercase letters. The script processes a wordlist file and outputs a new wordlist file that meets the specified criteria. This is particularly useful for creating targeted wordlists for dictionary-based password attacks, where specific character combinations are required.

## Features

- **Length Filtering**: Set minimum and maximum word lengths to control the size of the words in the wordlist.
- **Character Requirements**: Specify the minimum number of special characters, digits, uppercase, and lowercase letters required in each word, ensuring that the generated wordlist matches specific password policy requirements.
- **Error Handling**: Handles Unicode decoding errors by skipping problematic lines, ensuring smooth processing of large wordlists.
- **Verbose Mode**: Optionally prints details of removed lines, helping you understand why certain words were excluded.

## Requirements

- Python 3.x

## Installation

To use the script, clone the repository or download the script file directly. Ensure you have Python 3.x installed on your system.

```bash
git clone <repository-url>
cd <repository-directory>
```

## Usage

Run the script from the command line using the following syntax:

```bash
python3 script_name.py -i <input_file> [options]
```

### Required Arguments

- `-i`, `--input`: The input wordlist file (required).

### Optional Arguments

- `-o`, `--output`: The output wordlist file (default: `<input_file>_checked.txt`).
- `-min`, `--min_length`: Minimum word length (default: 8).
- `-max`, `--max_length`: Maximum word length (default: 20).
- `-sn`, `--min_specials`: Minimum number of special characters required (default: 1).
- `-nn`, `--min_numbers`: Minimum number of digits required (default: 1).
- `-uc`, `--min_uppercase`: Minimum number of uppercase characters required (default: 1).
- `-lc`, `--min_lowercase`: Minimum number of lowercase characters required (default: 1).
- `-v`, `--verbose`: Enable verbose mode to show each removed line (default: False).

### Example Usage

#### Basic Filtering

```bash
python3 script_name.py -i wordlist.txt -o filtered_wordlist.txt -min 10 -max 15 -sn 2 -nn 2 -uc 2 -lc 2
```

This command will filter the `wordlist.txt` file, keeping only words between 10 and 15 characters long that contain at least 2 special characters, 2 digits, 2 uppercase letters, and 2 lowercase letters. The filtered list will be saved in `filtered_wordlist.txt`.

#### Verbose Mode

```bash
python3 script_name.py -i wordlist.txt -v
```

This command filters the `wordlist.txt` file with the default settings and prints each removed line to the console for review.

#### Custom Output File

```bash
python3 script_name.py -i wordlist.txt -o custom_output.txt
```

This command filters the `wordlist.txt` file with the default settings and saves the filtered list in `custom_output.txt`.

### Generating Specific Wordlists for Dictionary Attacks

This script is particularly useful for generating highly specific wordlists that can be used in dictionary password attacks, where the password policy of the target system is known. For example:

#### Example 1: Generating a Wordlist for Passwords with a Length of 12-16 Characters, Containing at Least 1 Special Character, 2 Digits, and 3 Uppercase Letters

```bash
python3 script_name.py -i raw_wordlist.txt -o attack_wordlist.txt -min 12 -max 16 -sn 1 -nn 2 -uc 3
```

This command generates a wordlist containing passwords that are 12-16 characters long, with at least 1 special character, 2 digits, and 3 uppercase letters. This can be particularly useful when the target system requires such a password format.

#### Example 2: Generating a Wordlist for Complex Passwords with 8-10 Characters, Containing 2 Special Characters, 3 Digits, and Both Uppercase and Lowercase Letters

```bash
python3 script_name.py -i raw_wordlist.txt -o complex_passwords.txt -min 8 -max 10 -sn 2 -nn 3 -uc 1 -lc 1
```

This command filters the `raw_wordlist.txt` file, keeping only passwords that are 8-10 characters long, with at least 2 special characters, 3 digits, and both uppercase and lowercase letters. This wordlist would be ideal for attacking systems with complex password policies.

#### Example 3: Generating a Wordlist for Simple Passwords with a Length of 6-8 Characters and No Special Characters

```bash
python3 script_name.py -i simple_wordlist.txt -o simple_passwords.txt -min 6 -max 8 -sn 0
```

This command filters the `simple_wordlist.txt` file, removing any passwords with special characters and keeping only those that are 6-8 characters long. This can be used for systems with simpler password requirements.

### Output

- The filtered wordlist will be saved to the specified output file.
- Summary statistics, including the total number of input lines, output lines, and any lines skipped due to decoding errors, will be printed to the console.

### Verbose Mode

Verbose mode can be helpful for debugging or understanding why certain words were excluded from the output file. To enable verbose mode, simply include the `-v` flag:

```bash
python3 script_name.py -i wordlist.txt -v
```

### Best Practices for Dictionary Attacks

- **Tailor the wordlist**: Adjust the script parameters to match the password policy of the target system.
- **Keep it concise**: Avoid generating unnecessarily large wordlists by setting appropriate length limits.
- **Combine wordlists**: Merge multiple filtered wordlists for a more comprehensive attack.

## Notes

- If no output file is specified, the output file will be named `<input_file>_checked.txt`.
- The input file should be in a text format and can contain UTF-8 encoded characters.
- Handle large wordlists with caution, as filtering may take considerable time.

## License

This script is free to use and distribute under the MIT License.
