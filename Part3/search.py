from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: keyword_to_titles
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping keyword to list of article titles in which the
#         articles contain keyword
#
# Example return value:
# {
#   'keyword': ['article title', 'article title 2']
#   'another_keyword': ['article title 2', 'article title 3']
# }
def keyword_to_titles(metadata):
    result = dict()
    for i in range(len(metadata)):
        for keyword in metadata[i][4]: # metadata[i][4] -> keywords
            if  not keyword in result: # if the keyword doesn't already exist as a key in result then add it
                result[keyword] = [metadata[i][0]] # metadata[i][0] -> article title
            else: 
                result[keyword].append(metadata[i][0]) # if the keyword exists as a key in result then append to it
    return result

# print(keyword_to_titles(article_metadata()))


# 2) 
#
# Function: title_to_info
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping article title to a dictionary with the following
#         keys: author, timestamp, length of article. It may be assumed that
#         the input data has unique article titles.
#
# Example return value:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'article title 2': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }
def title_to_info(metadata):
    result = dict()
    for i in range(len(metadata)):
        result[metadata[i][0]] = {
            'author': metadata[i][1],
            'timestamp': metadata[i][2],
            'length': metadata[i][3]
        }
    return result

# print(title_to_info(article_metadata()))


# 3) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of titles with articles containing the keyword, case-sensitive
#         or an empty list if none are found
def search(keyword, keyword_to_titles):
    if keyword in keyword_to_titles:
        return keyword_to_titles[keyword]
    else:
        return []


'''
Functions 4-8 are called after searching for a list of articles containing the user's keyword.
'''
# 4) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from given titles for articles that do not
#         exceed max_length number of characters
def article_length(max_length, article_titles, title_to_info):
    result = []
    for title in article_titles:
        if title_to_info[title]['length'] <= max_length:
            result.append(title)
    return result

# 5) 
#
# Function: key_by_author
#
# Parameters:
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary that maps author to a list of all articles titles written
#         by that author
#
# Example return value:
# {
#   'author': ['article title', 'article title 2'],
#   'another author': ['article title 3']
# }

# for reference: 
# Example return value for title_to_info:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'article title 2': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }

def key_by_author(article_titles, title_to_info):            
    result = {}
    for title in article_titles:
        author = title_to_info[title]['author']
        if author in result:
            result[author].append(title)
        else:
            result[author] = [title]
    return result

# 6) 
#
# Function: filter_to_author
#
# Parameters:
#   author - author name to filter results to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the initial search written by the author
#         or an empty list if none.

def filter_to_author(author, article_titles, title_to_info):
    titles_and_author = key_by_author(article_titles, title_to_info)
    if author in titles_and_author:
        return titles_and_author[author]
    else:
        return []
    
    #OR
    
    # by_author = []
    # for title, descrip in title_to_info.items():
    #     if title in article_titles and descrip["author"] == author:
    #         by_author.append(title)
            
    # return by_author

# 7) 
#
# Function: filter_out
#
# Parameters:
#   keyword - a second keyword to use to filter out results
#   article_titles - list of article titles resulting from basic search
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of articles from the basic search that do not include the
#         new keyword
def filter_out(keyword, article_titles, keyword_to_titles):
    out = [] #Initializing the output list

    if keyword not in keyword_to_titles:
        return article_titles

    new_keyword_articles = keyword_to_titles[keyword] #article titles corresponding to the new keyword

    for title in article_titles:
        if title not in new_keyword_articles: #checking if the basic search title is not in the new keyword's article titles, and include that in the output, else exclude the title
            out.append(title)
    
    return out



# 8) 
#
# Function: articles_from_year
#
# Parameters:
#   year - year (ex: 2009) to filter articles to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the basic search that were published
#         during the provided year.
def articles_from_year(year, article_titles, title_to_info):
    out = [] #Initializing the output list

    for title in article_titles: #collecting every title
            
            timestamp = title_to_info[title]['timestamp'] #collecting timestamps of every article from the title_to_info dict
            
            dt = datetime.date.fromtimestamp(timestamp) #converting the epoch time to calender time
            timestamp_year = str(dt.year) #extracting just the year

            if timestamp_year == str(year): #comparing timestamp year with input year
                out.append(title)

    return out


# Prints out articles based on searched keyword and advanced options
def display_result():
    # Preprocess all metadata to dictionaries
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search(), keyword_to_titles_dict)

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 2:
        # Update articles to be a dictionary keyed by author
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 3:
        # value stores author name
        # Update article metadata to only contain titles and timestamps
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 4:
        # value stores a second keyword
        # Filter articles to exclude those containing the new keyword.
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 5:
        # value stores year as an int
        # Update article metadata to contain only articles from that year
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

if __name__ == "__main__":
    display_result()