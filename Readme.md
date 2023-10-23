# Text Formatting Library

This Python library offers a collection of functions designed to format and adapt textual content to conform to specific standards, notably Swiss formatting conventions. It is particularly tailored to handle currency formatting, time formatting, and linguistic adjustments between German and Swiss terminologies.

## Features

1. **Number Standardization**: Normalize numbers within a text, removing unnecessary spaces, dots, and commas.
2. **Swiss Number Formatting**: Convert number formats to adhere to Swiss conventions.
3. **Currency Formatting**: Adjust currency formats by adding appropriate symbols and decimal points.
4. **Quotation Mark Replacement**: Replace standard double quotation marks with angled quotation marks.
5. **Time Formatting**: Modify time representations by replacing colons with dots.
6. **Esszett Conversion**: Transform the German letter "ß" into the Swiss equivalent "ss".
7. **German-to-Swiss Word Conversion**: Substitutes specific German words with their Swiss counterparts.

## Functions

### `standardize_number_in_text(text: str) -> str`
Sanitizes the number format within a text string.

### `swiss_number_format(text: str) -> str`
Formats a number string to comply with Swiss number format conventions.

### `format_currency(text: str, currency_symbols: Set[str] = {"EUR", "USD", "€", "$", "CHF"}) -> str`
Formats currency values in a text with the appropriate currency symbol and decimal point.

### `replace_quotes(text: str) -> str`
Replaces double quotation marks with angled quotation marks.

### `format_time(text: str) -> str`
Changes time format from "HH:MM" to "HH.MM".

### `format_currency_handler(text: str) -> str`
Applies standardization, currency formatting, and Swiss number formatting to a text.

### `convert_esszett(text: str) -> str`
Replaces the German letter "ß" with "ss".

### `convert_words(text: str) -> str`
Translates certain German words to their Swiss equivalents based on a predefined vocabulary.

### `adapt_text_handler(text: str) -> str`
A comprehensive function that applies multiple formatting and conversion functions to a given text.

## How to Use

gh repo clone Quicknick123/german2swiss
cd german2swiss
poetry install

If you are using pip: 
gh repo clone Quicknick123/german2swiss
cd german2swiss
poetry export -f requirements.txt --output requirements.txt
cd ..
pip install -r german2swiss/requirements.txt

Now you can import the library into your Python script:

```python
from german2swiss import *
```

## Dependencies

- The `re` module for regular expressions.
- The `pickle` module for serializing and deserializing Python object structures.

## Future Improvements

- Extend vocabulary for German-to-Swiss word translations.
- Introduce more number formatting conventions.
