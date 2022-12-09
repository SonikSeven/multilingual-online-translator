from bs4 import BeautifulSoup

import sys
import requests


def translate(translate_from, translate_to, word):
    url = f"https://context.reverso.net/translation/{translate_from.lower()}-{translate_to.lower()}/{word.lower()}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 404:
        print(f"Sorry, unable to find {word}")
        quit()
    if response.status_code != 200:
        print("Something wrong with your internet connection")
        quit()
    main_soup = BeautifulSoup(response.content, 'html.parser')
    sentences_soup = main_soup.find("section", {"id": "examples-content"})
    words = [i.text for i in main_soup.find_all("span", {"class": "display-term"})]
    sentences = [i.text.strip() for i in sentences_soup.find_all("span", {"class": "text"})]
    with open(word + ".txt", "a", encoding="utf-8") as word_file:
        print(f"{translate_to} Translations:", words[0], f"\n{translate_to} Examples:", sep="\n", file=word_file)
        print(sentences[0], sentences[1], "\n", sep="\n", file=word_file)


def main():
    languages = ("Arabic", "German", "English", "Spanish", "French",
                 "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese",
                 "Romanian", "Russian", "Turkish")
    translate_from, translate_to, word = sys.argv[1:4]
    if translate_from.capitalize() not in languages:
        return print(f"Sorry, the program doesn't support {translate_from}")
    if translate_to.capitalize() not in languages and translate_to != "all":
        return print(f"Sorry, the program doesn't support {translate_to}")
    if translate_to == "all":
        for translate_to in languages:
            if translate_to.lower() != translate_from:
                translate(translate_from, translate_to, word)
    else:
        translate(translate_from, translate_to, word)
    with open(word + ".txt", encoding="utf-8") as word_file:
        print(word_file.read())


if __name__ == "__main__":
    main()
