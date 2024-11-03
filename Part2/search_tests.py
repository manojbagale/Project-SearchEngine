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

    # FUNCTION 4 UNIT TEST
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


    # FUNCTION 5 UNIT TEST
    def test_favorite_author(self):
        # Test normal cases
        self.assertEqual(favorite_author('mack johnson',search('soccer')), True)
        self.assertEqual(favorite_author('Nihonjoe',search('music')), True)
        self.assertEqual(favorite_author('hello',search('music')), False)
    
        # Test no fav auther entered
        self.assertEqual(favorite_author('',search('music')), False)

        # Fav auther searched in list with no metadata
        self.assertEqual(favorite_author('mack johnson',[]), False)

        # Empty fav author in empty metadata
        self.assertEqual(favorite_author('',[]), False)





        



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

    # FUNCTION 4 INTEGRATION TEST
    @patch('builtins.input')
    def test_most_recent_article_test(self, input_mock):

        # Test Normal Case
        keyword = 'soccer'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n" + "Here are your articles: ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]\n"

        self.assertEqual(output, expected)

        # Test when keyword has no titles relating to it 
        keyword = 'hello'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n" + "No articles found\n"

        self.assertEqual(output, expected)

        # Test no keyword entered and asked for latest
        keyword = ''
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n" + "No articles found\n"

        self.assertEqual(output, expected)        


    # FUNCTION 5 INTEGRATION TEST
    @patch('builtins.input')
    def test_favorite_author_test(self, input_mock):

        # Test Normal Case: True
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'Nihonjoe'
        article_list = "[['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\n" + "Here are your articles: " + article_list + "\n" + "Your favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

        # Test Normal Case: False
        advanced_response = 'hello'
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\n" + "Here are your articles: " + article_list + "\n" + "Your favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)

        # Test no fav auther entered
        advanced_response = ''
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\n" + "Here are your articles: " + article_list + "\n" + "Your favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)

        # Fav auther searched when keyword had no titles related to it
        keyword = 'hello'
        advanced_option = 4
        advanced_response = 'Nihonjoe'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\n" + "No articles found"+ "\n" + "Your favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)

        # Neither keyword nor fav auther entered
        keyword = ''
        advanced_option = 4
        advanced_response = ''

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\n" + "No articles found"+ "\n" + "Your favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)



# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()