# собирать данные про книжки , с первой странички , ддя каждой книжки собрать название книжки, цену, 
# рейтинг, и availability на складе, сохранить все в csv , один рядок - одна книжка 
import requests
from bs4 import BeautifulSoup
import csv


URL = "https://books.toscrape.com/"


def scrape_books(url: str) -> list[dict]:
    """Scrape books data from the given URL."""
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_ = "product_pod")

    results = []

    for book in books:
        title = book.h3.a.get("title", "No title")
        
        price = book.find("p", class_ = "price_color").text
        rating_class = book.find("p", class_="star-rating")["class"][1]
        ratings = {
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
    }
        rating = ratings.get(rating_class, "0")
        availability = book.find("p", class_ = "instock availability").text.strip()
        
        results.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
        })

    return results


def save_to_csv(data: list[dict], filename: str) -> None:
    """Save scraped data to CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating", "availability"]
        )
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    books = scrape_books(URL)
    save_to_csv(books, "books.csv")
    print(f"Saved {len(books)} books to books.csv")