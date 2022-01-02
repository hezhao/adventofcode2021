#
#  https://adventofcode.com/2021/day/7
#  Advent of Code 2021
#
#  Created on 2021-12-06.
#

import heapq
import math
from collections import defaultdict, deque
from itertools import combinations, permutations
from typing import List, Set, Dict, Tuple, Optional


class Solution:
    def part1(self, positions: List[int]) -> int:
        res = float('inf')
        left = min(positions)
        right = max(positions)

        for i in range(left, right + 1):
            fuel = 0
            for pos in positions:
                fuel += abs(pos - i)
            res = min(res, fuel)

        return res

    def part2(self, positions: List[int]) -> int:
        res = float('inf')
        left = min(positions)
        right = max(positions)

        for i in range(left, right + 1):
            fuel = 0
            for pos in positions:
                fuel += (1 + abs(pos - i)) * abs(pos - i) // 2
            res = min(res, fuel)

        return res

if __name__ == '__main__':
    s = Solution()
    with open('07.txt') as f:
        positions = [int(a) for a in f.readline().rstrip().split(',')]
    print(s.part2(positions))
