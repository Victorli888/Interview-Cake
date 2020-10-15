"""
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're
using an algorithm that sorts in O(n lg(n) ) time, but players are complaining that their rankings aren't updated
fast enough. You need a faster sorting algorithm.

Task:
1. Takes a list of unsorted scores & the highest possible score in a game and returns a sorted list.
2. The sorted list should be faster than O(n lg(n) )
"""
import unittest

def super_sort(unsorted, hps):  # unsorted scores, highest possible score

    score_count = [0] * (hps + 1)

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


class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = super_sort([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = super_sort([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = super_sort([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = super_sort([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = super_sort([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

