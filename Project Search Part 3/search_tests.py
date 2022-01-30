from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_title_to_info():
  fake_metadata_one = [['Donald', 'HarryP', 123450900, 240, ['all', 'the', 'right', 'moves', 'places']], ['McDonald', 'RonW', 98712349356, 4000, ['both', 'the', 'moves', 'can', 'do']]]
  expected_one = {'Donald': {'author': 'HarryP', 'timestamp': 123450900, 'length': 240}, 'McDonald': {'author': 'RonW', 'timestamp': 98712349356, 'length': 4000}}
  fake_metadata_two = [['Donald', 'Perry', 2343434, 2400, ['can', 'the', 'right', 'do']], ['McDonald', 'Dalglish', 98712349356, 4080, ['right', 'the', 'moves', 'can', 'do']]]
  expected_two = {'Donald': {'author': 'Perry', 'timestamp': 2343434, 'length': 2400}, 'McDonald': {'author': 'Dalglish', 'timestamp': 98712349356, 'length': 4080}}
  fake_metadata_three = [['Hurry', 'Kant', 2343434, 3030, ['what', 'if', 'he', 'did']], ['Up', 'Waddle', 74932356, 9400, ['the', 'right', 'thing']]]
  expected_three = {'Hurry': {'author': 'Kant', 'timestamp': 2343434, 'length': 3030}, 'Up': {'author': 'Waddle', 'timestamp': 74932356, 'length': 9400}}

  assert title_to_info(deepcopy(fake_metadata_one)) == expected_one
  assert title_to_info(deepcopy(fake_metadata_two)) == expected_two
  assert title_to_info(deepcopy(fake_metadata_three)) == expected_three

def test_keyword_to_titles():
  fake_metadata_one = [['Donald', 'HarryP', 123450900, 240, ['all', 'the', 'right', 'moves', 'places']], ['McDonald', 'RonW', 98712349356, 4000, ['both', 'the', 'moves', 'can', 'do']]]

  expected_one = {'all': ['Donald'], 'the': ['Donald', 'McDonald'], 'right': ['Donald'], 'moves': ['Donald', 'McDonald'], 'places': ['Donald'], 'both': ['McDonald'], 'can': ['McDonald'], 'do': ['McDonald']}

  fake_metadata_two = [['Donald', 'Perry', 2343434, 2400, ['can', 'the', 'right', 'do']], ['McDonald', 'Dalglish', 98712349356, 4080, ['right', 'the', 'moves', 'can', 'do']]]

  expected_two = {'can': ['Donald', 'McDonald'], 'the': ['Donald', 'McDonald'], 'right': ['Donald', 'McDonald'], 'do': ['Donald', 'McDonald'], 'moves': ['McDonald']}

  fake_metadata_three = [['Hurry', 'Kant', 2343434, 3030, ['what', 'if', 'he', 'did']], ['Up', 'Waddle', 74932356, 9400, ['the', 'right', 'thing']]]

  expected_three = {'what': ['Hurry'], 'if': ['Hurry'], 'he': ['Hurry'], 'did': ['Hurry'], 'the': ['Up'], 'right': ['Up'], 'thing': ['Up']}

  assert keyword_to_titles(deepcopy(fake_metadata_one)) == expected_one
  assert keyword_to_titles(deepcopy(fake_metadata_two)) == expected_two
  assert keyword_to_titles(deepcopy(fake_metadata_three)) == expected_three

def test_search():
  assert search('soccer') == SOCCER
  assert search('travel') == TRAVEL
  assert search('photo') == PHOTO

def test_article_info():
  expected_1 = {'Spain national beach soccer team': {'author': 'Pegship', 'timestamp': 1233458894, 'length': 1526}, 'Will Johnson (soccer)': {'author': 'Mayumashu', 'timestamp': 1218489712, 'length': 3562}, 'Steven Cohen (soccer)': {'author': 'Scouselad10', 'timestamp': 1237669593, 'length': 2117}}
  expected_2 = {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}
  expected_3 = {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
  assert article_info(deepcopy(SOCCER), TITLE_TO_INFO) == expected_1
  assert article_info(deepcopy(TRAVEL), TITLE_TO_INFO) == expected_2
  assert article_info(deepcopy(PHOTO), TITLE_TO_INFO) == expected_3

def test_article_length():
  expected_1 = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
  expected_2 = []
  expected_3 = ['Digital photography']
  assert article_length(15000, deepcopy(SOCCER), TITLE_TO_INFO) == expected_1
  assert article_length(4000, deepcopy(TRAVEL), TITLE_TO_INFO) == expected_2
  assert article_length(19000, deepcopy(PHOTO), TITLE_TO_INFO) == expected_3

def test_title_timestamp():
  expected_1 = {'Spain national beach soccer team': 1233458894, 'Will Johnson (soccer)': 1218489712, 'Steven Cohen (soccer)': 1237669593}
  expected_2 = {'Time travel': 1140826049}
  expected_3 = {'Digital photography': 1095727840}
  assert title_timestamp(deepcopy(SOCCER), TITLE_TO_INFO) == expected_1
  assert title_timestamp(deepcopy(TRAVEL), TITLE_TO_INFO) == expected_2
  assert title_timestamp(deepcopy(PHOTO), TITLE_TO_INFO) == expected_3

def test_favorite_author():
  assert favorite_author('Mayumashu', deepcopy(SOCCER), TITLE_TO_INFO) == True
  assert favorite_author('David', deepcopy(TRAVEL), TITLE_TO_INFO) == False
  assert favorite_author('Mintleaf', deepcopy(PHOTO), TITLE_TO_INFO) == True

def test_multiple_keywords():
  expected_1 = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Time travel']
  expected_2 = ['Time travel', 'Digital photography']
  expected_3 = ['Digital photography', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
  assert multiple_keywords('travel', deepcopy(SOCCER)) == expected_1
  assert multiple_keywords('photo', deepcopy(TRAVEL)) == expected_2
  assert multiple_keywords('soccer', deepcopy(PHOTO)) == expected_3

@patch('builtins.input')
def test_integration_tests(input_mock):
    keyword = 'soccer'
    advanced_option = 2
    advanced_response = 9000

    output_one = get_print(input_mock, [keyword, advanced_option, advanced_response])

    expected_one = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"
    assert output_one == expected_one

    keyword = 'travel'
    advanced_option = 3

    output_two = get_print(input_mock, [keyword, advanced_option, advanced_response])

    expected_two = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'Time travel': 1140826049}\n"
    assert output_two == expected_two

# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    test_title_to_info()
    test_keyword_to_titles()
    test_search()
    test_article_info()
    test_article_length()
    test_title_timestamp()
    test_favorite_author()
    test_multiple_keywords()
    test_integration_tests()

