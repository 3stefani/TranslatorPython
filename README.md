##Language Translator with Google Translator

This is a simple language translator created in Python using the googletrans library. The program allows you to translate text from one language to another specified by the user.

### Features
- Translation of words or phrases between different languages.

- Prompts for source and target languages.

- Simple and user-friendly console interface.

### Requirements

Before running this program, make sure you have the following installed:

- Python 3.x

- The googletrans library

You can install googletrans with the following command:

	pip install googletrans==4.0.0-rc1

## How to Use

1. Clone this repository or copy the source code.

2. Ensure you have the required dependencies installed.

3. Run the script with the following command:

	python translator.py

4. Follow the instructions in the console:

	Enter the text you want to translate.

	Enter the source language (e.g., en for English, es for Spanish).

	Enter the target language.
	

### Example

Suppose you want to translate "Hello, world!" from English to Spanish. The program will prompt you for the following:

	Enter the word or phrase to translate: Hello, world!
	Enter the source language: en
	Enter the target language: es

**The result will be something like:**
	Ingrese la palabra o frase a traducir: casa
	Ingrese el idioma de origen:es
	Ingrese el idioma de destino:en
	Texto Original (es): casa
	texto_a_traducido (en): home

### Important Notes

Make sure to use the correct language codes. You can check the full list of codes in the Google Translator documentation.

If you encounter issues with the googletrans library, ensure you are using the recommended version (4.0.0-rc1).
