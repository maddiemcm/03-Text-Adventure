import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)




# Game loop functions
def render(game, current, moves): 
    ''' Display the current room, moves, and points '''
    r = game['rooms']
    c = r[current]
    print('\n\nMoves: {moves}'.format(moves=moves))
    print('\n\n{name}'.format(name=c['name']))
    print(c['desc'])
    return True

def checkInput():
    '''Asks the user for input and normalizes the inputted value.'''

    response = input('\nWhat would you like to do? ').strip().upper().split()
    return response

def update(response, game, current):
    '''Update our location, if possible, etc. '''
    s = list(response)[0] #assumes verb is the first thing typed
    if s == "":
        print("\nSorry, I don't understand. Try another command.")
    elif s == 'verbs':
        for v in game["rooms"][current]["exits"]:
            print(v["verb"])
        return current
    else:
        for e in game['rooms'][current]['exits']:
            if s == e['verb']:
                return e['target']
    print("\nYou can't do that. Try something else.")        
    return current


def main():
    game = {}
    with open('txtgame.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'START'
    quit = False
    moves = 0
    while not quit:
        #render
        render(game, current,moves)
        #check player input
        response = checkInput()
        #update
        current = update(response, game, current)
        moves = moves+1
    return True
# condition statements is so certain actions are made available with acquired inventory


#if we are running this from the command line, run main
if __name__ == '__main__':
	main()