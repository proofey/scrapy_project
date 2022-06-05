This is a Scrapy Framework project.The script in this repository scrapes data from a particular website.After the scraping is done all the data is
stored in a sqlite database file.

If you want to try it follow these steps:

1.First I recommend you to create a Python virtual environment 
(Check this link in case you don't know how to do it - https://docs.python.org/3/library/venv.html)
2.Clone the repository inside your venv.
3.Open your terminal and navigate to the project folder where the requirements.txt file is.
Execute the following command: pip install -r requirements.txt.
The command will install all the packages that are required for this script.
4.Finally execute this command in the terminal to start the script: scrapy crawl devices
It may take some time but after the scraping is done you will see a 'devices.db' file inside the project folder with all the scraped data in it.

