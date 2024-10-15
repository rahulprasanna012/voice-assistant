import requests
from bs4 import BeautifulSoup
import re

def search_brain(query):
    try:
        # URL encode the search query and construct the Google search URL
        search_url = f"https://www.google.com/search?q={query}"

        # Make a GET request to fetch the search results page
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the search results page content
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the first search result (a div with class 'g' or similar for regular search results)
            first_result = soup.find("div", class_="g")

            # Extract and clean the text
            if first_result:
                first_result_text = first_result.get_text(separator=' ')
                sentences = re.split(r'(?<=[.!?])\s', first_result_text)

                # Filter out sentences containing common link and date patterns
                filtered_sentences = [sentence for sentence in sentences if not re.search(r'https?://\S+|(\d{1,2} [A-Za-z]+ \d{4})', sentence)]

                # Join and return the remaining sentences (limit to the first 3-4 sentences)
                result_text = '. '.join(filtered_sentences[:4])
                return result_text.replace("Featured snippet from the web", "")

        return "No results found or there was an issue."

    except Exception as e:
        return f"An error occurred: {e}"

# Test the function
result = search_brain("Who is Ajith")
print(result)
