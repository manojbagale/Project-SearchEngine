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

    # FUNCTION 1 UNIT TEST
    def test_search(self):

        # Basic Test
        output_for_rock = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], 
                                  ['Noise (music)', 'jack johnson', 1194207604, 15641], 
                                  ['2009 in music', 'RussBot', 1235133583, 69451], 
                                  ['Rock music', 'Mack Johnson', 1258069053, 119498], 
                                  ['Arabic music', 'RussBot', 1209417864, 25114], 
                                  ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], 
                                  ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], 
                                  ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], 
                                  ['2006 in music', 'Jack Johnson', 1171547747, 105280], 
                                  ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], 
                                  ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], 
                                  ['2007 in music', 'Bearcat', 1169248845, 45652], 
                                  ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        
        assert search('rock') == output_for_rock
        # Case-Insensitive test
        assert search('RoCk') == output_for_rock

        assert search('soCcER') == [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], 
                                    ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], 
                                    ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]

        # No Matches Test
        assert search('nonexistent') == []
        assert search('Bearcat') == []

        # Empty Keyword Test
        assert search('') == []

        # Partial Matches Test (should not match partially)
        assert search('mu') == []
        assert search('a') == []

        # Numeric Keyword Test
        assert search('2007') == [['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116], 
                                  ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], 
                                  ['Annie (musical)', 'Jack Johnson', 1223619626, 27558], 
                                  ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], 
                                  ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], 
                                  ['2007 in music', 'Bearcat', 1169248845, 45652], 
                                  ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]]
        
        assert search('2008') == [['2009 in music', 'RussBot', 1235133583, 69451], 
                                  ['Lights (musician)', 'Burna Boy', 1213914297, 5898], 
                                  ['USC Trojans volleyball', 'jack johnson', 1218049435, 5525], 
                                  ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], 
                                  ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], 
                                  ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], 
                                  ['Personal computer', 'Pegship', 1220391790, 45663], 
                                  ['2008 in music', 'Burna Boy', 1217641857, 107605], 
                                  ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]]
        

    # FUNCTION 2 UNIT TEST
    def test_article_length(self):

        
        #I'm using a sample metadata for this part so there is less volume of data to deal with.
        sample_metadata = [
            ['Landseer (dog)', 'Bearcat', 1231438650, 2006],
            ['Charles McPherson (musician)', 'Bearcat', 1255183865, 3007],
            ['Comparison of programming languages (basic instructions)', 'RussBot', 1238781354, 61644],
            ['Les Cousins (music club)', 'Mack Johnson', 1187072433, 4926],
            ['Paul Carr (musician)', 'Burna Boy', 1254142018, 5716],
            ['2006 in music', 'Jack Johnson', 1171547747, 105280],
            ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413],
            ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638],
            ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419],
            ['Danja (musician)', 'RussBot', 1257155543, 6925],
            ['Ruby (programming language)', 'Bearcat', 1193928035, 30284],
            ['Texture (music)', 'Bearcat', 1161070178, 3626],
            ['List of computer role-playing games', 'Mr Jake', 1179441080, 43088],
            ['Register (music)', 'Pegship', 1082665179, 598],
            ['Mode (computer interface)', 'Pegship', 1182732608, 2991],
            ['2007 in music', 'Bearcat', 1169248845, 45652],
            ['List of video games with time travel', 'Mack Johnson', 1234110556, 2344],
            ['2008 in music', 'Burna Boy', 1217641857, 107605],
            ['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616],
            ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]
        ]

        # Basic test
        assert article_length(5000, sample_metadata) == [['Landseer (dog)', 'Bearcat', 1231438650, 2006], 
                                                         ['Charles McPherson (musician)', 'Bearcat', 1255183865, 3007], 
                                                         ['Les Cousins (music club)', 'Mack Johnson', 1187072433, 4926], 
                                                         ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413], 
                                                         ['Texture (music)', 'Bearcat', 1161070178, 3626], 
                                                         ['Register (music)', 'Pegship', 1082665179, 598], 
                                                         ['Mode (computer interface)', 'Pegship', 1182732608, 2991], 
                                                         ['List of video games with time travel', 'Mack Johnson', 1234110556, 2344]]

        # exact length match
        assert article_length(61644, sample_metadata) == [['Landseer (dog)', 'Bearcat', 1231438650, 2006],
                                                        ['Charles McPherson (musician)', 'Bearcat', 1255183865, 3007],
                                                        ['Comparison of programming languages (basic instructions)', 'RussBot', 1238781354, 61644],
                                                        ['Les Cousins (music club)', 'Mack Johnson', 1187072433, 4926],
                                                        ['Paul Carr (musician)', 'Burna Boy', 1254142018, 5716],
                                                        ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413],
                                                        ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638],
                                                        ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419],
                                                        ['Danja (musician)', 'RussBot', 1257155543, 6925],
                                                        ['Ruby (programming language)', 'Bearcat', 1193928035, 30284],
                                                        ['Texture (music)', 'Bearcat', 1161070178, 3626],
                                                        ['List of computer role-playing games', 'Mr Jake', 1179441080, 43088],
                                                        ['Register (music)', 'Pegship', 1082665179, 598],
                                                        ['Mode (computer interface)', 'Pegship', 1182732608, 2991],
                                                        ['2007 in music', 'Bearcat', 1169248845, 45652],
                                                        ['List of video games with time travel', 'Mack Johnson', 1234110556, 2344],
                                                        ['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616],
                                                        ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]]
        
        # Edge Case Test: Empty Metadata List
        assert article_length(1000, []) == []

        # entering zero
        assert article_length(0, sample_metadata) == []

        # length exceeds upper bound so the entire metadata is returned
        assert article_length(200000, sample_metadata) == sample_metadata

        # Test with max_length smaller Than smallest article
        assert article_length(500, sample_metadata) == []

        # only one article with length <= max_length
        single_article_metadata = [['Test Article', 'Author', 1234567890, 1234]]
        assert article_length(1234, single_article_metadata) == single_article_metadata

        # no articles satisfying the conditions
        assert article_length(1000, single_article_metadata) == []

    # FUNCTION 3 UNIT TEST
    def test_unique_authors(self):
        
        search_results = [
        ['Rock music', 'Raken Maharjan', 1258069053, 119498],
        ['Fisk University', 'Damnman', 1263393671, 16246],
        ['Jazz Studies', 'Mack Johnson', 1267891234, 154321],
        ['Science and Technology', 'Dr. Brown', 1274567890, 145678]
        ]
        
        self.assertEqual(unique_authors(4, search_results), search_results)
        self.assertEqual(unique_authors(1, search_results), [['Rock music', 'Raken Maharjan', 1258069053, 119498]])
        self.assertEqual(unique_authors(0, search_results), [])
        self.assertEqual(unique_authors(-1, search_results), [])

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
        
        
    # FUNCTION 6 UNIT TEST
    def test_refine_search(self):
        search_results = [
            ['Rock music', 'Mack Johnson', 1258069053, 119498], 
            ['Fisk University', 'RussBot', 1263393671, 16246]
            ]
        self.assertEqual(refine_search('student', search_results), [['Fisk University', 'RussBot', 1263393671, 16246]])
        self.assertEqual(refine_search('heyman', search_results), [])
        self.assertEqual(refine_search('', search_results), [])







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

    
    # ADVANCED OPTION 2: INTEGRATION TEST
    @patch('builtins.input')
    def test_number_of_unique_authors(self, input_mock):

        #testing for normal cases
        keyword = 'mLs'
        advanced_option = 2
        advanced_response = 4

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]\n"

        self.assertEqual(output, expected)

        keyword = 'cANADa'
        advanced_option = 2
        advanced_response = 7

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755]]\n"

        self.assertEqual(output, expected)

        #empty keyword
        keyword = ''
        advanced_option = 2
        advanced_response = 700

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

        #keyword exists but max number of unique authors doesn't
        keyword = 'soccer'
        advanced_option = 2
        advanced_response = 0

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    
    # FUNCTION 3 INTEGRATION TEST
    @patch('builtins.input')
    def test_most_recent_article(self, input_mock):

        #article exists
        keyword = 'MuSIC'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Rock music', 'Mack Johnson', 1258069053, 119498]\n"

        self.assertEqual(output, expected)

        keyword = 'canaDA'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]\n"

        self.assertEqual(output, expected)

        #article does not exist
        keyword = 'messi'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

        self.assertEqual(output, expected)

        # empty keyword
        keyword = ''
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

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


    # ADVANCED OPTION 4: INTEGRATION TEST
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
    
    #ADVANCED OPTION 5: INTEGRATION TEST
    @patch('builtins.input')
    def test_advanced_option_5(self, input_mock):
        '''
        college provided as keyword for the advanced option 5
        '''
        
        keyword = 'college'
        advanced_option = 5
       
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [('Rock music', 'Mack Johnson'), ('Fisk University', 'RussBot')]\n"
        
        self.assertEqual(output, expected)

        '''
        man provided as keyword for the advanced option 5
        '''
        
        keyword = 'man'
        advanced_option = 5
       
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [('Black dog (ghost)', 'Pegship'), ('List of dystopian music, TV programs, and games', 'Bearcat')]\n"
        
        self.assertEqual(output, expected)
    
    #ADVANCED OPTION 6: INTEGRATION TEST
    @patch('builtins.input')
    def test_refine_search_test(self, input_mock):
        '''
        college provided as keyword and advanced_respose "fisk"
        '''
        
        keyword = 'college'
        advanced_option = 6
        advanced_response = 'fisk'
       
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Fisk University', 'RussBot', 1263393671, 16246]]\n"
        
        self.assertEqual(output, expected)
        
        '''
        music provided as keyword and advanced_response "lee"
        '''
        
        keyword = 'music'
        advanced_option = 6
        advanced_response = 'lee'
       
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023]]\n"
        
        self.assertEqual(output, expected)





# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
