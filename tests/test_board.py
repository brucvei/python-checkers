import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from board import Board
from piece import Piece


@pytest.fixture
def pieces():
    return [Piece("0WN"), Piece("1BN"), Piece("2WN"), Piece("3BN")]


@pytest.fixture
def board(pieces):
    return Board(pieces, "W")


def test_get_color_up(board):
    assert board.get_color_up() == "W"


def test_get_pieces(board, pieces):
    assert board.get_pieces() == pieces


def test_get_piece_by_index(board, pieces):
    assert board.get_piece_by_index(0) == pieces[0]
    assert board.get_piece_by_index(1) == pieces[1]


def test_has_piece(board):
    assert board.has_piece(0) is True
    assert board.has_piece(4) is False


def test_get_row_number(board):
    assert board.get_row_number(0) == 0
    assert board.get_row_number(5) == 1


def test_get_col_number(board):
    assert board.get_col_number(0) == 0
    assert board.get_col_number(5) == 3


def test_get_row(board):
    row = board.get_row(0)
    expected_positions = {"0", "1", "2", "3"}
    row_positions = {piece.get_position() for piece in row}

    assert row_positions == expected_positions


def test_get_pieces_by_coords(board, pieces):
    # Adjust the expected pieces based on the actual pieces at the given coordinates
    expected_pieces = [pieces[0], None]  # Assuming pieces[0] is at (0, 0) and no piece at (1, 3)
    assert board.get_pieces_by_coords((0, 0), (1, 3)) == expected_pieces


def test_move_piece(board, pieces):
    board.move_piece(0, 5)
    assert pieces[0].get_position() == "5"


def test_get_winner(board):
    assert board.get_winner() is None
    board.pieces = [Piece("0WN"), Piece("1WN")]
    assert board.get_winner() == "W"
