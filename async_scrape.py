"""parent class containing the synchronous web scraping methods utilised
by the child scraper data/parser classes"""
import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup

class AsyncScraper:
    """class containing the methods for the asynchronous web scraper"""
    def __init__(self):
        self.soups = []

    """method called from child class, which takes the passed in list of
    URLs and initialises a loop that will run each of the URLs through the
    scraper by calling main()"""
    def start_scrape(self, urls_to_scrape):
        self.urls = urls_to_scrape
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main(self.urls))

    """method to gather all of the site data as it is returned"""
    async def return_soup(self, soup):
        self.soups.append(soup)
        return self.soups

    """method that takes each URL from main() and sends a request
    to the host server for the page. Once the response is received it is 
    sent to the return_soup() method to be passed back out to the child class 
    as a list of soups"""
    async def scrape(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                body = await resp.text()
                soup = BeautifulSoup(body, 'html.parser')
                await self.return_soup(soup)

    """method that arranges the input URLs into a group and sends 
    it to scrape() in order to be scraped asynchronously"""
    async def main(self, urls_to_scrape):
        start_time = time.time() # set start time for comparison

        tasks = []
        urls = []
        for url in urls_to_scrape:
            urls.append(url)

        for row in urls:
            task = asyncio.create_task(self.scrape(row))
            tasks.append(task)

        await asyncio.gather(*tasks)

        # compare finish time to start time for comparison
        time_difference = time.time() - start_time
        print(f'Scraping time: %.2f seconds.' % time_difference)
