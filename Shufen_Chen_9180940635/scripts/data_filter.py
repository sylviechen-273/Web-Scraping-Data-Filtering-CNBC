from bs4 import BeautifulSoup
import csv

# get the html file from the local folder
with open("../data/raw_data/web_data.html", "r", encoding = "utf-8") as f:
    html = f.read()

# parse the html
print("Parsing the html...")
soup = BeautifulSoup(html, 'html.parser')

print("Filtering fields...")
# find the container for market banner
container = soup.find("div", id = "market-data-scroll-container")
cards = container.find_all("a", class_ = "MarketCard-container")

# find the container for latest news list
side_container = soup.find("ul", class_ = "LatestNews-list")
news = side_container.find_all("li", class_ = "LatestNews-item")

# extract and store the specific elements from the market banner
market_list = []
for card in cards:
    marketCard_symbol = card.find("span", class_ = "MarketCard-symbol").get_text()
    marketCard_stockPosition = card.find("span", class_ = "MarketCard-stockPosition").get_text()
    marketCard_changePct = card.find("span",class_ = "MarketCard-changesPct").get_text()
    market_list.append([marketCard_symbol, marketCard_stockPosition, marketCard_changePct])

# ectract and store the elements from the news list
news_list = []
for new in news:
    latestNews_timestamp = new.find("time", class_ = "LatestNews-timestamp").get_text()
    title = new.find("a", class_ = "LatestNews-headline").get_text()
    link = new.find("a", class_ = "LatestNews-headline")["href"]
    news_list.append([latestNews_timestamp, title, link])

print("Extraction completed!")

# save the list into csv files
with open ('../data/processed_data/market_data.csv', 'w',  encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["marketCard_symbol", "marketCard_stockPosition", "marketCard_changePct"])
    writer.writerows(market_list)
print("Successfully saved the market banner information as market_data.csv")

with open ('../data/processed_data/news_data.csv', 'w', encoding = 'utf-8') as f1:
    writer = csv.writer(f1)
    writer.writerow(["LatestNews-timestamp", "title", "link"])
    writer.writerows(news_list)

print("Successfully saved the latest news information as news_data.csv")
print("Data filtering completed!")
