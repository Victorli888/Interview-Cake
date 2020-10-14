"""
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're
using an algorithm that sorts in O(n lg(n) ) time, but players are complaining that their rankings aren't updated
fast enough. You need a faster sorting algorithm.

Task:
1. Takes a list of unsorted scores & the highest possible score in a game and returns a sorted list.
2. The sorted list should be faster than O(n lg(n) )
"""


def super_sort(unsorted, hps):  # unsorted scores, highest possible score

    score_count = [0] + (hps + 1)

    # Populate score_counts
    for score in unsorted:
        score_count[score] += 1

    # Populate Final Scores in a sorted list
    sorted_scores = []

    # For each item in score
    for score in range(len(score_count) - 1, -1, -1):
        count = score_count[score]

        # For the number of times the item occurs
        for time in range(count):
            # add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores
