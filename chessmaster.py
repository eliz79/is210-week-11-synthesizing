#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A chess game """

import time


class ChessPiece(object):
    """Moving piece in a game of chess."""
    prefix = ''

    def __init__(self, position):
        """Docstring.
        Args:
            position: an alphanumeric position on the board.
        Attribute:
            prefix: an empty string by default.
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '{} is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """A tile as a two value tuple used as position.
        Arg:
            tile: tuple consisting two value of the position on the board.
        """
        x_axis = 'abcdefgh'
        y_axis = [1, 2, 3, 4, 5, 6, 7, 8]
        if tile[0] in x_axis and int(tile[1]) in y_axis:
            return (x_axis.find(tile[0]), (int(tile[1]) - 1))
        else:
            return None

    def is_legal_move(self, position):
        """To test if new position is legal to move.
        Args:
            position: an allowed position on the board.
        Attribute:
            newpos: a new position on the board.
        """
        newpos = self.algebraic_to_numeric
        if newpos(position):
            return True
        else:
            return False

    def move(self, position):
        """Pieces to move.
        Args:
            position: an allowed position on the board.
        Attribute:
            newpos: a new position on the board.
        """
        newpos = self.is_legal_move(position)
        if newpos:
            tup = (self.prefix + self.position,
                   self.prefix + position, time.time())
            self.moves.append(tup)
            self.position = position
            return tup
        else:
            return False
