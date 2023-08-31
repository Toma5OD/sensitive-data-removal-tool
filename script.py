import re

def remove_or_redact_info(content, words_to_remove, method, case_sensitive):
    total_redactions = 0
    for word_to_remove in words_to_remove:
        pattern = re.compile(re.escape(word_to_remove), re.IGNORECASE if not case_sensitive else 0)
        
        if not pattern.search(content):
            print(f"Word '{word_to_remove}' not found.")
            continue
        
        count = len(pattern.findall(content))
        total_redactions += count
        
        if method == 'redact':
            content = pattern.sub('[REDACTED]', content)
        else:
            content = pattern.sub('', content)
            
    return content, total_redactions

def add_security_notes(content):
    note = "\n--- Sensitive information has been removed from this file for security reasons ---\n"
    return note + content + note

def main():
    print("Welcome to the Redaction Tool! You can redact a file or input text directly.")
    
    from_file = input("Would you like to import data from a file? (y/n): ").lower() == 'y'
    
    if from_file:
        file_path = input("Enter the path to the text file: ")
        with open(file_path, 'r') as f:
            content = f.read()
    else:
        content = input("Enter the text directly: ")

    num_words = int(input("How many different words would you like to redact?: "))
    words_to_remove = [input(f"Enter word {i+1} to be redacted: ") for i in range(num_words)]
    
    case_sensitive = input("Should the removal be case-sensitive? (y/n): ").lower() == 'y'

    print("By default, the words will be redacted.")
    method = 'redact' if input("Would you like the words to be simply removed instead of being redacted? (y/n): ").lower() != 'y' else 'remove'
    
    updated_content, total_redactions = remove_or_redact_info(content, words_to_remove, method, case_sensitive)
    
    if total_redactions == 0:
        print("No words found. Operation unsuccessful.")
        return
    
    print(f"Total redactions made: {total_redactions}")

    add_notes = input("Add security note to the top and bottom of the content? (y/n): ").lower() == 'y'

    if add_notes:
        updated_content = add_security_notes(updated_content)

    output_terminal = input("Output to terminal? (y/n): ").lower() == 'y'
    output_file = input("Output to file? (y/n): ").lower() == 'y'

    if output_terminal:
        print("---- Updated Content ----")
        print(updated_content)
        print("-------------------------")

    if output_file:
        output_file_name = input("Enter the output file name: ")
        with open(output_file_name, 'w') as f:
            f.write(updated_content)
        print(f"Content saved to {output_file_name}")

    print("Operation successful.")

if __name__ == '__main__':
    main()
