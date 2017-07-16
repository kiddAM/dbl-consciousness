from lxml import html
import requests 

class WebScraper:


    def __init__(self):
        return self 

    # returns a JSON of business information for a specified source
    def get_resources(self, source):
        resources = {}
        if(source == 'http://www.blackbusinesslist.com/online-directory1'):
            resources = black_business_list_data

        
        return resources 

    def black_business_list_data(self):
        site ='http://www.blackbusinesslist.com/online-directory1' 
        black_business_data = {}
        tree = get_tree_from(site)
        black_business_data = parse_business_list_tree(tree)
    
        return black_business_data
    

def get_tree_from(site):
    page = requests.get(site)
    tree = html.fromstring(page.content)
    return tree

# Takes a tree and returns a hash of relevant business information 
# Example JSON
# { "business_1" : { "address": {"street": "4206 Iron Ln", "state": "TX", "city": "Mansfield" } }
def parse_business_list_tree(tree):
    businesses = {}
    titles = tree.xpath('//a[@class="blog-title-link blog-link"]/text()')
    for title in titles:
        title_and_address = get_title_and_address(title) 
        title = title_and_address[0]
        address = title_and_address[1]
        city = address.split(",")[0]
        state = address.split(",")[1]
        businesses[title] = { "address": { "state": state, "city": city } }
    return businesses


def get_title_and_address(title):
        delimeter_index = title.rfind("-")
        new_title = title[0:delimeter_index]
        address = title[delimeter_index + 1: len(title)]
        return (new_title, address)
