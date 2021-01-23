import requests
from parsel import Selector


def crawler_vultr():
    url = 'https://www.vultr.com/products/cloud-compute/#pricing'
    text = requests.get(url).text
    selector = Selector(text=text)

    element_header = selector.xpath(
        '''//div[starts-with 
      (@class, "pt__header")]/div[starts-with 
      (@class, "pt__cell")]/text()'''
    ).getall()

    element_body = selector.xpath(
        '//div[starts-with (@class, "pt__cell")]/span/strong/text()').getall()

    element_memory = selector.xpath(
        '//div[starts-with (@class, "pt__cell")]/strong/text()').getall()

    return element_header, element_body, element_memory


def crawler_ocean():
    url = 'https://www.digitalocean.com/pricing/'
    text = requests.get(url).text
    selector = Selector(text=text)

    element_header = selector.xpath(
        '''//div[starts-with 
      (@class, "container")]/table/thead/tr/th/text()'''
    ).getall()

    element_body = selector.xpath(
        '''//div[starts-with 
      (@class, "container")]/table/tbody/tr/td/text()'''
    ).getall()

    return element_header, element_body
