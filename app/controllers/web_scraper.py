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
        
        # grab all the data in the form of a tree
        tree = get_tree_from_site(site)

        # parse the tree for the information 
        # store that info in a hash and return it  

        return black_business_data




