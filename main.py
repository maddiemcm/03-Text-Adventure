import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)




# Game loop functions
def render(game, current): 
    ''' Display the current room, moves, and points '''
    r = game['rooms']
    c = r[current]

    print('\n\nYou are in the {name}'.format(name=c['name']))
    print(c['desc'])
        # the render is figuring out where the person is by going from the rooms within the game (r = game ['rooms']), to current location to name and then itll say the description. Current is a variable but name and room are strings. 
    return True

def checkInput():
    '''Asks the user for input and normalizes the inputted value.'''

    response = input('\nWhat would you like to do? ').strip().upper()
    return response

def update(response, game, current):
    '''Update our location, if possible, etc. '''
    #verbs are north, south, east, west
    #targets are the location you are targetting 
    #exits represent transition between rooms based on verbs/input
    for e in game['rooms'][current]['exits']:
        if e['verb'] == response:
            current = e['target']        
    return current


def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'
            # WHOUS is the location in the game where we start
    quit = False
    while not quit:
        #render
        render(game, current)
        #check player input
        response = checkInput()
        #update
        current = update(response, game, current)
        
    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()