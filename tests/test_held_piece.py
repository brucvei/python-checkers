import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from held_piece import HeldPiece


@pytest.fixture
def surface():
    return pygame.Surface((50, 50))


@pytest.fixture
def offset():
    return (10, 10)


@pytest.fixture
def held_piece():
    surface = pygame.Surface((50, 50))
    return HeldPiece(surface, (10, 10))



def test_draw_piece(held_piece, mocker):
    display_surface = mocker.Mock()
    held_piece.draw_piece(display_surface)
    assert held_piece.draw_rect.topleft == (10, 10)


def test_check_collision(held_piece):
    rect_list = [pygame.Rect(110, 110, 50, 50), pygame.Rect(200, 200, 50, 50)]
    held_piece.draw_rect.topleft = (110, 110)
    assert held_piece.check_collision(rect_list) == rect_list[0]
    held_piece.draw_rect.topleft = (200, 200)
    assert held_piece.check_collision(rect_list) == rect_list[1]
    held_piece.draw_rect.topleft = (300, 300)
    assert held_piece.check_collision(rect_list) is None
