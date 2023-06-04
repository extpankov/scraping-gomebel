# Products scraper for [gomebel.com](https://gomebel.com)

<p align="center">
   <img src="https://img.shields.io/badge/python-3.10.8-green" alt="Python Version">
   <img src="https://img.shields.io/badge/version-v1-lightgrey" alt="Project Version">
   <img src="https://img.shields.io/badge/language-ru-blue" alt="Language">
  <br>
   <img src="https://img.shields.io/badge/beautifulsoup4-v4.12.2-green">
  <img src="https://img.shields.io/badge/lxml-v4.9.2-green">
   <img src="https://img.shields.io/badge/selenium-v4.9.1-green">
</p>

## About
The task was set to get links to all products from the presented site.

The script goes through the page with categories, collects their links, and then goes through each category and collects links with products, saving them in links.txt

The complete collection of links in a text document was 235 seconds for Macbook Air 2018 (i5, 8 GB), 20.515 links were collected.

It can be finalized in the form of parsing product cards into a csv file.
## One more thing
Messages output to the terminal slow down the execution of the program. If you need to disable them, please switch the flag in line 6 main.py


## Developers

- [Roman Pankov](https://github.com/extpankov)
