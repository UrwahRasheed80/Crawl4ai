import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from bs4 import BeautifulSoup
import csv

async def crawl_indeed():
    browser_cfg = BrowserConfig(headless=True, verbose=False)
    run_cfg = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun("https://pk.indeed.com/jobs?q=python+developer", config=run_cfg)
        html = result.html

    soup = BeautifulSoup(html, "html.parser")
    jobs = [[job.select_one("h2 span").get_text(strip=True) if job.select_one("h2 span") else "N/A",
             job.select_one(".companyName").get_text(strip=True) if job.select_one(".companyName") else "N/A"]
            for job in soup.select(".job_seen_beacon")]

    with open("indeed_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Company"])
        writer.writerows(jobs)
    print("Indeed data saved to indeed_jobs.csv")

if __name__ == "__main__":
    asyncio.run(crawl_indeed())
