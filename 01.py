#
#  https://adventofcode.com/2021/day/1
#  Advent of Code 2021
#
#  Created on 2021-12-04.
#

import heapq
import math
from collections import defaultdict, deque
from itertools import combinations, permutations
from typing import List, Set, Dict, Tuple, Optional


class Solution:
    def part1(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                res += 1
        return res

    def part2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(3, n):
            if nums[i] > nums[i - 3]:
                res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    with open('01.txt') as f:
        nums = [int(line.rstrip()) for line in f]
        print(s.part2(nums))
