from selenium.webdriver.common.by import By
from driver import Chrome, Firefox
from dataclasses import dataclass
import argparse
import json
import os
import sys

SITE_URL = "https://quotes.toscrape.com"

driver = Chrome()

@dataclass
class Author:
    name: str
    description: str
    birth_date: str
    birth_location: str


@dataclass
class Quote:
    text: str
    tags: list[str]


def extract_quotes(author_name: str) -> tuple[Author | None, list[Quote]]:
    driver.get(SITE_URL)

    author_url: str | None = None
    quotes: list[Quote] = []
    while True:
        quotes_el = driver.find_elements(By.CSS_SELECTOR, ".quote")
        for quote_el in quotes_el:
            q_author_name = quote_el.find_element(By.CSS_SELECTOR, ".author").text
            if author_name != q_author_name:
                continue

            c_text = quote_el.find_element(By.CSS_SELECTOR, ".text").text
            tags = [tag_el.text for tag_el in quote_el.find_elements(By.CSS_SELECTOR, "a.tag")]
            if author_url is None:
                author_url = quote_el.find_element(By.CSS_SELECTOR, ".author ~ a").get_attribute("href") or ""

            quotes.append(Quote(c_text, tags))

        if driver.find_elements(By.CSS_SELECTOR, ".pager .next") == []:
            break

        driver.find_element(By.CSS_SELECTOR, ".pager .next a").click()

    author = extract_author_info(author_url) if author_url else None
    return (author, quotes)


def extract_author_info(author_url: str) -> Author:
    driver.get(author_url)

    name = driver.find_element(By.CSS_SELECTOR, ".author-title").text
    description = driver.find_element(By.CSS_SELECTOR, ".author-description").text
    birth_date = driver.find_element(By.CSS_SELECTOR, ".author-born-date").text
    birth_location = driver.find_element(By.CSS_SELECTOR, ".author-born-location").text

    return Author(name, description, birth_date, birth_location)


def main() -> int:
    parser = argparse.ArgumentParser(description="Script para extrair citações do site Quotes to Scrape")
    parser.add_argument("autor", type=str, help="Nome do autor")
    args = parser.parse_args()

    author_name = args.autor

    (author, quotes) = extract_quotes(author_name)
    if author is None:
        print("Autor não encontrado", file=sys.stderr)
        return 1

    out = json.dumps({"author": author.__dict__, "quotes": [q.__dict__ for q in quotes]}, indent=2, ensure_ascii=False)
    print(out)

    try:
        if not os.path.exists("data"):
            os.makedirs("data")

        with open(f"data/{author_name}.json", "w") as f:
            f.write(out)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}", file=sys.stderr)

    driver.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
