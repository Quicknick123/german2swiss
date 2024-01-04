
import re
import os
from typing import Set
import pickle

def standardize_number_in_text(text: str) -> str:
    """The standardize_number_in_text function takes a string as input and standardizes the number format within the text. It removes spaces and dots within numbers, removes commas used as thousand separators within numbers, and replaces commas used as decimal separators with periods.

    Args:
        text (str): The input text to be standardized.
    
    Returns:
        str: The standardized text."""
    # Step 1: Remove spaces and dots within numbers
    sanitized_str = re.sub(r'(\d)[\s.](?=\d)', r'\1', text)
    
    # Step 2: Remove commas used as thousand separators within numbers
    sanitized_str = re.sub(r'(\d),(?=\d{3})', r'\1', sanitized_str)
    
    # Step 3: Replace comma used as decimal separator with a period
    standardized_str = re.sub(r'(\d),(?=\d)', r'\1.', sanitized_str)
    
    return standardized_str

def swiss_number_format(number: str) -> str:
    """The swiss_number_format function is a Python function that takes a string representing a number as input and returns the same number formatted with a Swiss number format. The function should work for numbers with or without decimal places. The function should not change the number if it is less than 4 digits long.
    
    Args:
        text (str): The input text to be formatted.
        
    Returns:
        str: The formatted text with the Swiss number format."""
    # Remove any existing thousand separators
    number = number.replace("'", "")
    number = number.replace(",", "")

    # Add the Swiss thousand separator
    number = number[::-1]
    number = "'".join(number[i:i+3] for i in range(0, len(number), 3))
    number = number[::-1]

    return number

def format_currency(text: str, currency_symbols: Set[str] = {"EUR", "USD", "€", "$", "CHF"}) -> str:
    """The format_currency function is used to format currency values in a given text by adding the appropriate currency symbol and decimal point if necessary.
    Args:
        text (str): The input text to be formatted.
        currency_symbols (Set[str], optional): The set of currency symbols to be used. Defaults to {"EUR", "USD", "€", "$", "CHF"}.
    Returns:
        str: The formatted text with the appropriate currency symbol and decimal point if necessary.
    """
    for symbol in currency_symbols:
        pattern_before = r'(\d+\.?\d*)( ?)' + re.escape(symbol)
        pattern_after = re.escape(symbol) + r'( ?)(\d+\.?\d*)'
        
        # For symbol after the number
        match_after = re.search(pattern_after, text)
        if match_after:
            number = match_after.group(2)
            if '.' not in number:
                number += '.-'
            number_parts = number.split('.')
            number_parts[0] = swiss_number_format(number_parts[0])
            number = '.'.join(number_parts)
            text = re.sub(pattern_after, symbol + ' ' + number, text)
        
        # For symbol before the number
        match_before = re.search(pattern_before, text)
        if match_before:
            number = match_before.group(1)
            if '.' not in number:
                number += '.-'
            number_parts = number.split('.')
            number_parts[0] = swiss_number_format(number_parts[0])
            number = '.'.join(number_parts)
            text = re.sub(pattern_before, symbol + ' ' + number, text)
    
    return text

def replace_quotes(text: str) -> str:
    """The replace_quotes function is a Python function that takes a string as input and replaces all occurrences of double quotation marks (") with angled quotation marks («»).
    Args:
        text (str): The input text to be formatted.
    
    Returns:
        str: The formatted text with the double quotation marks replaced by angled quotation marks."""
    # Replace straight double quotes and German-style quotes
    text = re.sub(r'"(.*?)"', r'«\1»', text)
    text = re.sub(r'„(.*?)“', r'«\1»', text)
    
    # Replace single quotes if they appear in pairs (assuming they are used as quotation marks)
    text = re.sub(r"'(.*?)'", r'«\1»', text)
    return text
    
def format_time(text: str) -> str:
    """The time_format function uses regular expressions to replace occurrences of time in the format "HH:MM" with "HH.MM".
    Args:
        text (str): The input text to be formatted.

    Returns:
        str: The formatted text with the colon replaced by a dot.
    """
    return re.sub(r'(\b\d{2}):(\d{2}\b)', r'\1.\2', text)

def format_currency_handler(text: str) -> str:
    """The format_currency_handler function is a Python function that takes a string as input and formats the numbers within the text to a standardized currency format. It uses the standardize_number_in_text function to remove spaces, dots, and commas within numbers, and replaces commas used as decimal separators with periods. It then applies the swiss_number_format function to format the numbers with a Swiss number format.
    Args:
        text (str): The input text to be formatted.
        
    Returns:
        str: The formatted text with the standardized currency format."""
    text = standardize_number_in_text(text)
    text = format_currency(text)
    return text
    
def convert_esszett(text: str) -> str:
    """The convert_esszett function is a Python function that takes a string as input and replaces all occurrences of the German letter ß with the equivalent Swiss letter combination ss.

    Args:
        text (str): The input text to be formatted.
        
    Returns:
        str: The formatted text with the esszett subsituted with ss.
    """
    return re.sub(r'ß', 'ss', text) 

def convert_words(text: str) -> str: 
    """The convert_words function is a Python function that takes a string as input and replaces all occurrences of the German words "Straße" and "Strasse" with the equivalent Swiss word "Strasse".

    Args:
        text (str): The input text to be formatted.

    Returns:
        str: The formatted text with German words substituted with Swiss words.
    """
    # Get the current file's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the swiss_vocab.pickle file
    vocab_file = os.path.join(current_dir, 'swiss_vocab.pickle')

    # Load the vocabulary from the pickle file
    with open(vocab_file, 'rb') as f:
        vocab = pickle.load(f)
        
    for key, value in vocab.items():
        pattern = r'\t' + re.escape(key) + r'\t'
        text = re.sub(pattern, '\t' + value + '\t', text)

    return text

def replace_apostrophes(text: str) -> str:
    """The replace_apostrophes function is a Python function that takes a string as input and replaces all occurrences of the German apostrophe (’) with the equivalent Italian apostrophe (').

    Args:
        text (str): The input text to be formatted.

    Returns:
        str: The formatted text with the apostrophes substituted.
    """
    return re.sub(r'’', "'", text)

def adapt_text_handler(text: str, language: str = "swiss") -> str:
    """The adapt_text_handler function is a Python function that takes a string as input and applies the following functions to the text in the following order: replace_quotes, format_time, format_currency_handler, convert_esszett, and convert_words.

    Args:
        text (str): The input text to be formatted.

    Returns:
        str: The formatted text with the appropriate substitutions.
    """
    if language == "swiss":
        text = replace_quotes(text)
        text = format_currency_handler(text)
        text = convert_esszett(text)
        text = convert_words(text)
        text = format_time(text)
    if language == "italian":
        text = replace_apostrophes(text)
    
    return text

