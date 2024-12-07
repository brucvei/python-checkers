import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import get_position_with_row_col, get_piece_position, get_piece_gui_coords, get_surface_mouse_offset


def test_get_position_with_row_col():
    assert get_position_with_row_col(0, 0) == 0
    assert get_position_with_row_col(1, 0) == 4
    assert get_position_with_row_col(2, 1) == 8
    assert get_position_with_row_col(3, 2) == 13

def test_get_piece_position():
    assert get_piece_position((100, 100), 50, (0, 0)) == 9
    assert get_piece_position((150, 150), 50, (0, 0)) == 13
    assert get_piece_position((200, 200), 50, (0, 0)) == 18
    assert get_piece_position((250, 250), 50, (0, 0)) == 22

def test_get_piece_gui_coords():
    assert get_piece_gui_coords((0, 0), 50, (0, 0)) == (0, 0)
    assert get_piece_gui_coords((1, 1), 50, (0, 0)) == (50, 50)
    assert get_piece_gui_coords((2, 2), 50, (0, 0)) == (100, 100)
    assert get_piece_gui_coords((3, 3), 50, (0, 0)) == (150, 150)

def test_get_surface_mouse_offset():
    assert get_surface_mouse_offset((100, 100), (50, 50)) == (50, 50)
    assert get_surface_mouse_offset((200, 200), (100, 100)) == (100, 100)
    assert get_surface_mouse_offset((300, 300), (150, 150)) == (150, 150)
    assert get_surface_mouse_offset((400, 400), (200, 200)) == (200, 200)
