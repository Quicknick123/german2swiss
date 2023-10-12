
import re
import pickle

def standardize_number_in_text(text: str) -> str:
    # Step 1: Remove spaces and dots within numbers
    sanitized_str = re.sub(r'(\d)[\s.](?=\d)', r'\1', text)
    
    # Step 2: Remove commas used as thousand separators within numbers
    sanitized_str = re.sub(r'(\d),(?=\d{3})', r'\1', sanitized_str)
    
    # Step 3: Replace comma used as decimal separator with a period
    standardized_str = re.sub(r'(\d),(?=\d)', r'\1.', sanitized_str)
    
    return standardized_str

def swiss_number_format(number: str) -> str:
    return re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\1\'', number)

def format_currency(text: str) -> str:
    currency_symbols = ["EUR", "USD", "€", "$", "CHF"]
    for symbol in currency_symbols:
        pattern_before = r'(\d+\.?\d*)( ?)' + re.escape(symbol)
        pattern_after = re.escape(symbol) + r'( ?)(\d+\.?\d*)'
        
        # For symbol after the number
        match_after = re.search(pattern_after, text)
        if match_after:
            number = match_after.group(2)
            if '.' not in number:
                number += '.-'
            text = re.sub(pattern_after, symbol + ' ' + number, text)
        
        # For symbol before the number
        match_before = re.search(pattern_before, text)
        if match_before:
            number = match_before.group(1)
            if '.' not in number:
                number += '.-'
            text = re.sub(pattern_before, symbol + ' ' + number, text)
    
    return text

def quotes(text):
    return re.sub(r'“(.+?)”', r'«\1»', text)
    
def time_format(text):
    return re.sub(r'(\b\d{2}):(\d{2}\b)', r'\1.\2', text)

def currency_format(text):
    text = standardize_number_in_text(text)
    text = format_currency(text)
    text = swiss_number_format(text)
    return text
    
def eszett(text):
    return re.sub(r'ß', 'ss', text) 

def words(text): 
    with open('swiss_vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
    
    translation_table = str.maketrans(vocab)
    text = text.translate(translation_table)
    
    return text

def adapt_text(text: str) -> str:
    text = quotes(text)
    text = time_format(text)
    text = currency_format(text)
    text = eszett(text)
    text = words(text)
    
    return text
