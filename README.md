# Defi Statistics

Python tools to scrape and aggregate defi statistics.  **Work in progress**

## Project Directory Structure

Programs are organized into the following directory structure:
- [api](./api) - Programs and tools which use a public API endpoint.
- [utilities](./utilities) - Adhoc utilities.
- [web_scrape](./web_scrape) - Programs and tools which use web scraping techniques.


## Prerequisites

Use of these tools require working knowledge of [Python](https://www.python.org/).  The following packages are required for python programs written within this repository.

Install Python dependencies
```bash
pip install beautifulsoup4 selenium bs4 lxml pandas
```

Install ChromeDriver
```bash
brew install chromedriver
```


## Getting Started

Execute the [defillama-protocols.py](./api/defillama-protocols.py) program to query the DefiLlama API for relevant statistics.

Work in progress...


## Reference

https://www.geeksforgeeks.org/how-to-install-selenium-on-macos/
https://stackoverflow.com/questions/38081021/using-selenium-on-mac-chrome

