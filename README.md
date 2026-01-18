# Lab 1: Web Scraping & Data Filtering (CNBC)

name: Shufen Chen
USCID: 9180940635

This project scrapes the CNBC webside into a HTML file and extracts the spefic elements from the Market Banner as well as the Latest News list.
---

## Project Objectives

1. Scrape the HTML 
    - Fetch the CNBC webpage (https://www.cnbc.com/world/?region=world) and save it as 'web_data.html'

2. Data filtering from the HTML
    - Market Banner
      - marketCard_symbol
      - marketCard_stockPosition
      - marketCard_changePct

    - LatestNews Lise
      - LatestNews-timestamp
      - title
      - link

## Folder Structure
Lab1/<br>
|--Shufen_Chen_9180940635/<br>
|  |--data/<br>
|  |  |--raw_data/<br>
|  |  |  |--web_data.html<br>
|  |  |--processed_data/<br>
|  |  |  |--market_data.csv<br>
|  |  |  |--news_data.csv<br>
|  |--scripts/<br>
|  |  |--task_1.py<br>
|  |  |--web_scraper.py<br>
|  |  |--data_filter.py<br>
|--README.md<br>


## Setup
Make sure Python3 and pip are installed.
Install required packages:
pip install bs4
pip install selenium

## How to Run
1. Locate in the target folder
cd Lab1/Shufen_Chen_9180940635/scripts

2. Run the user name testing file
python3 task_1.py

3. Run web scraper
python3 web_scraper.py

4. Run data filter
python3 data_filter.py


## Output Files
data/raw_data/web_data.html<br>
data/processed_data/market_data.csv<br>
data/processed_data/news_data.csv<br>
