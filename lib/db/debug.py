import ipdb
from models import session, Puzzle, Choice, Outcome

print('You walk into a cave you found, and run into a bunker.')
print('\n Press c to continue or x to leave the bunker')

user_input = 'not x'
puzzle_id = 1

while user_input != 'x':
    user_input = input('=>')
    if user_input == 'c':
        current_puzzle = session.query(Puzzle).filter_by(id = puzzle_id).first()
        user_input = input(current_puzzle.question)
        options = session.query(Choice).filter(Choice.puzzle_id == puzzle_id).all()
        if user_input == '1':
            print(f'{options[1].outcome.name}')
            puzzle_id = options[1].outcome.puzzle_id
        elif user_input == '2':
            print(f'{options[0].outcome.name}')
            puzzle_id = options[0].outcome.puzzle_id
        else:
            print(f'{user_input} is not a 1 or 2')
    elif user_input != 'x':
        print(f'{user_input} not an allowed key')

print('Thanks for playing!')

ipdb.set_trace()