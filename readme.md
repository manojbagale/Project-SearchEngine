
![SimpliSearch](https://github.com/user-attachments/assets/1a5b11f5-feb3-4209-8dea-d84d264a9f26)

## How to Make Your Repository Private

If you're working on this project and want to keep your repository private (especially for academic work), here's how to change your repository visibility on GitHub:

### Method 1: During Repository Creation
1. When creating a new repository on GitHub, look for the "Repository template" section
2. Select **Private** instead of **Public** before clicking "Create repository"

### Method 2: Change Existing Repository to Private
1. Go to your repository on GitHub.com
2. Click on the **Settings** tab (located at the top right of your repository page)
3. Scroll down to the **Danger Zone** section at the bottom of the Settings page
4. Click on **Change repository visibility**
5. Select **Make private**
6. Type your repository name to confirm the change
7. Click **I understand, change repository visibility**

### Important Notes:
- **Free GitHub accounts** can have unlimited private repositories
- Private repositories are only visible to you and collaborators you specifically invite
- If your repository was public before, it will no longer appear in search results or be accessible to others
- You can always change it back to public later using the same steps
- **For academic work**: Check with your instructor about their policy on private vs public repositories

### Adding Collaborators to Private Repositories:
1. Go to repository **Settings** → **Manage access**
2. Click **Invite a collaborator**
3. Enter their GitHub username or email
4. Choose their permission level (Read, Write, or Admin)
5. Click **Add [username] to this repository**

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


## Project[pt.2] Overview

### Part 1: Keyword Search in Article Titles
In the first part of this project, we searched a list of article titles to check if they contain a user-provided keyword as part of the title. 

### Part 2: Metadata Search
In this section, we’ll search through a 2D list of article metadata to find articles relevant to a keyword, not just those with titles that strictly include it.

- **Fetching Metadata**: Use `wiki.article_metadata()` to retrieve a 2D list where each row represents an article, containing:
    1. Article title (string)
    2. Author name (string)
    3. Publication timestamp (int, Unix/Epoch Time)
    4. Article character count (int)
    5. Keywords related to the content (list of strings)

## Project[pt.3] Overview

**Project 2: Part 3** builds on Part 2 by implementing additional search functionalities. This includes adding preprocessing functions to transform a 2D list of article metadata into a dictionary, simplifying searches. Refer to the "Project Description" for details about the task and data formatting.

---

## Starter Code
### Files Overview:
- **`search.py`**: Add search functionality.
- **`wiki.py`** (Do Not Modify): 
  - Provides raw article metadata and helper functions:
    - `article_metadata()`: Returns a complete list of article metadata.
    - `ask_search()`: Prompts for a basic search keyword.
    - `ask_advanced_search()`: Prompts for advanced search options.
- **`search_tests.py`**: Add unit and integration tests.
- **`search_tests_helper.py`** (Do Not Modify): 
  - Helper functions for integration tests:
    - `print_basic()`: Displays basic search prompt.
    - `print_advanced()`: Displays advanced search prompt.
    - `print_advanced_option()`: Displays advanced search options prompt.
    - `get_print()`: Simulates running the entire search program.


   
