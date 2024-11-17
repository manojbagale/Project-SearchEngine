from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    # UNIT TEST 1: keyword_to_titles
    def test_keyword_to_titles(self):
        # Test case 1: Basic functionality with multiple keywords
        metadata1 = [
            ["Title 1", "Author A", 1618637717, 500, ["tech", "computer"]],
            ["Title 2", "Author B", 717104905, 600, ["health", "computer"]],
            ["Title 3", "Author C", 870058258, 700, ["tech", "health"]],
        ]
        expected_output1 = {
            "tech": ["Title 1", "Title 3"],
            "computer": ["Title 1", "Title 2"],
            "health": ["Title 2", "Title 3"],
        }
        self.assertEqual(keyword_to_titles(metadata1), expected_output1)

        # Test case 2: Single article with multiple keywords
        metadata2 = [
            ["Title A", "Author X", 849626049, 300, ["science", "innovation", "education"]],
        ]
        expected_output2 = {
            "science": ["Title A"],
            "innovation": ["Title A"],
            "education": ["Title A"],
        }
        self.assertEqual(keyword_to_titles(metadata2), expected_output2)

        # Test case 3: No articles (empty metadata)
        metadata3 = []
        expected_output3 = {}
        self.assertEqual(keyword_to_titles(metadata3), expected_output3)

        # Test case 4: Keywords with no overlap between articles
        metadata4 = [
            ["Article 1", "Author 1", 1392057401, 400, ["finance"]],
            ["Article 2", "Author 2", 1476380860, 500, ["travel"]],
            ["Article 3", "Author 3", 27285498, 600, ["cooking"]],
        ]
        expected_output4 = {
            "finance": ["Article 1"],
            "travel": ["Article 2"],
            "cooking": ["Article 3"],
        }
        self.assertEqual(keyword_to_titles(metadata4), expected_output4)

    
    # UNIT TEST 2: title_to_info
    def test_title_to_info(self):
        # Test case 1: Basic functionality with multiple articles
        metadata1 = [
            ["Title 1", "Author A", 1618637717, 500, ["tech", "AI"]],
            ["Title 2", "Author B", 717104905, 600, ["health", "AI"]],
            ["Title 3", "Author C", 870058258, 700, ["tech", "health"]],
        ]
        expected_output1 = {
            "Title 1": {"author": "Author A", "timestamp": 1618637717, "length": 500},
            "Title 2": {"author": "Author B", "timestamp": 717104905, "length": 600},
            "Title 3": {"author": "Author C", "timestamp": 870058258, "length": 700},
        }
        self.assertEqual(title_to_info(metadata1), expected_output1)

        # Test case 2: Single article with metadata
        metadata2 = [
            ["Title A", "Author X", 849626049, 300, ["science", "innovation", "education"]],
        ]
        expected_output2 = {
            "Title A": {"author": "Author X", "timestamp": 849626049, "length": 300},
        }
        self.assertEqual(title_to_info(metadata2), expected_output2)

        # Test case 3: No articles (empty metadata)
        metadata3 = []
        expected_output3 = {}
        self.assertEqual(title_to_info(metadata3), expected_output3)
    
    # UNIT TEST 3: search
    def test_search(self):
        # Basic Test Case: keyword is present in the dictionary
        keyword_to_titles1 = {
            "tech": ["Title 1", "Title 3"],
            "computer": ["Title 1", "Title 2"],
            "health": ["Title 2", "Title 3"]
        }
        self.assertEqual(search("computer", keyword_to_titles1), ["Title 1", "Title 2"])

        # Test Case: keyword not present in the dictionary
        self.assertEqual(search("technology", keyword_to_titles1), [])

        # Edge Case: keyword is present but with case sensitivity
        self.assertEqual(search("tech", keyword_to_titles1), ["Title 1", "Title 3"])
        self.assertEqual(search("tEch", keyword_to_titles1), [])
        
        # Edge Case: Empty keyword input
        self.assertEqual(search("", keyword_to_titles1), [])
        
        # Edge Case: Empty dictionary
        self.assertEqual(search("science", {}), [])

         # Edge Case: Multiple keywords with similar names
        keyword_to_titles2 = {
            "health": ["Article x"],
            "Health": ["Article y"],
            "health-care": ["Article z"],
        }
        self.assertEqual(search("health", keyword_to_titles2), ["Article x"])
        self.assertEqual(search("Health", keyword_to_titles2), ["Article y"])
        self.assertEqual(search("health-care", keyword_to_titles2), ["Article z"])

    # UNIT TEST 4: Article Length
    def test_article_length(self):
        # '''creating sample examples to work on'''
        article_titles =  ['List of Canadian musicians', 'Edogawa, Tokyo']
        title_to_info = {
            'List of Canadian musicians' : {
                'author': 'Jack Ma',
                'timestamp': 1181623340,
                'length': 21023
            }, 
            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607041,
                'length': 4526
            }
        }
        self.assertEqual(article_length(2000, article_titles, title_to_info), [])
        self.assertEqual(article_length(100000, [], {}), [])
        self.assertEqual(article_length(25000, article_titles, title_to_info), ['List of Canadian musicians', 'Edogawa, Tokyo'])
        self.assertEqual(article_length(4527, article_titles, title_to_info), ['Edogawa, Tokyo'])

    # UNIT TEST 5: Key by Author
    def test_key_by_author(self):
        # '''creating sample examples to work on'''
        title_to_info_1 = {
            'List of Canadian musicians' : {
                'author': 'Jack Ma',
                'timestamp': 1181623340,
                'length': 21023
            }, 

            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607041,
                'length': 4526
            }
        } 
        expected_output_1 = {
           'Jack Ma': ['List of Canadian musicians'],
           'jack johnson': ['Edogawa, Tokyo'] 
        }

        title_to_info_2 = {
            'title1' : {
                'author': 'heyman',
                'timestamp': '2000',
                'length': 'length1'
            },
            'title2' :{
                'author': 'damnman',
                'timestamp': 'stamp2',
                'length': 'length2'
            },
            'title3' : {
                'author': 'heyman',
                'timestamp': 'stamp3',
                'length': 'length3'
            }
        }
        expected_output_2 = {
            'heyman' : ['title1', 'title3'],
            'damnman': ['title2']
        }

        self.assertEqual(key_by_author([], {}), {})
        self.assertEqual(key_by_author(['List of Canadian musicians', 'Edogawa, Tokyo'], title_to_info_1), expected_output_1)
        self.assertEqual(key_by_author(['title1', 'title2', 'title3'], title_to_info_2), expected_output_2)
        
        
    # UNIT TEST 6: Filter to Author
    def test_filter_to_author(self):
        article_titles =  ['List of Canadian musician', 'Edogawa, Tokyo']
        title_to_info = {
            'List of Canadian musician' : {
                'author': 'Jack Ma',
                'timestamp': 118162,
                'length': 21047
            }, 

            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607789,
                'length': 4574
            }
        } 
        
        author1 = 'Jack Ma'
        expected_output1 = ['List of Canadian musician']

        author2 = 'hey-damn-man'
        expected_output2 =[]

        self.assertEqual(filter_to_author(author1, article_titles, title_to_info), expected_output1)
        self.assertEqual(filter_to_author('', article_titles, title_to_info), [])
        self.assertEqual(filter_to_author('', [], {}), [])
        self.assertEqual(filter_to_author('Hi', [], {}), [])
        self.assertEqual(filter_to_author(author2, article_titles, title_to_info), expected_output2)

    
    # UNIT TEST 7: Testing Filter out
    def test_filter_out(self):
        # Sample data to simulate the metadata and the result of keyword_to_titles
        article_metadata = [
            ['Article 1', 'Author A', 1234567890, 5000, ['soccer', 'sports']],
            ['Article 2', 'Author B', 1234567900, 4500, ['soccer', 'football']],
            ['Article 3', 'Author C', 1234567910, 2000, ['sports', 'outdoor']],
            ['Article 4', 'Author A', 1234567920, 6000, ['gaming', 'esports']],
            ['Article 5', 'Author B', 1234567930, 4000, ['technology', 'gaming']]
        ]

        # Simulating the output of `keyword_to_titles`
        keyword_to_titles = {
            'soccer': ['Article 1', 'Article 2'],
            'sports': ['Article 1', 'Article 3'],
            'gaming': ['Article 4', 'Article 5'],
        }
        
        #Basic search has articles that do not contain the second keyword.
        article_titles = ['Article 1', 'Article 2', 'Article 3']
        result = filter_out('gaming', article_titles, keyword_to_titles)
        assert result == ['Article 1', 'Article 2', 'Article 3']

        article_titles = ['Article 1', 'Article 3']
        result = filter_out('gaming', article_titles, keyword_to_titles)
        assert result == ['Article 1', 'Article 3']

        article_titles = ['Article 1', 'Article 3', 'Article 2']
        result = filter_out('basketball', article_titles, keyword_to_titles)
        assert result == ['Article 1', 'Article 3', 'Article 2']


        #All articles contain the second keyword. (e.g., exclude 'gaming')
        article_titles = ['Article 4', 'Article 5']
        result = filter_out('gaming', article_titles, keyword_to_titles)
        assert result == []

        #The second keyword is an empty string, should return the same article list as the basic search.
        article_titles = ['Article 1', 'Article 3']
        result = filter_out('', article_titles, keyword_to_titles)
        assert result == ['Article 1', 'Article 3']

        #Basic search has all articles from the keyword list, and we are filtering out a present keyword ('sports').
        article_titles = ['Article 1', 'Article 2', 'Article 3']
        result = filter_out('sports', article_titles, keyword_to_titles)
        assert result == ['Article 2']

        #case sensitive test with Soccer instead of soccer
        article_titles = ['Article 1', 'Article 2']
        result = filter_out('Soccer', article_titles, keyword_to_titles)
        assert result == ['Article 1', 'Article 2']


        #Edge case with an empty list of articles from the basic search.
        article_titles = []
        result = filter_out('gaming', article_titles, keyword_to_titles)
        assert result == []


    # UNIT TEST 8: Testing articles_from_year
    def test_articles_from_year(self):
        # Sample article data (article titles and their metadata)
        article_metadata = [
            ['Article 1', 'Author A', 1577836800, 5000, ['sports']],  # 2019-12-31
            ['Article 2', 'Author B', 1609459200, 4500, ['football']],  # 2020-12-31
            ['Article 3', 'Author C', 1612137600, 3000, ['technology']],  # 2021-01-31
            ['Article 4', 'Author D', 1596240000, 2000, ['gaming']],  # 2020-07-31
            ['Article 5', 'Author E', 1583020800, 4000, ['outdoor']],  # 2020-02-29
            ['Article 6', 'Author F', 1585699200, 6000, ['sports']],  # 2020-03-31
            ['Article 7', 'Author G', 1606790400, 3500, ['technology']],  # 2020-11-30
            ['Article 8', 'Author H', 1614556800, 2500, ['gaming']],  # 2021-02-28
        ]


        # Dictionary to map article title to its metadata (author, timestamp, length)
        title_to_info = {
            'Article 1': {'author': 'Author A', 'timestamp': 1577836800, 'length': 5000},
            'Article 2': {'author': 'Author B', 'timestamp': 1609459200, 'length': 4500},
            'Article 3': {'author': 'Author C', 'timestamp': 1612137600, 'length': 3000},
            'Article 4': {'author': 'Author D', 'timestamp': 1596240000, 'length': 2000},
            'Article 5': {'author': 'Author E', 'timestamp': 1583020800, 'length': 4000},
            'Article 6': {'author': 'Author F', 'timestamp': 1585699200, 'length': 6000},
            'Article 7': {'author': 'Author G', 'timestamp': 1606790400, 'length': 3500},
            'Article 8': {'author': 'Author H', 'timestamp': 1614556800, 'length': 2500},
        }

        # List of article titles
        article_titles = ['Article 1', 'Article 2', 'Article 3', 'Article 4', 'Article 5', 'Article 6', 'Article 7', 'Article 8']

        #Nomal cases where some of the article_titles match the year and get removed
        
        result = articles_from_year(2020, article_titles, title_to_info)
        self.assertEqual(result, ['Article 2', 'Article 4', 'Article 5', 'Article 6', 'Article 7'])

        result = articles_from_year(2019, article_titles, title_to_info)
        self.assertEqual(result, ['Article 1'])

        result = articles_from_year(2021, article_titles, title_to_info)
        self.assertEqual(result, ['Article 3', 'Article 8'])

        result = articles_from_year(2030, article_titles, title_to_info) #non existent date
        self.assertEqual(result, [])

        result = articles_from_year(2020, [], title_to_info) #no articles to start with (empty list)
        self.assertEqual(result, [])




    #####################
    # INTEGRATION TESTS #
    #####################
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    Integration tests for "advanced options". Remember: there are 6 total advanced options. 
    '''
    
    # INTEGRATION TEST: ADVANCED OPTION 1: Article length
    @patch('builtins.input')
    def test_advanced_option_1_article_length(self, input_mock):
        '''
        "heyman" as the keyword and 4000 the advanced reponse. 
        '''
        keyword = 'heyman'
        advanced_option = 1
        advanced_response = 4000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
        
        '''
        "music" as the keyword and 6000 the advanced reponse. 
        '''
        keyword = 'music'
        advanced_option = 1
        advanced_response = 6000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['French pop music', 'Kevin Cadogan', 'Lights (musician)', 'Tim Arnold (musician)', 'Joe Becker (musician)', 'List of gospel musicians', 'Texture (music)']\n"

        self.assertEqual(output, expected)

    # INTEGRATION TEST: ADVANCED OPTION 2: Key by author
    @patch('builtins.input')
    def test_advanced_option_2_key_by_author(self, input_mock):
        '''
        "music" as the keyword
        '''
        keyword = 'indian'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Burna Boy': ['Indian classical music']}\n"

        self.assertEqual(output, expected)
        
        '''
        "football" as the keyword
        '''
        keyword = 'football'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Burna Boy': ['Georgia Bulldogs football']}\n"

        self.assertEqual(output, expected)

    # INTEGRATION TEST: ADVANCED OPTION 3: Filter to author
    @patch('builtins.input')
    def test_advanced_option_3_filter_to_author(self, input_mock):
        '''
        "music" as the keyword and man as the advanced response
        '''
        keyword = 'music'
        advanced_option = 3
        advanced_response = 'man'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
        
        '''
        "India" as the keyword and Jack as the advanced response
        '''
        keyword = 'India'
        advanced_option = 3
        advanced_response = 'Jack'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
        
        '''
        "music" as the keyword and Burna Boy as the advanced response
        '''
        keyword = 'music'
        advanced_option = 3
        advanced_response = 'Burna Boy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lights (musician)', 'Indian classical music', 'Tony Kaye (musician)', '2008 in music']\n"

        self.assertEqual(output, expected)

    
    # INTEGRATION TEST: ADVANCED OPTION 4: Filter out keyword
    @patch('builtins.input')
    def test_advanced_option_4_filter_out_keyword(self, input_mock):
        '''
        "music" as the keyword and man as the advanced response
        '''
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'man'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)
        
        '''
        soccer as the keyword and Jack as the advanced response
        '''
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = 'Jack'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)
        
        '''
        "music" as the keyword and Burna Boy as the advanced response
        Burna Boy is not in the keywords of any of the titles
        '''
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'Burna Boy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)

        '''
        "Hotel California" as the keyword and "nonexistent" as the advanced response 
        Hotel California itself will return an empty list so additional search wont even matter
        '''
        keyword = 'Hotel California'
        advanced_option = 4
        advanced_response = "nonexistent"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)



    # INTEGRATION TEST: ADVANCED OPTION 5: Articles from year
    @patch('builtins.input')
    def test_advanced_option_5_filter_by_year(self, input_mock):
        '''
        "soccer" as the keyword and 2008 as the advanced response
        this will effectively filter out the other years
        '''
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2008

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Will Johnson (soccer)']\n"

        self.assertEqual(output, expected)


        '''
        "soccer" as the keyword and 1130 as the advanced response
        This wont filter out anything and so wont return anything
        '''
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 1130

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)


        '''
        "canada" as the keyword and 2008 as the advanced response
        this also filters out the keywords
        '''
        keyword = 'canada'
        advanced_option = 5
        advanced_response = 2008

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lights (musician)', 'Will Johnson (soccer)']\n"

        self.assertEqual(output, expected)


        '''
        "music" as the keyword and 2005 as the advanced response
        this also filters out the keywords
        '''
        keyword = 'music'
        advanced_option = 5
        advanced_response = 2005

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Old-time music']\n"

        self.assertEqual(output, expected)


        '''
        "comedy" as the keyword and 2004 as the advanced response
        "comedy" already doesn't return any articles so futher filtering will also return out nothing
        '''
        keyword = 'comedy'
        advanced_option = 5
        advanced_response = 2004

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
        
        

        
    # INEGRATION TEST : ADVANCED OPTION 6: None  
    @patch('builtins.input')
    def test_advanced_option_6_none(self, input_mock):
        # Check for keyword dog
        keyword = 'dog'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option, ])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']\n"
        self.assertEqual(output, expected)

        # Check for keyword hello : Not found
        keyword = 'hello'

        output = get_print(input_mock, [keyword, advanced_option, ])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"
        self.assertEqual(output, expected)
        

    # @patch('builtins.input')
    # def test_example_integration_test(self, input_mock):
    #     keyword = 'soccer'
    #     advanced_option = 5
    #     advanced_response = 2009

    #     output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    #     expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

    #     self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()