import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai import AI
from board import Board
from piece import Piece


@pytest.fixture
def board():
    pieces = [Piece("0WN"), Piece("1BN"), Piece("2WN"), Piece("3BN")]
    return Board(pieces, "W")


@pytest.fixture
def ai():
    return AI("W")


def test_get_value(ai, board):
    print("Initial board value:", ai.get_value(board))
    assert ai.get_value(board) == 0

    # Move a piece to a new position
    piece = board.get_pieces()[1]
    piece.set_position("4")

    print("Board value after moving piece:", ai.get_value(board))
    assert ai.get_value(board) == 0


def test_minimax(ai, board, mocker):
    mocker.patch.object(Piece, 'get_moves', return_value=[{"position": "1", "eats_piece": False}])
    value = ai.minimax(board, True, 1, "W")
    print("Minimax value:", value)
    assert value == 1  # Adjust this value based on the expected outcome of the minimax function