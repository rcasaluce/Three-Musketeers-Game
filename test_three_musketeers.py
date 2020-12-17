import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((0, 2)) == R
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    board2 = [[_, M, _, _, _],
              [_, _, R, M, _],
              [R, R, _, R, _],
              [_, R, M, _, _],
              [_, _, _, R, _]]
    set_board(board2)
    assert at((4, 3)) == R
    assert at((0, 2)) == _
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    board2 = [[_, M, _, _, _],
              [_, _, R, M, _],
              [R, R, _, R, _],
              [_, R, M, _, _],
              [_, _, _, R, _]]
    set_board(board2)
    assert board2 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError) as excinfo:
        string_to_location("X3")
    assert string_to_location('A1') == (0,0)
    with pytest.raises(ValueError) as excinfo:
        string_to_location("F3")
    with pytest.raises(TypeError) as excinfo:
        string_to_location(13)
    #eventually add at least one more exception test and two more
    #test with correct inputs


def test_location_to_string():
    with pytest.raises(ValueError) as excinfo:
        location_to_string((0,5))
    assert location_to_string((0, 0)) == "A1"
    assert location_to_string((4, 0)) == "E1"
    assert location_to_string((3, 1)) != "D1"
    with pytest.raises(TypeError) as excinfo:
        location_to_string(2)
    # Replace with tests


def test_at():
    set_board(board1)
    assert at((1, 4)) == board1[1][4]
    assert at((0, 0)) == board1[0][0]
    assert at((4, 0)) == board1[4][0]
    assert at((4, 4)) == board1[4][4]
    # Replace with tests


def test_all_locations():
    assert all_locations()[0] == (0,0)
    assert all_locations()[5] == (1,0)
    assert all_locations()[24] == (4, 4)
    # Replace with tests


def test_adjacent_location():
    assert adjacent_location((0, 0), "down") == (1, 0)
    assert adjacent_location((0, 2), "left") == (0, 1)
    assert adjacent_location((0, 1), "right") == (0, 2)
    assert adjacent_location((2, 4), "up") == (1, 4)
    assert adjacent_location((4, 3), "right") == (4, 4)
    # Replace with tests


def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((1, 3), "left") == True
    assert is_legal_move_by_musketeer((2, 2), "left") == True
    assert is_legal_move_by_musketeer((1, 3), "right") == False
    assert is_legal_move_by_musketeer((2, 1), "right") == False
    assert is_legal_move_by_musketeer((0, 1), "down") == False
    # Replace with tests


def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((2, 3), "right") == True
    assert is_legal_move_by_enemy((3, 1), "left") == True
    assert is_legal_move_by_enemy((2, 1), "down") == False
    assert is_legal_move_by_enemy((1, 2), "right") == False
    assert is_legal_move_by_enemy((3, 1), "up") == False
    # Replace with tests


def test_is_legal_move():
    assert is_legal_move((1, 2), "left") == True
    assert is_legal_move((3, 1), "down") == True
    assert is_legal_move((0, 3), "down") == False
    assert is_legal_move((2, 3), "up") == False
    assert is_legal_move((2, 3), "right") == True
    # Replace with tests


def test_can_move_piece_at():
    assert can_move_piece_at((2, 2)) == True
    assert can_move_piece_at((1, 3)) == True
    assert can_move_piece_at((2, 3)) == True
    assert can_move_piece_at((4, 4)) == True
    # Replace with tests


def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board


def test_possible_moves_from():
    #assert possible_moves_from((1, 0)) == []
    assert possible_moves_from((2, 1)) == ["up", "left"]
    assert possible_moves_from((3, 1)) == ["down", "left", "right"]
    assert possible_moves_from((4, 3)) == ["up", "left", "right"]
    # Replace with tests


def test_is_legal_location():
    assert is_legal_location((1, 0)) == True
    assert is_legal_location((5, 0)) == False
    assert is_legal_location((3, 4)) == True
    assert is_legal_location((-1, 0)) == False
    # Replace with tests


def test_is_within_board():
    assert is_within_board((0, 0), "down") == True
    assert is_within_board((0, 0), "up") == False
    assert is_within_board((4, 0), "left") == False
    assert is_within_board((4, 4), "left") == True
    # Replace with tests


def test_all_possible_moves_for():
    board1 =  [ [_, _, M, _, _],
                [_, _, R, M, _],
                [_, _, M, R, _],
                [_, _, _, _, _],
                [_, _, _, _, _] ]
    assert all_possible_moves_for("M") == [ ((1, 3), "down"),((1, 3), "left"),((2, 2), "up"),
                                           ((2,2), "left"),((2,2), "right")]
    #assert all_possible_moves_for("R") == []
    # Replace with tests


def test_make_move():
    board1 = [[_, _, _, M, _],
              [_, _, R, M, _],
              [_, R, M, R, _],
              [_, R, _, _, _],
              [_, _, _, R, _]]

    board_new = [[_, _, _, M, _],
                 [_, _, R, M, _],
                 [_, R, M, R, _],
                 [_, R, _, _, _],
                 [_, _, R, _, _]]
    assert make_move((4, 3), "left") == board_new
    board1 = [[_, _, _, M, _],
              [_, _, R, M, _],
              [_, R, M, R, _],
              [_, R, _, _, _],
              [_, _, R, _, _]]

    board_new = [[_, _, _, M, _],
                 [_, _, M, M, _],
                 [_, R, _, R, _],
                 [_, R, _, _, _],
                 [_, _, R, _, _]]
    assert make_move((2, 2), "up") == board_new
    # Replace with tests


def test_choose_computer_move():
    #assert choose_computer_move("M") == ()
    #assert choose_computer_move("R") == ()
    board5 = [[R, R, R, R, _],
              [R, R, R, R, M],
              [R, R, M, R, R],
              [R, R, R, R, R],
              [R, R, R, R, R]]
    set_board(board5)
    assert choose_computer_move("R") == ((0,3), "right")
    board8 = [[R, R, R, R, M],
              [R, R, R, R, R],
              [R, R, M, R, R],
              [M, R, R, R, R],
              [_, R, R, R, R]]
    set_board(board8)
    assert choose_computer_move("R") == ((4, 1), "left")
    # Replace with tests; should work for both 'M' and 'R'


def test_is_enemy_win():
    #assert is_enemy_win() == True
    set_board([[_, R, _, _, M],
               [_, _, _, _, M],
               [_, _, _, _, M],
               [_, _, _, _, _],
               [_, R, _, _, _]])
    assert is_enemy_win() == True

    board6 = [[_, R, _, _, M],
               [R, _, R, _, R],
               [_, R, _, _, M],
               [_, _, _, _, _],
               [_, M, _, _, _]]
    set_board(board6)
    assert is_enemy_win() == False
    board8 = [[_, R, _, _, R],
              [R, _, R, _, R],
              [_, R, _, _, _],
              [_, _, _, _, _],
              [_, M, _, M, M]]
    set_board(board8)
    assert is_enemy_win() == True
    # Replace with tests


