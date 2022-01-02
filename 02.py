#
#  https://adventofcode.com/2021/day/2
#  Advent of Code 2021
#
#  Created on 2021-12-05.
#

import heapq
import math
from collections import defaultdict, deque
from itertools import combinations, permutations
from typing import List, Set, Dict, Tuple, Optional


class Solution:
    def part1(self, points: List[List[int]]) -> int:
        pos = [0, 0]
        for p in points:
            pos[0] += p[0]
            pos[1] += p[1]

        return pos[0] * pos[1]

    def part2(self, points: List[List[int]]) -> int:
        pos = [0, 0]
        aim = 0
        for p in points:
            if p[0] == 0: # forward
                pos[0] += aim * p[1]
                pos[1] += p[1]
            else: # aim
                aim += p[0]

        return pos[0] * pos[1]

if __name__ == '__main__':
    s = Solution()
    points = []
    with open('02.txt') as f:
        for line in f:
            p = line.rstrip().split()
            if p[0] == 'forward':
                points.append([0, int(p[1])])
            elif p[0] == 'down':
                points.append([int(p[1]), 0])
            elif p[0] == 'up':
                points.append([-int(p[1]), 0])
    print(s.part2(points))
