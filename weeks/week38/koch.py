# -*- coding: utf-8 -*-
import turtle

def koch(n, size):
    """Funktion der tegner koch-kurven. n er antallet af iterationer, og size er størrelsen"""
    if n == 1:
        turtle.forward(size)
    else:
        koch(n-1, size/3.0)
        turtle.left(60)
        koch(n-1, size/3.0)
        turtle.right(120)
        koch(n-1, size/3.0)
        turtle.left(60)
        koch(n-1, size/3.0)
        
