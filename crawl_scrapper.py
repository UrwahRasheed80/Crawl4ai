import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from bs4 import BeautifulSoup
import csv

async def crawl_arxiv():
    browser_cfg = BrowserConfig(headless=True, verbose=False)
    run_cfg = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun("https://arxiv.org/search/?query=artificial+intelligence&searchtype=all", config=run_cfg)
        html = result.html

    soup = BeautifulSoup(html, "html.parser")
    papers = [[item.select_one(".title").get_text(strip=True), item.select_one(".authors").get_text(strip=True)]
              for item in soup.select(".arxiv-result")]

    with open("arxiv_papers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Authors"])
        writer.writerows(papers)
    print("arXiv data saved to arxiv_papers.csv")

if __name__ == "__main__":
    asyncio.run(crawl_arxiv())
