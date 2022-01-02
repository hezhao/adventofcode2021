#
#  https://adventofcode.com/2021/day/5
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
    def part1(self, points: List[List[List[int]]]) -> int:
        size = 1000
        grid = [[0] * size for _ in range(size)]
        res = 0

        for p in points:
            if p[0][0] == p[1][0]: # horizontal
                y = p[0][0]
                x1 = min(p[0][1], p[1][1])
                x2 = max(p[0][1], p[1][1])
                for x in range(x1, x2 + 1):
                    grid[x][y] += 1
            elif p[0][1] == p[1][1]: # vertical
                x = p[0][1]
                y1 = min(p[0][0], p[1][0])
                y2 = max(p[0][0], p[1][0])
                for y in range(y1, y2 + 1):
                    grid[x][y] += 1

        for x in range(size):
            for y in range(size):
                if grid[x][y] > 1:
                    res += 1
        return res

    def part2(self, points: List[List[List[int]]]) -> int:
        size = 1000
        grid = [[0] * size for _ in range(size)]
        res = 0

        for p in points:
            if p[0][0] == p[1][0]:  # horizontal
                y = p[0][0]
                x1 = min(p[0][1], p[1][1])
                x2 = max(p[0][1], p[1][1])
                for x in range(x1, x2 + 1):
                    grid[x][y] += 1
            elif p[0][1] == p[1][1]:  # vertical
                x = p[0][1]
                y1 = min(p[0][0], p[1][0])
                y2 = max(p[0][0], p[1][0])
                for y in range(y1, y2 + 1):
                    grid[x][y] += 1
            elif p[0][0]+p[0][1] == p[1][0]+p[1][1]: # bottom-left to top-right
                p.sort()
                x1 = p[0][0]
                x2 = p[-1][0]
                y = p[0][1]
                for i in range(x2 - x1 + 1):
                    grid[y - i][x1 + i] += 1
            elif abs(p[0][0]-p[1][0]) == abs(p[0][1]-p[1][1]): # top-left to bottom-right
                p.sort()
                x1 = p[0][0]
                x2 = p[-1][0]
                y = p[0][1]
                for i in range(x2 - x1 + 1):
                    grid[y + i][x1 + i] += 1

        for x in range(size):
            for y in range(size):
                if grid[x][y] > 1:
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    points = []
    with open('05.txt') as f:
        for line in f:
            l = line.rstrip().split('->')
            p1 = [int(cord) for cord in l[0].split(',')]
            p2 = [int(cord) for cord in l[1].split(',')]
            if p1[0] == p2[0] or p1[1] == p2[1] or p1[0]+p1[1] == p2[0]+p2[1] or abs(p1[0]-p2[0]) == abs(p1[1]-p2[1]):
                points.append([p1, p2])
    print(s.part2(points))
