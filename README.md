# Overview
This utility is designed to remove unnecessary passwords from wordlists. During password attacks, understanding the password policy of the target system is crucial. This tool can filter out passwords from a wordlist that do not conform to the target's password policy, making the attack more efficient.

# Features
* Filters out passwords based on minimum length.
* Removes passwords that lack the required number of digits.
* Eliminates passwords without the specified number of special characters.
* Optional verbose mode to display each line removed from the file.
* Command-line flags for customization.
* Generates summary statistics after processing.

# Requirements
* Python 3.x

# Installation
* Clone the repository to your local machine:
* Navigate into the project directory:
```bash
git clone <repository-url>
cd path/to/project
```
# Usage
Run the script from the command line as follows:
```bash
python script_name.py -i input_wordlist.txt [-o output_wordlist.txt] [-l 8] [-sn 1] [-nn 1] [-v]
Options:
-i, --input: Input wordlist file (Required).
-o, --output: Output wordlist file (Optional).
-l, --length: Minimum word length (Default is 8).
-sn, --min_specials: Minimum number of special characters required (Default is 1).
-nn, --min_numbers: Minimum number of digits required (Default is 1).
-v, --verbose: Verbose mode, shows each removed line (Default is False).
```
To see all options and their explanations, run:
```bash
python script_name.py -h
```
# Contribution
Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss what you would like to change.

# License
This project is open-source and available under the MIT License.
