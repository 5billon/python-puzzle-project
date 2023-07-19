import ipdb
from models import session, Puzzle, Choice, Outcome

print('You walk into a cave you found, and run into a bunker.')
print('\n Press c to continue or x to leave the bunker')

user_input = 'not x'

while user_input != 'x':
    user_input = input('=>')
    if user_input == 'c':
        for puzzle in session.query(Puzzle).filter_by(id = 1):
            user_input=input(f'{puzzle.question}')
            for outcome in session.query(Outcome).filter_by(puzzle_id = 1):
                if user_input == 'Yes':
                    user_input=input(f'{outcome.name}')
                if user_input == 'No':
                    user_input=input(f'{outcome.name}')
                elif user_input != 'Yes':
                    print(f'{user_input} is not yes or no')
    elif user_input != 'x':
        print(f'{user_input} not an allowed key')

print('Thanks for playing!')

#ipdb.set_trace()