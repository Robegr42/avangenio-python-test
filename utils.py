"""
Auxiliar module to handle processes
"""
import random
import string
from typing import Tuple

async def check_text(data:str) -> Tuple[bool, int]:
    temp_data = data.lower() + "#"
    nums, spaces = 0,0
    for i in range(0, len(data)):
        if temp_data[i] == temp_data[i+1] == "a":
            return True, 1000
        if temp_data[i].isdigit():
            nums += 1
        if temp_data[i].isspace():
            spaces += 1
    letters = len(data) - nums - spaces
    metric = (letters*1.5 + nums*2)/spaces
    return False, metric

def generate_text(length:int = 10**6, min_spaces:int=3, max_spaces:int=5) -> str:
    spaces = random.randint(min_spaces, max_spaces)

    # Creating the pool of valid characters
    char_pool = string.ascii_letters + string.digits # a-z, A-Z, 0-9
    temp_text = ''.join(random.choice(char_pool) for i in range(length - spaces))

    # Inserting spaces randomly
    spaces_pos = random.sample(range(1, length-spaces), spaces)

    # Adding spaces to the text
    text = ""
    index = 0
    for i in range(spaces):
        text += temp_text[index:spaces_pos[i]] + " "
        index = spaces_pos[i]

    text += temp_text[index:]

    return text