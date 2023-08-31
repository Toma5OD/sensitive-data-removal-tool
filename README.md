# Sensitive Data Redaction Tool

## Overview

This Python script allows you to redact or remove sensitive words or strings from text files as well as text entered directly in the terminal. It's a versatile utility designed to scrub confidential information from documents or live inputs.

## Features

- Supports `.txt` files and terminal-based text inputs
- Option to remove or redact words
- Case sensitivity option
- Interactive command line prompts
- Option to output to terminal or save to a new file
- Adds optional security notes to the content

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.
2. Open your terminal and navigate to the folder where the script is located.
3. Run the script using `python script.py`.
4. Follow the interactive prompts to redact or remove sensitive information.

### Example:

```
Welcome to the Redaction Tool! You can redact a file or input text directly.
Would you like to import data from a file? (y/n): y
Enter the path to the text file: /path/to/your/file.txt
Enter the word or string to be removed: secret
Should the removal be case-sensitive? (y/n): n
By default, the word will be redacted.
Would you like the word to be simply removed instead of being redacted? (y/n): y
Add security note to the top and bottom of the content? (y/n): y
Output to terminal? (y/n): y
Output to file? (y/n): n
---- Updated Content ----
[REDACTED] text here.
-------------------------
Operation successful.
```

## File Storage

The redacted content will be saved to a new file in the same directory where the script is run, unless specified otherwise.

## Limitations

- Does not support PDF, DOCX, or other complex text file types (yet).

## Future Plans

- Add support for more complex file types like PDFs and DOCX.
