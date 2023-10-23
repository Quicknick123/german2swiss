    
from ..german2swiss import *
def test_input_string_contains_only_digits(self):
    input_str = "1234567890"
    expected_output = "1234567890"
    assert standardize_number_in_text(input_str) == expected_output

    # Standardizes a string containing only letters
def test_input_string_contains_only_letters(self):
    input_str = "abcdefghij"
    expected_output = "abcdefghij"
    assert standardize_number_in_text(input_str) == expected_output

    # Standardizes a string containing whitespace characters
def test_input_string_contains_whitespace(self):
    input_str = "12 345 67890"
    expected_output = "1234567890"
    assert standardize_number_in_text(input_str) == expected_output


def test_less_than_4_digits(self):
        input_number = "123"
        expected_output = "123"
        assert swiss_number_format(input_number) == expected_output
    
def test_only_digits_no_separators(self):
        input_number = "1234567890"
        expected_output = "1234567890"
        assert swiss_number_format(input_number) == expected_output
        
def test_only_one_separator(self):
    input_number = "1'234"
    expected_output = "1'234"
    assert swiss_number_format(input_number) == expected_output
    
def test_replace_time_format(self):
        # Arrange
        input_text = "The meeting is scheduled at 10:30"
        expected_result = "The meeting is scheduled at 10.30"
    
        # Act
        result = time_format(input_text)
    
        # Assert
        assert result == expected_result

def test_replace_multiple_time_formats(self):
        # Arrange
        input_text = "The train departs at 09:45 and arrives at 14:30"
        expected_result = "The train departs at 09.45 and arrives at 14.30"
    
        # Act
        result = time_format(input_text)
    
        # Assert
        assert result == expected_result
        
def test_invalid_hour_minute(self):
        # Arrange
        input_text = "The time is 25:30"
    
        # Act
        result = time_format(input_text)
    
        # Assert
        assert result == input_text
        
def test_currency_symbol_before_number(self):
        text = "USD 10"
        expected_result = "USD 10.-"
        assert format_currency(text) == expected_result
        
def test_currency_symbol_after_number(self):
        text = "10 USD"
        expected_result = "USD 10.-"
        assert format_currency(text) == expected_result
        
def test_scientific_notation_and_currency_symbols(self):
        text = "1.23e5 USD"
        expected_result = "$ 123000.-"
        assert format_currency(text) == expected_result