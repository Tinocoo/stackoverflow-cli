import time
from .Stackoverflow import Stackoverflow


def create_app():
    stack = Stackoverflow()
    search = input("Enter the search criteria : ") 
    
    response_stackoverflow = stack.searchDiscussion(search)
    response_items = response_stackoverflow['data']['items']
    
    if len(response_items) == 0:
        print('your search returned no results')
    
    for question in response_items:
        if question['is_answered'] is True:
            response = 'Title: {}\n'.format(question['title'])
            response += 'Link: {}\n'.format(question['link'])
            response += 'Score: {}\n'.format(question['score'])

        print(response)
        time.sleep(1)