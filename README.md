# Python scrapy

Exploring the popular [Scrapy](https://scrapy.org/) library.

## Development machine setup

This development environment was created by:

* Cloning this repository using PyCharm (so as to create a new PyCharm project automatically)
* Setting the project interpreter to:
    * a Virtualenv Environment with 
    * a base interpreter of Python 3.6
* Adding the Scrapy package using PyCharm
* Running `. venv/bin/activate` from the project root to activate the environment

## Example

An example Spider called quotes can be found in `tutorial/tutorial/spiders/quotes_spider.py`. This is a simple spider which scrapes the content from two URLs and saves the content of each ot its own .html file. It can by running `scrapy crawl quotes` from `tutorial/tutorial/`