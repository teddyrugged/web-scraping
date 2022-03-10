# An entrypoint of your application
from webscaper import *
from urllib.error import HTTPError
# URL = 'https://www.python.org'



def front_end():
    scraper = WebScraper()
    log = LogCsv()
    vis = Visual()
    Code = True
    while Code:
            options = input('Would you like to scrape a website (Y/N)?').lower()
            if options == 'y':
                url = input('Enter a website to scrape: ')
                a = scraper.get_link(url)
                b = scraper.filter_words(a)
                c = scraper.sort_list(b)
                d = scraper.reverse_data(c)
                log.csv_log(url)
                vis.graph_details(d)
                vis.chart_details(d)
    
            elif options == 'n':
                print('Thanks for analysing! Come back again!!! ')
                code = False
                
front_end()
        