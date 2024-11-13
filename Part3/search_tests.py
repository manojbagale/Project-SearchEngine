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
    
    #UNIT TEST 3: search
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



    #####################
    # INTEGRATION TESTS #
    #####################

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