# Flask-App-for-Masters
Web scraping Python Flask Application
This Python Flask web application was created as my final project for my Masters in Computer Science. 
Based around the observation that using major web search engines like Google and Bing, etc. is not very effective for users who are searching for specific, niche topics, I decided to experiment with creating a targeted search engine that only looked at appropriate sites, and returned to the user with enough real information from the site itself to decide whether or not to visit it. 

The prototype web application is created with Python Flask, using SQLite3 for data storage and extraction and Jinja2 templates for the user interface.
I used the BeautifulSoup Python library to create the web scrapers. There is also a branch showing an experiment with asynchronous scraping using the aiohttp library.  

Users select search areas from dropdown menus, and the application checks the database to see if the entries exist. If they don't the relevant site for the area are scraped and the results returned to the user as a list with links.  
For this prototype, I used only a selection of the websites for climbing walls and events venues in the UK, since it was a preliminary experiment to see the feasibility of searching this way. 

It became obvious very early on that the biggest downfalls of this approach are: 
  1) The sheer quantity of websites to scrape. Climbing is a niche sport, but is also a growing one. There are over 400 climbing centres in the UK alone, and the number grows daily. This is a huge amount of set up maintenance.
  2) The differences in website construction meaning that scrapers could not be reused. I use a parent class for the scraping methods themselves, but had to create separate (and sometimes lengthy) classes for the areas because each site required a different approach to scraping due to differences in set up.
  3) Due to point 2, the code is brittle. There is too much hard-coding in it for it to be feasible as a project that could be released and scaled up without constant maintenance and repair.

Overall, I have produced a very usable web application, but without further research into improving the scrapers, it remains infeasible as a large-scale effort. 
I would be extremely interested to see if it is possible to use AI and NLP/NLU to improve the scrapers so that they can learn what kind of content they are looking for and automate the content scraping and storage, thus reducing set up and maintenance needs. 

