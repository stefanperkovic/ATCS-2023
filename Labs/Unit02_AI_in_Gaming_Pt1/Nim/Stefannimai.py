"""
File to be modified by the students
The student should rename the file to 
be yourname_nimai.py.
"""

def ai_take_turn(piles):
    num_piles = 4
    for pile in piles:
        if pile == 0:
            num_piles += -1
    
    if num_piles % 2 == 0:
        if piles[1] > 0:
            return (1, piles[1])
        elif piles[2] > 1:
            return (2, piles[2] - 1)
        elif piles[3] > 1:
            return (3, piles[3] - 1)
        else:
            if piles[2] > 0:
                return (2, piles[2])
            elif piles[3] > 1:
                return (3, piles[3])

    else:
        
        if piles[0] > 0:
            return (0, 1)
        elif piles[1] > 0:
            return (1, piles[1])
        elif piles[2] > 0:
            return (2, piles[2])
        elif piles[3] > 0:
            return (3, piles[3])





            



    




    # TODO: Complete function
    pass





