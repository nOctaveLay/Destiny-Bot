import random

__all__ = ['roll_dice']

def roll_dice(num:int = 6):
    return random.choice([x+1 for x in range(num)])
