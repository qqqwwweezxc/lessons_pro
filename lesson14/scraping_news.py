import requests
import pandas as pd
import csv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


URL = "https://www.unian.ua/"


def get_page(url: str) -> BeautifulSoup | None:
    """Download page HTML and return BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    
    except requests.RequestException as error:
        print(f"Error. Failed to fetch page: {error}")
        return None


def parse_news(soup: BeautifulSoup) -> list[dict]:
    """Extract news from homepage."""
    news_list = []

    try:
        items = soup.find_all("div", class_ = "list-news__item")

        for item in items:
            title = item.find("a", class_ = "list-news__title").text
            link = item.find("a", class_ = "list-news__title").get("href")
            date = item.find("span", class_ = ["list-news__time", "time"]).text

            news_list.append(
                {
                    "title": title,
                    "link": link,
                    "date": date
                }
            )

        return news_list
    
    except Exception as error:
        print(f"Error. Failed to parse news: {error}")


def parse_date(date_str: str) -> datetime | None:
    """Convert string to datetime."""
    try:
        return datetime.strptime(date_str.strip(), "%H:%M, %d.%m.%Y")
    
    except Exception as e:
        print(f"Error. Failed to parse date: {date_str} | {e}")
        return None

    
def filter_recent_news(news: list[dict], days: int = 7) -> list[dict]:
    """Filter news for the last N days."""
    now = datetime.now()
    threshold = now - timedelta(days=days)

    filtered = []

    for item in news:
        parsed_date = parse_date(item["date"])

        if parsed_date and parsed_date >= threshold:
            item["parsed_date"] = parsed_date
            filtered.append(item)

    return filtered


def save_to_csv(data: list[dict], filename: str) -> None:
    """Save news to CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "link", "date", "parsed_date"]
            )
            writer.writeheader()
            writer.writerows(data)

    except IOError as error:
        print(f"Error. Failed to write CSV file: {error}")


def generate_stats(news: list[dict]) -> None:
    """Generate simple statistics: number of news per day."""
    
    if not news:
        print("No data for statistics.")
        return

    df = pd.DataFrame(news)

    if "parsed_date" not in df.columns:
        df["parsed_date"] = pd.to_datetime(df["date"], format="%H:%M, %d.%m.%Y")

    df["date_only"] = df["parsed_date"].dt.date

    stats = df.groupby("date_only").size()

    print("\nNews count by date:")
    print(stats)


    print("\nSorted:")
    print(stats.sort_index())


if __name__ == "__main__":
    page = get_page(URL)

    if page is None:
        print("Program stopped: page not loaded.")
    else:
        news = parse_news(page)

        if news:
            filtered_news = filter_recent_news(news, days=7)
            save_to_csv(filtered_news, "./lesson14/news.csv")
            print("Successfully parsed and saved news to news.csv")

            generate_stats(filtered_news)
        else:
            print("No news found.")




