import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup


class AsyncScraper:
    def __init__(self):
        self.soups = []

    def start_scrape(self, urls_to_scrape):
        self.urls = urls_to_scrape
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main(self.urls))

    async def return_soup(self, soup):
        self.soups.append(soup)

        #for soup in self.soups:
        #    print(soup)
        return self.soups

    async def scrape(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                body = await resp.text()
                soup = BeautifulSoup(body, 'html.parser')
                await self.return_soup(soup)

    async def main(self, urls_to_scrape):
        start_time = time.time()

        tasks = []
        urls = []
        for url in urls_to_scrape:
            urls.append(url)

        for row in urls:
            task = asyncio.create_task(self.scrape(row))
            tasks.append(task)

        await asyncio.gather(*tasks)

        time_difference = time.time() - start_time
        print(f'Scraping time: %.2f seconds.' % time_difference)
