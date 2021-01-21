import requests
from parsel import Selector

url = 'https://www.vultr.com/products/cloud-compute/#pricing'
text = requests.get(url).text
selector = Selector(text=text)
'''
url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)
'''
element_header = selector.xpath(
    '''//div[starts-with 
  (@class, "pt__header")]/div[starts-with 
  (@class, "pt__cell")]/text()'''
).getall()

element_body = selector.xpath(
    '//div[starts-with (@class, "pt__cell")]/span/strong/text()').getall()
