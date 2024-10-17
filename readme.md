Simplified Search Engine
Project Description
A search engine takes a given search phrase or word and finds pages on the internet that are relevant, ranks the pages, and then displays the pages in the order of ranking.

For this project, we’ll build a simplified search engine that returns articles in no particular order from searching one word, a keyword. Each search will have two parts:

Basic Search

To run a basic search, ask the user for a keyword and use the keyword to search through the complete list of articles (from wiki.article_titles()), and return the list of articles that contain the keyword. The search should not be case-sensitive (ie if a user enters “Dog”, the resulting list should return all titles with “Dog”, “dog”, "dOG", etc.). If the user does not enter anything or no results are found, return an empty list.

When running a search, the basic search will always be run, and it will always be run before the advanced search.

Advanced Search

The user is then prompted for different options to perform an advanced search. There will be 6 advanced search options:

Article title length - user provides a max article title length (in characters). After searching for article titles with the user’s keyword, return only the article titles that do not exceed the max article title length. For example, if the user searched for “dog” and wants a maximum article title length of 25 characters, only return article titles containing the word “dog” with a maximum article title length of 25 characters.

Number of articles - user provides a max number of articles to receive. After searching for article titles with the user’s keyword, return the number of articles requested by the user, starting from the first article. If the number of articles requested by the user exceeds the number of articles satisfying the keyword search, return the entire list.

Get one random article - user provides a random number. After searching for article titles with the user’s keyword, return only the article title at the index of the user’s random number. If there are no articles or the index is not within the bounds of the articles, return an empty string.

Check whether favorite article in list - user provides a favorite article title. After searching for article titles with the user’s keyword, return True if the provided article is included in the returned list of article titles and False otherwise. The search should not be case-sensitive (ex: if the favorite article title is "guide dog" and "Guide dog" is provided, returns True).

Multiple keywords - user provides another keyword to search. After searching for article titles with the user’s basic search keyword, search all of the articles again using this second keyword. Return a combined list of all articles from both search results, with the new search results coming after the initial results from the basic search.

None - user does not want an advanced search.

Examples
Note all of the below examples search for "dog" but any term is allowed.

Basic Search Only (#6):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 6

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']

Advanced Search #1 (title length):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 1
What's the max article title length (in number of characters) you're looking for? 25

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']

Advanced Search #2 (number of articles):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 2
What's the max number of articles you would like? 3

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

Advanced Search #3 (random article):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 3
Please provide a random number to get a random article: 3

Here are your articles: Black dog (ghost)

Advanced Search #4 (favorite article found):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 4
What's your favorite article title? Guide dog

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
Your favorite article is in the returned articles!

Advanced Search #4 (favorite article not found):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 4
What's your favorite article title? Great dogs

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
Your favorite article is not in the returned articles!

Advanced Search #5 (multiple keywords):

What are you searching for? dog
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 5
What's the other keyword you would like to search for? volleyball

Here are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']

No results found:

What are you searching for? cats
Any advanced searches?
1. Article title length
2. Number of articles
3. Get one random article
4. Check whether favorite article in list
5. Multiple keywords
6. None
Please enter a number corresponding to which advanced search you would like to perform: 6

No articles found

