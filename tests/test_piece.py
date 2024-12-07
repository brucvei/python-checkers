import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from piece import Piece


def test_get_name():
    piece = Piece("16WN")
    assert piece.get_name() == "16WN"


def test_get_position():
    piece = Piece("16WN")
    assert piece.get_position() == "16"


def test_get_color():
    piece = Piece("16WN")
    assert piece.get_color() == "W"


def test_get_has_eaten():
    piece = Piece("16WN")
    assert piece.get_has_eaten() is False


def test_is_king():
    piece = Piece("16WN")
    assert piece.is_king() is False
    piece_king = Piece("16WY")
    assert piece_king.is_king() is True


def test_set_position():
    piece = Piece("16WN")
    piece.set_position(20)
    assert piece.get_position() == "20"


def test_set_is_king():
    piece = Piece("16WN")
    piece.set_is_king(True)
    assert piece.is_king() is True
    piece.set_is_king(False)
    assert piece.is_king() is False


def test_set_has_eaten():
    piece = Piece("16WN")
    piece.set_has_eaten(True)
    assert piece.get_has_eaten() is True
    piece.set_has_eaten(False)
    assert piece.get_has_eaten() is False


def test_get_adjacent_squares(mocker):
    piece = Piece("16WN")
    board = mocker.Mock()
    board.get_col_number.return_value = 1
    board.get_row_number.return_value = 1
    board.get_color_up.return_value = "W"
    board.get_pieces_by_coords.return_value = [None, None]
    assert piece.get_adjacent_squares(board) == [(0, 0), (0, 2)]


def test_get_moves(mocker):
    piece = Piece("16WN")
    board = mocker.Mock()
    board.get_col_number.return_value = 1
    board.get_row_number.return_value = 1
    board.get_color_up.return_value = "W"
    board.get_pieces_by_coords.return_value = [None, None]
    expected_moves = [{"position": "0", "eats_piece": False}, {"position": "1", "eats_piece": False}]
    assert piece.get_moves(board) == expected_moves