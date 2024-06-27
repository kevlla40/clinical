import os
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def read_file_with_fallback(file_path, fallback_encoding='utf-8'):
    try:
        encoding = detect_encoding(file_path)
        with open(file_path, 'r', encoding=encoding) as file:
            return file.readlines(), encoding
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding=fallback_encoding) as file:
            return file.readlines(), fallback_encoding

def write_file_with_encoding(file_path, lines, encoding='utf-8'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.writelines(lines)

def remove_unwanted_line_from_file(file_path, unwanted_pattern):
    lines, encoding = read_file_with_fallback(file_path)
    cleaned_lines = [line for line in lines if not re.search(unwanted_pattern, line)]
    write_file_with_encoding(file_path, cleaned_lines, encoding)

def remove_unwanted_line_from_directory(directory_path, unwanted_pattern):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                remove_unwanted_line_from_file(file_path, unwanted_pattern)

# Example usage
directory_path = r'C:\Users\king\clinicalmanagement'  # Use raw string to avoid escape sequences
unwanted_pattern = r"sumit, \d+ years ago"  # Example pattern

remove_unwanted_line_from_directory(directory_path, unwanted_pattern)
