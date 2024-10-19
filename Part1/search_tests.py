from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)


    #FUNCTION 1 TEST
    def test_search(self):
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

        expected_music_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(search('music'), expected_music_search_results)

        expected_mayer_search_results = [] #an element not in article_titles()
        self.assertEqual(search('mayer'), expected_mayer_search_results)

        expected_french_search_results = ['French pop music'] #Single element in article_titles()
        self.assertEqual(search('french'), expected_french_search_results)

        self.assertEqual(search(''), []) # Empty keyword

        self.assertEqual(search('unknownkeyword'), []) # Keyword not found (case insensitive)

        self.assertEqual(search('dog!'), []) # Special characters in the keyword
        
        self.assertEqual(search('DoG'), expected_dog_search_results) # Keyword with mixed case
        self.assertEqual(search('mUSiC'), expected_music_search_results) # Keyword with mixed case
        self.assertEqual(search('mus'), expected_music_search_results)  # Testing partial matches

    #FUNCTION 2
    def test_title_length(self):
        expected_music_title_length_10_results = ['Rock music']
        titles_music = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(title_length(10, titles_music), expected_music_title_length_10_results) 
        self.assertEqual(title_length(100, titles_music), titles_music) #Title length larger than every title
        self.assertEqual(title_length(0, titles_music), []) #Title length zero
        self.assertEqual(title_length(-10, titles_music), []) # Negetive title length

        titles_french = ['French pop music']
        self.assertEqual(title_length(5, titles_french), []) #When title length is less than the length of all title

        self.assertEqual(title_length(10, ''), []) # When passed no titles

    #function 3 test
    
    def test_article_count(self):
        titles = ["hey", "damn", "hawa mula", "dhfdshfkhdf", "sdfdsf", "sdfd"]
        self.assertEqual(article_count(0, titles), [])
        self.assertEqual(article_count(5, []), [])
        self.assertEqual(article_count(4, titles), ["hey", "damn", "hawa mula", "dhfdshfkhdf"])
        self.assertEqual(article_count(1, titles), ["hey"])
        self.assertEqual(article_count(2, titles), ["hey", "damn"])


    #FUNCTION 4 TEST
    def test_random_article(self):
        titles = article_titles()

        self.assertEqual(random_article(1, titles), 'French pop music') #Valid index (middle element)

        self.assertEqual(random_article(0, titles), 'List of Canadian musicians') #Index is 0 (first element)

        self.assertEqual(random_article(len(titles)-1, titles), "Wake Forest Demon Deacons men's soccer") #Index is the last element

        self.assertEqual(random_article(-1, titles), '') #Negative index (invalid)
        self.assertEqual(random_article(-len(titles), titles), '') #testing a negative index equal to length of input array

        self.assertEqual(random_article(2*len(titles), titles), '') #Index out of bounds (too large)

        self.assertEqual(random_article(0, []), '')  #index on an empty list should return ''
        self.assertEqual(random_article(1000, []), '')  #testing empty list with a large index

    #FUNCTION 5 TEST
    def test_favorite_article(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']
        self.assertEqual(favorite_article('Endogenous cannabinoid', titles), True) # Testing normal functioning
        self.assertEqual(favorite_article('endogenOUs cannabinoid', titles), True) # Testing with combination of upper and lower cases
        self.assertEqual(favorite_article('   Endogenous cannabinoid   ', titles), True) # Testing normal functioning
        self.assertEqual(favorite_article('', titles), False) # No favorite title typed
        self.assertEqual(favorite_article('endogenOUs cannabinoid', []), False) # No title passed
        self.assertEqual(favorite_article('', []), False) # Titles and favorite both empty

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    #ADVANCED OPTION 1
    @patch('builtins.input')
    def test_article_title_length_test(self, input_mock):

        '''Elements exist with 15 chars'''
        keyword = 'music'
        advanced_option = 1

        output = get_print(input_mock, [keyword, advanced_option, 15]) #max 15 characters in the output
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "15\n" + "\nHere are your articles: ['Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Aube (musician)', 'Old-time music', 'Arabic music', 'Aco (musician)', '1936 in music', 'Annie (musical)', '1996 in music', '2006 in music', 'Texture (music)', '2007 in music', '2008 in music']\n"

        #print(output, expected)
        #self.maxDiff  = None  
        '''Doing the above to check what went wrong'''
        self.assertEqual(output, expected)

        
        '''Elements dont exist'''
        keyword = 'music'
        advanced_option = 1

        output = get_print(input_mock, [keyword, advanced_option, 4]) #max 4 characters in the output (elements do not exist with 4 chars that have music in them)
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "4\n" + "\nNo articles found\n"

        #print(output, expected)
        #self.maxDiff  = None  
        '''Doing the above to check what went wrong'''
        self.assertEqual(output, expected)

    #ADVANCED OPTION 6    
    @patch('builtins.input')
    def test_None_test(self, input_mock):
        keyword = 'music'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()