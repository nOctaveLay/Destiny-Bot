import random

__all__ = ['roll_dice']


def roll_dice(num:int = 6):
    """
    주사위 눈을 뽑아주는 함수이다.
    Args:
        num : 주사위 눈금.

    Return:
        the random value of dice (int)

    """
    return random.choice([x+1 for x in range(num)])
