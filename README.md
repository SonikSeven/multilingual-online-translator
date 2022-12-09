# Multilingual Online Translator

Multilingual Online Translator is a Python project leveraging the power of BeautifulSoup and Reverso Context to provide concise translations and examples for given words or phrases between supported languages.

## Features

- Translates words or phrases between a variety of languages.
- Extracts and provides example sentences using the translated word or phrase.
- Outputs the translations and examples to a text file for easy access and reference.
- Supports multiple languages including Arabic, German, English, Spanish, French, Hebrew, Japanese, Dutch, Polish, Portuguese, Romanian, Russian, and Turkish.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/multilingual-online-translator.git
```

2. Navigate to the cloned repository:

```
cd multilingual-online-translator
```

3. Create and activate a virtual environment:

```
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies using pip and the requirements.txt file:

```
pip install -r requirements.txt
```

## Usage

Multilingual Online Translator is executed from the command line. Here's how to use it:

1. Open your terminal or command prompt.

2. Navigate to the project directory.

3. Run the script using the following syntax:

```
python main.py <translate_from> <translate_to> <word>
```

- `<translate_from>`: The source language you are translating from (e.g., English).
- `<translate_to>`: The target language you wish to translate to. Use 'all' to translate to all supported languages.
- `<word>`: The word or phrase you wish to translate.

Example command:

```
python main.py English Spanish hello
```

This will translate the word "hello" from English to Spanish and save the translations along with example sentences to a text file named "hello.txt".

## License

This project is licensed under the [MIT License](LICENSE.txt).

## Acknowledgments

- This project uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Reverso Context](https://context.reverso.net/translation/) for scraping translations and examples.
