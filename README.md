# Lab 1: Web Scraping & Data Filtering (CNBC)

name: Shufen Chen<br>
USCID: 9180940635<br>

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
```text
Lab1/
|--Shufen_Chen_9180940635/
|  |--data/
|  |  |--raw_data/
|  |  |  `--web_data.html
|  |  `--processed_data/
|  |  |  |--market_data.csv
|  |  |  `--news_data.csv
|  `--scripts/
|  |  |--task_1.py
|  |  |--web_scraper.py
|  |  `--data_filter.py
`--README.md
```

## Setup
Make sure Python3 and pip are installed.<br>
Install required packages:<br>
pip install bs4<br>
pip install selenium<br>

## How to Run
1. Locate in the target folder<br>
cd Lab1/Shufen_Chen_9180940635/scripts<br>

2. Run the user name testing file<br>
python3 task_1.py<br>

3. Run web scraper<br>
python3 web_scraper.py<br>

4. Run data filter<br>
python3 data_filter.py<br>


## Output Files
data/raw_data/web_data.html<br>
data/processed_data/market_data.csv<br>
data/processed_data/news_data.csv<br>
