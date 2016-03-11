#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import sys


class Bowling():

    def __init__(self, original_frame_list):
        self.frame_list = self.set_frame_list(original_frame_list)
        self.score = 0

    @staticmethod
    def set_frame_list(score_list):
        frame_list = list()

        for score_pair in score_list:
            for score in score_pair:
                frame_list.append(int(score))

        return frame_list

    def cal_score(self):
        score = 0
        current_frame = 0
        score_list = list()

        for count in xrange(10):
            if self.is_strike(current_frame):
                score += self.strike_score(current_frame)
                current_frame += 1
            elif self.is_spare(current_frame):
                score += self.spare_score(current_frame)
                current_frame += 2
            else:
                score += self.frame_score(current_frame)
                current_frame += 2

            score_list.append(score)

        self.score = score

        return score_list

    def is_strike(self, current_frame):

        return self.frame_list[current_frame] == 10

    def is_spare(self, current_frame):

        return self.frame_list[current_frame] + self.frame_list[current_frame + 1] == 10

    def strike_score(self, current_frame):

        return 10 + self.frame_list[current_frame + 1] + self.frame_list[current_frame + 2]

    def spare_score(self, current_frame):

        return 10 + self.frame_list[current_frame + 2]

    def frame_score(self, current_frame):

        return self.frame_list[current_frame] + self.frame_list[current_frame + 1]


def main():

    start_time = time.time()

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        original_frame_list = [i.split(',') for i in test.strip().split(';')]

        print "original_frame_list", original_frame_list

        bowling_game = Bowling(original_frame_list)

        print "score_list", bowling_game.cal_score()

        print

    test_cases.close()

    print "Run time...{} secs \n".format(round(time.time() - start_time, 4))


if __name__ == '__main__':
    main()