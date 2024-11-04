# Import Libraries
import requests
from bs4 import BeautifulSoup

# Analyze Title Tags
def analyze_title_tag(soup):
    title_tag = soup.find('title')
    if title_tag:
        return f"Title Tag: {title_tag.get_text()}"
    else:
        return "No Title Tag Found."
    
# Analyze Meta Descriptions
def analyze_meta_description(soup):
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description and meta_description.get('content'):
        return f"Meta Description: {meta_description['content']}"
    else:
        return "No Meta Description Found."
    
# Analyze Header Tags (H1, H2, H3, etc.)
def analyze_header_tags(soup):
    headers = {}
    for level in range(1, 7):
        header = soup.find_all(f'h{level}')
        headers[f'H{level}'] = [h.get_text() for h in header]
    return headers

# Analyze Image Alt Tags
def analyze_image_alt_tags(soup):
    images = soup.find_all('img')
    missing_alt = [img['src'] for img in images if not img.get('alt')]
    if missing_alt:
        return f"Images missing Alt Tags: {missing_alt}"
    else:
        return "All images have Alt Tags."

# Main Function to Run the Analyzer
def seo_analyzer(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Analyze each SEO element
            print(analyze_title_tag(soup))
            print(analyze_meta_description(soup))
            
            headers = analyze_header_tags(soup)
            for header, texts in headers.items():
                print(f"{header}: {texts}")

            print(analyze_image_alt_tags(soup))
        else:
            print(f"Error: Unable to fetch the webpage. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the SEO Analyzer
if __name__ == "__main__":
    url = input("Enter the URL of the website: ")
    seo_analyzer(url)
