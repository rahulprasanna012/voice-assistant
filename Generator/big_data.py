import requests
from bs4 import BeautifulSoup
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def search_and_extract(query):
    try:
        # Use requests to perform a Google search
        search_url = f"https://www.google.com/search?q={query}"

        # Set the user agent to avoid blocking
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Get the search results page
        response = requests.get(search_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the search results page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the first search result (class "g" or similar for search results)
            first_result = soup.find("div", class_="g")

            # Extract the link of the first result
            if first_result:
                first_result_link = first_result.find("a")["href"]

                # Visit the first result link and extract the webpage content
                webpage_response = requests.get(first_result_link, headers=headers)

                if webpage_response.status_code == 200:
                    webpage_content = webpage_response.text
                    soup = BeautifulSoup(webpage_content, 'html.parser')

                    # Extract text from the webpage, excluding script and style tags
                    webpage_text = ' '.join([p.get_text() for p in soup.find_all('p')])

                    # Extract and print the first 8-9 sentences from the webpage text
                    sentences = re.split(r'(?<=[.!?])\s', webpage_text)
                    result_text = '. '.join(sentences[:9])
                    return result_text
                else:
                    return "Failed to fetch the webpage content."
            else:
                return "No search result found."
        else:
            return f"Error: Unable to perform the search (Status code: {response.status_code})."

    except Exception as e:
        return f"An error occurred: {e}"


def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])


def summary(text):
    text_to_summarize = text
    summary_result = summarize_text(text_to_summarize)
    return summary_result


def deep_search(text):
    search_result = search_and_extract(text)
    if search_result:
        summarized_result = summary(search_result)
        return summarized_result
    return "No result to summarize."

