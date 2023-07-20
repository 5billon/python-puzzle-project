import ipdb
from models import session, Puzzle, Choice, Outcome


print('press x to exit at any point. Type "Help" to see list of available commands')
print('You walk into a cave you found, and run into a bunker.')

user_input = 'not x'
puzzle_id = 1
outcome_id = 1
check = False
while user_input != 'x' and outcome_id != 11:
    # if user_input == '':
        # for puzzle in session.query(Puzzle).filter_by(id = 1):
    current_puzzle = session.query(Puzzle).filter_by(id = puzzle_id).first()
    user_input=input(current_puzzle.question)
    # for outcome in session.query(Outcome).filter_by(puzzle_id = 1):
    options = session.query(Choice).filter(Choice.puzzle_id == puzzle_id).all()
    for option in options:
        check = False
        if user_input == option.answer:
            print(f'{option.outcome.name}')
            puzzle_id = option.outcome.puzzle_id
            outcome_id = option.outcome.id
            check = True
            
        # elif user_input == '2':
        #     print(f'{options[0].outcome.name}')
        #     puzzle_id = options[0].outcome.puzzle_id
        elif user_input == 'x':
            break
        elif user_input == 'Help':
            break
    if user_input == 'Help':
        print(f'your choices are "x" to exit')
        for option in options:
            print(f'"{option.answer}"')
    elif check == False:
        print(f'{user_input} is not an acceptable choice, type "Help" for options')
    
        # else:
        #     print(f'{user_input} is not "1" or "2"')
    # elif user_input != 'x':
    #     print(f'{user_input} not an allowed key')

print('Thanks for playing!')

ipdb.set_trace()