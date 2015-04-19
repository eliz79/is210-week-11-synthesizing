#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A chess game """

import time


class ChessPiece(object):
    """Docstring.

    """
    prefix = ''

    def __init__(self, position):
        """Docstring.

        """
        if not ChessPiece.is_legal_move(self, position): #testing legal move
            excep = '{} is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Docstring.

        """
        x_axis = ('abcdefgh')
        y_axis = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(tile) > 2:
            return None
        else:
            if x_axis[0] and int(y_axis[1]) in tile:
                return (x_axis.find(x_axis[0]), (int(y_axis[1]) - 1))
            else:
                return None

    def is_legal_move(self, position):
        """Docstring.

        """
        newpos = self.algebraic_to_numeric
        if newpos(position):
            return True
        else:
            return False
        #if test not in ChessPiece.position():
            #excep = '{} is not a legal start position'
            #raise ValueError(excep.format(position))
            

    #def move(self, position):
        """Docstring.

        """
        #newpos = self.is_legal_move(position)
        #if newpos:
            #tup = (self.prefix + position, self.prefix + position, time.time()
            #return tup
        #else:
            #return False


        
