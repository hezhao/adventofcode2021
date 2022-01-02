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
    def part1(self, fish: List[int], days: int) -> int:
        for d in range(days):
            n = len(fish)
            for i in range(n):
                if fish[i] > 0:
                    fish[i] -= 1
                else:
                    fish[i] = 6
                    fish.append(8)

        return len(fish)

    def part2(self, fish: List[int], days: int) -> int:
        fishmap = [0] * 9
        for f in fish:
            fishmap[f] += 1

        for d in range(days):
            fishmap_new = fishmap[1:] + [fishmap[0]]
            fishmap_new[6] += fishmap[0]
            fishmap = fishmap_new.copy()

        return sum(fishmap)

if __name__ == '__main__':
    s = Solution()
    days = 256
    with open('06.txt') as f:
        fish = [int(a) for a in f.readline().rstrip().split(',')]
    print(s.part2(fish, days))
