import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from game_control import GameControl
from piece import Piece
from board import Board
from board_gui import BoardGUI
from held_piece import HeldPiece
from ai import AI


@pytest.fixture
def game_control():
    return GameControl(player_color="W", is_computer_opponent=True)


def test_get_turn(game_control):
    assert game_control.get_turn() == "W"


def test_get_winner(game_control):
    assert game_control.get_winner() is None


def test_setup(game_control):
    game_control.setup()
    assert isinstance(game_control.board, Board)
    assert isinstance(game_control.board_draw, BoardGUI)
    assert len(game_control.board.get_pieces()) == 24


def test_draw_screen(game_control, mocker):
    display_surface = mocker.Mock()
    game_control.draw_screen(display_surface)
    assert display_surface.blit.call_count > 0


def test_release_piece(game_control, mocker):
    mocker.patch.object(HeldPiece, 'check_collision', return_value=pygame.Rect(0, 0, 50, 50))
    mocker.patch.object(BoardGUI, 'show_piece', return_value=0)
    mocker.patch.object(Board, 'get_piece_by_index', return_value=Piece("0WN"))
    mocker.patch.object(Board, 'move_piece')
    mocker.patch.object(BoardGUI, 'set_pieces')
    mocker.patch.object(Board, 'get_winner', return_value=None)
    mocker.patch.object(Piece, 'get_moves', return_value=[])
    game_control.held_piece = HeldPiece(pygame.Surface((50, 50)), (0, 0))
    game_control.release_piece()
    assert game_control.held_piece is None


def test_set_held_piece(game_control, mocker):
    mocker.patch.object(BoardGUI, 'get_surface', return_value=pygame.Surface((50, 50)))
    mocker.patch('utils.get_surface_mouse_offset', return_value=(0, 0))
    game_control.set_held_piece(0, Piece("0WN"), (0, 0))
    assert isinstance(game_control.held_piece, HeldPiece)


def test_move_ai(game_control, mocker):
    mocker.patch.object(AI, 'get_move', return_value={"position_from": "0", "position_to": "1"})
    mocker.patch.object(Board, 'get_pieces', return_value=[Piece("0BN")])
    mocker.patch.object(Board, 'move_piece')
    mocker.patch.object(BoardGUI, 'set_pieces')
    mocker.patch.object(Board, 'get_winner', return_value=None)
    mocker.patch.object(Piece, 'get_moves', return_value=[])
    game_control.turn = "B"
    game_control.move_ai()
    assert game_control.turn == "W"
