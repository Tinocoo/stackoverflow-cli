import time
from app import Stackoverflow


if __name__ == "__main__":
    stack = Stackoverflow()
    search = input("Enter the search criteria : ") 
    
    result = stack.searchDiscussion(search)

    for question in result['data']['items']:
        print('\n\n---------------------------------------------\n')
        print('Title: {}'.format(question['title']))
        print('Score: {}'.format(question['score']))
        print('Is Answered: {}'.format(question['is_answered']))
        print('Link: {}'.format(question['link']))
        time.sleep(1)

    print('---------------------------------------------\n\n')
