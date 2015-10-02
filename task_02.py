#!/usr.bin/env python
#!-*- coding: utf-8-*-
"""Changes to be made to module."""


import data


BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Schmerman')

MYLIST = ('Don Quixote', 'Sylvia')
BALLETS.extend(MYLIST)

