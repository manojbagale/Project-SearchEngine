from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    #FUNCTION 4 UNIT TEST
    def test_most_recent_article(self):
        
        # Testing Normal Cases
        self.assertEqual(most_recent_article(search('soccer')), ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117])
        self.assertEqual(most_recent_article(search('cAnada')), ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562])
        self.assertEqual(most_recent_article(search('music')), ['Rock music', 'Mack Johnson', 1258069053, 119498])

        # Testing keywords not in the list 
        self.assertEqual(most_recent_article(search('hello')), '')

        # Testing for empty arguments passed
        self.assertEqual(most_recent_article(search('')), '')
        self.assertEqual(most_recent_article(''), '')
        self.assertEqual(most_recent_article([]), '')




        



    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()