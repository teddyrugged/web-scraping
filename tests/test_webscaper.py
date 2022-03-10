import unittest
from webscaper import WebScraper


class TestWebScaper(unittest.TestCase):
    
    def setUp(self):
        self.check_web = WebScraper()
        self.link = self.check_web.get_link('https://www.python.org')
        self.words = self.check_web.filter_words(self.link)
        self.sort = self.check_web.sort_list(self.words)
        self.reverse = self.check_web.reverse_data(self.sort)
    
    def test_get_link(self):
        self.assertTrue(self.link)
        
    def test_filter_words(self):
        self.assertTrue(self.words)
    
    def test_sort_list(self):
        self.assertTrue(self.sort)
    
    def test_reverse_data(self):
        self.assertEqual(self.reverse)
    
    


























# from webscaper import webscraper
# from matplotlib import pyplot as plt

# class Visual:
#     def __init__(self) -> None:
#         pass
    
#     def graph_details(self, key, value):
#         plt.figure(figsize =(10, 7))
#         plt.pie(value, labels = key, autopct="%1.1f%%")
#         plt.show()
        
        
#     def chart_details(self, value, key):
#         plt.bar(value, key)
#         plt.title("Most Occuring Words")
#         plt.ylabel("Occurence")
#         plt.xlabel("Words")
#         plt.tight_layout()
#         plt.show()
        

# vis = Visual()
# # print(vis.graph_details(webscraper.reverse_data()[1], webscraper.reverse_data()[0]))
# print(webscraper.reverse_data()[1])