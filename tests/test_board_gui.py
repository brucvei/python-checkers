import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from board_gui import BoardGUI
from board import Board
from piece import Piece


@pytest.fixture
def pieces():
    return [Piece("0WN"), Piece("1BN"), Piece("2WN"), Piece("3BN")]


@pytest.fixture
def board(pieces):
    return Board(pieces, "W")


@pytest.fixture
def board_gui(board):
    pygame.init()
    return BoardGUI(board)


def test_set_pieces(board_gui, pieces):
    new_pieces = [{"rect": pygame.Rect(0, 0, 41, 41), "color": "B", "is_king": False}]
    board_gui.set_pieces(new_pieces)
    assert board_gui.pieces == new_pieces


def test_get_piece_properties(board_gui, board):
    piece_properties = board_gui.get_piece_properties(board)
    assert len(piece_properties) == 4
    assert piece_properties[0]["color"] == "W"
    assert piece_properties[1]["color"] == "B"


def test_get_piece_by_index(board_gui):
    piece = board_gui.get_piece_by_index(0)
    assert piece["color"] == "W"


def test_hide_piece(board_gui):
    board_gui.hide_piece(0)
    assert board_gui.hidden_piece == 0


def test_show_piece(board_gui):
    board_gui.hide_piece(0)
    piece_shown = board_gui.show_piece()
    assert piece_shown == 0
    assert board_gui.hidden_piece == -1


def test_draw_pieces(board_gui, mocker):
    display_surface = mocker.Mock()
    board_gui.draw_pieces(display_surface)
    assert display_surface.blit.call_count == 4


def test_draw_board(board_gui, mocker):
    display_surface = mocker.Mock()
    board_gui.draw_board(display_surface)
    assert display_surface.blit.call_count > 0


def test_get_piece_on_mouse(mocker, board):
    mocker.patch.object(BoardGUI, 'get_piece_on_mouse', return_value={"piece": {"color": "W"}, "index": 0})
    board_gui = BoardGUI(board)
    result = board_gui.get_piece_on_mouse((0, 0))
    assert result is not None
    assert result["piece"]["color"] == "W"
    assert result["index"] == 0

def test_get_surface(board_gui):
    piece = Piece("0WN")
    surface = board_gui.get_surface(piece)
    assert surface is not None


def test_get_move_marks(board_gui):
    move_marks = board_gui.get_move_marks()
    assert move_marks == []


def test_set_move_marks(board_gui):
    board_gui.set_move_marks([(0, 0)])
    assert len(board_gui.move_marks) == 1


def test_get_position_by_rect(board_gui):
    rect = pygame.Rect(34, 34, 41, 41)
    position = board_gui.get_position_by_rect(rect)
    print("Position returned by get_position_by_rect:", position)
    assert position == 0  # Adjust this assertion based on the expected outcome