import requests
import re

def search_keywords(url, keywords):
    # Fetch the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text content of the webpage
        webpage_text = response.text
        
        # Check for each keyword in the webpage content
        for keyword in keywords:
            # Case-insensitive search using regular expressions
            pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)
            
            # Search for the keyword in the webpage text
            matches = re.findall(pattern, webpage_text)
            
            # If there are matches, print the keyword and the number of occurrences
            if matches:
                print(f'Keyword "{keyword}" found {len(matches)} times on {url}')
    else:
        print(f'Failed to fetch {url}')

# Example usage
url = 'https://example.com'
keywords = ['Python', 'web scraping', 'data science']

search_keywords(url, keywords)
#Organic cotton
#Recycled materials
#Eco-friendly fabrics
#Fair trade
#Sustainable fashion
#Ethically sourced
#GOTS certified (Global Organic Textile Standard)
#FSC certified (Forest Stewardship Council)
#Oeko-Tex certified
# Vegan clothing
# Low-impact dyes
# Upcycled clothing
# Biodegradable materials
# Carbon-neutral production
# Zero-waste practices
# Water-saving techniques
# Locally made
# Energy-efficient production
# Non-toxic materials
# Closed-loop manufacturing