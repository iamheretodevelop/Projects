from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_titles() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
ARTICLE_TITLES = article_titles()

def test_example_unit_tests():
    # Storing into a variable so don't need to copy and paste long list every time
    # If you want to store search results into a variable like this, make sure you pass a copy of it when
    # calling a function, otherwise the original list (ie the one stored in your variable) is going to be
    # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
    dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
    
    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == dog_search_results

    # Advanced search option 1, function #2
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']

    assert title_length(25, dog_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(3, dog_search_results.copy()) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

    # Advanced search option 3, function #4
    assert random_article(3, dog_search_results.copy()) == 'Black dog (ghost)'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', dog_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', dog_search_results.copy()) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1
    advanced_response = 25

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Edogawa, Tokyo\', \'Kevin Cadogan\', \'Endogenous cannabinoid\', \'Black dog (ghost)\', \'2007 Bulldogs RLFC season\', \'Mexican dog-faced bat\', \'Dalmatian (dog)\', \'Guide dog\', \'Georgia Bulldogs football\', \'Endoglin\', \'Sun dog\', \'The Mandogs\', \'Landseer (dog)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_search():
  dogs_search_results = ['2007 Bulldogs RLFC season', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston']
  assert search('dogs') == dogs_search_results, "Incorrect search results."
  assert search('cat') == ['Voice classification in non-classical music'], "Incorrect search results."
  assert search('money') == [], "Incorrect search results."

def test_title_length():
  dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  expected_one = ['Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs']
  expected_two = ['Sun dog']
  expected_three = []
  assert title_length(11, dog_search_results.copy()) == expected_one, "The title length exceeds the limit."
  assert title_length(7, dog_search_results.copy()) == expected_two, "The title length exceeds the limit."
  assert title_length(5, dog_search_results.copy()) == expected_three, "There are no available articles for this length."

def test_article_count():
  dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  expected_one = []
  expected_two = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season']
  expected_three = []
  assert article_count(50, dog_search_results.copy()) == expected_one, "Not enough articles."
  assert article_count(5, dog_search_results.copy()) == expected_two, "Article count exceeds the requirement"
  assert article_count(0, dog_search_results.copy()) == expected_three, "No articles were asked."

def test_random_article():
  dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  expected_one = 'Mexican dog-faced bat'
  expected_two = ''
  expected_three = 'Sun dog'
  assert random_article(5, dog_search_results.copy()) == expected_one, "The expected article title is Mexican dog-faced bat."
  assert random_article(19, dog_search_results.copy()) == expected_two, "Given index absent in the list."
  assert random_article(11, dog_search_results.copy()) == expected_three, "The expected article title is Sun dog."

def test_favorite_article():
  dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  assert favorite_article('Kevin Cadogan', dog_search_results.copy()) == True, "It is present in the list"
  assert favorite_article('German Shepherd', dog_search_results.copy()) == False, "It is not present in the list"
  assert favorite_article('Guide dog', dog_search_results.copy()) == True, "It is present in the list"

def test_multiple_keywords():
  dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  cat_search_results = ['Voice classification in non-classical music']
  expected_one = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Digital photography', 'Wildlife photography']
  expected_two = ['Voice classification in non-classical music', 'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
  assert multiple_keywords('photography', dog_search_results.copy()) == expected_one, "Incorrect list output"
  assert multiple_keywords('dog', cat_search_results) == expected_two, "Incorrect list output"
  assert multiple_keywords('money', dog_search_results.copy()) == dog_search_results.copy(), "Incorrect list output"

@patch('builtins.input')
def test_integration_test(input_mock):
    keyword = 'photo'
    advanced_option = 3
    advanced_response = 1

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: Wildlife photography\n'

    assert output == expected, "Unexpected program layout."

# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()
    test_search()
    test_title_length()
    test_article_count()
    test_random_article()
    test_favorite_article()
    test_multiple_keywords()
    test_integration_test()
    
