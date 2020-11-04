"""
I want to learn some big words so people think I'm smart.
Write a Function for finding the index of the "rotation point"

"""


def frp(words):  # Find_Rotation_Point
    first_word = words[0]
    floor_idx = 0

    ceiling_idx = len(words) - 1

    while floor_idx < ceiling_idx:
        # Guess a index halfway between floor and ceiling
        guess_idx = floor_idx + ((ceiling_idx - floor_idx) // 2)

        # If guess comes after first word or is the first word

        if words[guess_idx] >= first_word:
            # move right
            floor_idx = guess_idx

        else:
            # Go left
            ceiling_idx = guess_idx

        # If floor and ceiling have converged
        if floor_idx + 1 == ceiling_idx:
            # Between foor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_idx




