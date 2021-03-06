
# The Three Musketeers Game
import pickle
import random
import os
def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]
    

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    rows = ["A", "B", "C", "D", "E"]
    columns = [1, 2, 3, 4, 5]
    if s[0] not in rows or int(s[1]) not in columns:
        raise ValueError('String out ot the range')
    else:
        location = (ord(s[0]) - 65, int(s[1]) - 1)
        return location


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    range_tuples_location = list(range(5)) # list integers frorm 0 to 4
    if location[0] not in range_tuples_location or location[1] not in range_tuples_location:
        raise ValueError('Out of range')
    else:
        string_location = "".join((chr(location[0] + 65), str(location[1] + 1)))# convert tuple to string
        return string_location


def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]


def all_locations():
    """Returns a list of all 25 locations on the board."""
    list_tuple_locations = [(x, y) for x in list(range(0, 5))
                            for y in list(range(0, 5))]
    return list_tuple_locations


def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == "up":
        location = (row - 1, column)
        return location
    if direction == "down":
        location = (row + 1, column)
        return location
    if direction == "left":
        location = (row, column - 1)
        return location
    if direction == "right":
        location = (row, column + 1)
        return location


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    return at(location) == 'M' and is_within_board(location, direction) and at(
        adjacent_location(location, direction)) == 'R'

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    return at(location) == 'R' and is_within_board(location, direction) and at(
            adjacent_location(location, direction)) == '-'


def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location) == 'M':
        return is_legal_move_by_musketeer(location, direction)
    if at(location) == 'R':
        return is_legal_move_by_enemy(location, direction)


def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    if possible_moves_from: #checks if the list is not empty
        return True


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    if possible_moves_from:
        return True


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    possible_moves = []
    directions = ['up', 'down', 'left', 'right']
    for i in directions:
        if is_legal_move(location, i):
            possible_moves.append(i)
    return possible_moves


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    if 0 <= location[0] <= 4 and 0 <= location[1] <= 4:
        return True
    else:
        return False


def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    loc = adjacent_location(location, direction)
    if is_legal_location(loc):
        return True
    else:
        return False


def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    who = player
    all_possible_moves = []
    directions = ['up', 'down', 'left', 'right']
    for i in all_locations():
        for j in directions:
            if who == "M" and is_legal_move_by_musketeer(i, j) and at(i) != "-":
                all_possible_moves.append((i, j))
            else:
                if who == "R" and is_legal_move_by_enemy(i, j) and at(i) != "M":
                    all_possible_moves.append((i, j))
    return all_possible_moves


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    if at(location) == "M":
        new_location = adjacent_location(location, direction)
        board[new_location[0]][new_location[1]] = "M"
        board[location[0]][location[1]] = "-"
        return board
    if at(location) == "R":
        new_location = adjacent_location(location, direction)
        board[new_location[0]][new_location[1]] = "R"
        board[location[0]][location[1]] = "-"
        return board


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    choose_comp = all_possible_moves_for(who)[random.choice((0,len(all_possible_moves_for(who))-1))]
    return choose_comp



def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    three_musketeers = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == "M":
                three_musketeers.append((i, j))
    if three_musketeers[0][1] == three_musketeers[1][1] == three_musketeers[2][1]:
        return True
    if three_musketeers[0][0] == three_musketeers[1][0] == three_musketeers[2][0]:
        return True
    else:
        return False

#---------- Communicating with the user ----------


user_choice_save = 'R'
board_to_save = []
global quit
quit = False



def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    b = []
    c = []
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
            c.append(board[i][j])
        print()
        b.append(c)
        c = []
        ch = chr(ord(ch) + 1)
    global board_to_save
    board_to_save = b
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    global user_choice_save
    user_choice_save = user
    
    return user


def save_game(name):
    #save into two separate files users choice and board
    with open('save/'+name +".txt", "wb") as file:
        pickle.dump(board_to_save, file)
    with open('save/'+name, "wb") as file:
        pickle.dump(user_choice_save, file)

def load_game(name):
    
    board_file_name = 'save/'+ name +".txt"
    users_side_file_name = 'save/'+ name
    
    #save into two separate files users choice and board
    with open(board_file_name, "rb") as file:
        board = pickle.load(file)
    with open(users_side_file_name, "rb") as file:
        users_side = pickle.load(file)
    
    #when loaded the files will be deleted
    os.remove(board_file_name)
    os.remove(users_side_file_name)
    
    return users_side, board

def print_loaded_board(board):
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    b = []
    c = []
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
            c.append(board[i][j])
        print()
        b.append(c)
        c = []
        ch = chr(ord(ch) + 1)
    global board_to_save
    board_to_save = b
    print()

def get_files_load():
    """Function that return all the text files that can be loaded
    in the save folder"""
    path = os.getcwd()
    p = '\save'
    files = os.listdir(path + p)
    return files

def create_board_load(b):
    global board
    """Creates the board load and makes it globally
       available"""
    m = 'M'
    r = 'R'
    board = b
    return board
      

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    global quit
    if quit == True:
        move = input("Your move?: ").upper().replace(' ', '')
    else: 
        move = input("Your move? or if you want to save the game type Y: ").upper().replace(' ', '')
    if move == 'Y':
        name = input("Please choose a name to save your game: ").upper().replace(' ', '_')
        save_game(name)
        print('Game saved!')
        quit = True
        return get_users_move()
    elif (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',          location_to_string(location), 'to',          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    
    load = input("Hello! if you want to load an existing game type Y or type any keys to start a new game: \n").upper().replace(' ', '')

    if load == 'Y':

        files = get_files_load()
        if files == []:
            print('Sorry no file saved, Please type any keys below to start a new game')
            users_side = choose_users_side()
            board = create_board()
            print_instructions()
            print_board()
        else:
            print('Please choose a name of the file from the list below that you want to load\n')
            for i in range(len(files)):
                if files[i].endswith('.txt'):
                    print(files[i][:-4].lower().replace('_', ' '))
            name = input("Please type here the name of the game: ").upper().replace(' ', '_')     

            users_side, board = load_game(name)
            board = create_board_load(board)

            if users_side == 'M':
                print('\nYou are a Musketeer "M"')
            else: 
                print('You are Cardinal Richleau "R"')

            print_loaded_board(board)

    else:
        users_side = choose_users_side()
        board = create_board()
        print_instructions()
        print_board()

    #finish = True
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            print((board),'')
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break


if __name__ == "__main__":
    start()




