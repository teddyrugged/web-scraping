from bs4 import BeautifulSoup
from utils.utils import common_words
import operator
import requests
from matplotlib import pyplot as plt
import re
import csv


class WebScraper:
    # def __init__(self, URL):
    #     self.URL = URL
    
    def get_link(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.getText().strip()
        soup = soup.lower()
        soup = re.sub(r"[^\w\s]|[0-9]", "", str(soup)).split()
        return soup

    def filter_words(self, soup):

        arr = []
        for element in soup:
            if element not in common_words:
                arr.append(element)
        return arr
    
    def sort_list(self, arr):
        result = {}
        for item in arr:
            result[item] =  arr.count(item)
            a = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
        return a
    
    def reverse_data(self, a):
        highest_count = dict(sorted(a.items(), key=operator.itemgetter(1), reverse=True)[:10])
        highest_word = [k for k in highest_count.keys()]
        print(f'The top word is: {highest_word[0]}')
        return highest_count
    
class LogCsv:
    def csv_log(self, url):
        with open('log.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([url])

class Visual(WebScraper):
    
    def chart_details(self, reverse_data):
        value = [i for i in reverse_data.values()]
        key = [i for i in reverse_data.keys()]
        plt.figure(figsize =(10, 7))
        plt.pie(value, labels = key, autopct="%1.1f%%")
        plt.show()
        
        
    def graph_details(self, reverse_data):
        value = [i for i in reverse_data.values()]
        key = [i for i in reverse_data.keys()]
        plt.bar(key, value)
        plt.title("Most Occuring Words")
        plt.ylabel("Occurence")
        plt.xlabel("Words")
        plt.tight_layout()
        plt.show()
        


# scraper = WebScraper()
# scraper.get_link()
# scraper.reverse_data()[0]
# log = LogCsv()
# log.csv_log('https://www.python.org')
# vis = Visual()
# print(vis.graph_details(scraper.reverse_data()[1], scraper.reverse_data()[0]))
# print(vis.chart_details(scraper.reverse_data()[1], scraper.reverse_data()[0]))
