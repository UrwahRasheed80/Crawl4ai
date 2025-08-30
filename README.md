#  Day 2 – Crawl4AI Scraping  

In this task, we explored how to use **Crawl4AI** to scrape data from the web efficiently.  
We focused on two case studies:  

-  Research Papers from **arXiv**  
-  Job Listings from **Indeed**  

---

##  1. Installation  

First, install Crawl4AI using pip:  

```bash
pip install crawl4ai

## 2. Scraping Research Papers (arXiv)

We used **Crawl4AI** to fetch research paper metadata from **arXiv**.

### 2.1 Example Code

```python
from crawl4ai import Crawl4AI

# Initialize crawler
crawler = Crawl4AI()

# Define target URL
url = "https://arxiv.org/list/cs.AI/recent"

# Scrape data
data = crawler.scrape(url)

# Print result
print(data[:5])  # Display first 5 papers
3. Scraping Jobs (Indeed)

We also scraped job listings from Indeed.

3.1 Example Code
from crawl4ai import Crawl4AI

crawler = Crawl4AI()

url = "https://www.indeed.com/jobs?q=data+scientist&l=remote"

data = crawler.scrape(url)

print(data[:5])  # Display first 5 job listings

4. Key Learnings

Crawl4AI makes web scraping easier with minimal setup

Can extract structured data (JSON format)

Works well for both academic research and job market analysis

