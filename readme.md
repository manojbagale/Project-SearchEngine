
![SimpliSearch](https://github.com/user-attachments/assets/1a5b11f5-feb3-4209-8dea-d84d264a9f26)

## Project Description

A search engine takes a given search phrase or word and finds pages on the internet that are relevant, ranks the pages, and then displays the pages in the order of ranking.

For this project, we’ll build a simplified search engine that returns articles in no particular order from searching one word, a keyword. Each search will have two parts:

### 1. Basic Search

To run a basic search, ask the user for a keyword and use the keyword to search through the complete list of articles (from wiki.article_titles()), and return the list of articles that contain the keyword. The search should not be case-sensitive (ie if a user enters “Dog”, the resulting list should return all titles with “Dog”, “dog”, "dOG", etc.). If the user does not enter anything or no results are found, return an empty list.

When running a search, the basic search will always be run, and it will always be run before the advanced search.

### 2. Advanced Search

The user is then prompted for different options to perform an advanced search. There will be 6 advanced search options:

1. **Article title length** - user provides a max article title length (in characters). After searching for article titles with the user’s keyword, return only the article titles that do not exceed the max article title length. For example, if the user searched for “dog” and wants a maximum article title length of 25 characters, only return article titles containing the word “dog” with a maximum article title length of 25 characters.

2. **Number of articles** - user provides a max number of articles to receive. After searching for article titles with the user’s keyword, return the number of articles requested by the user, starting from the first article. If the number of articles requested by the user exceeds the number of articles satisfying the keyword search, return the entire list.

3. **Get one random article** - user provides a random number. After searching for article titles with the user’s keyword, return only the article title at the index of the user’s random number. If there are no articles or the index is not within the bounds of the articles, return an empty string.

4. **Check whether favorite article in list** - user provides a favorite article title. After searching for article titles with the user’s keyword, return True if the provided article is included in the returned list of article titles and False otherwise. The search should not be case-sensitive (ex: if the favorite article title is "guide dog" and "Guide dog" is provided, returns True).

5. **Multiple keywords** - user provides another keyword to search. After searching for article titles with the user’s basic search keyword, search all of the articles again using this second keyword. Return a combined list of all articles from both search results, with the new search results coming after the initial results from the basic search.

6. **None** - user does not want an advanced search.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/simplified-search-engine.git
   cd simplified-search-engine

2. **Set up the environment:**
   Ensure you have Python 3.8 or higher installed on your machine. Install the required dependencies using pip.
   
