#
#  https://adventofcode.com/2021/day/3
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
    def part1(self, nums: List[str]) -> int:
        n = len(nums)
        m = len(nums[0])
        gamma = ''
        epsilon = ''

        for i in range(m):
            ones = 0
            for j in range(n):
                if nums[j][i] == '1':
                    ones += 1
            if ones > n // 2:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
        return int(gamma, 2) * int(epsilon, 2)

    def part2(self, nums: List[str]) -> int:
        n = len(nums)
        m = len(nums[0])
        oxygen = 0
        co2 = 0

        s = set([i for i in range(n)])
        for i in range(m):
            ones = 0
            for j in s:
                if nums[j][i] == '1':
                    ones += 1
            if ones >= len(s) - ones:
                for j in list(s):
                    if nums[j][i] == '0':
                        s.remove(j)
            else:
                for j in list(s):
                    if nums[j][i] == '1':
                        s.remove(j)
            if len(s) == 1:
                oxygen = int(nums[s.pop()], 2)

        s = set([i for i in range(n)])
        for i in range(m):
            ones = 0
            for j in list(s):
                if nums[j][i] == '1':
                    ones += 1
            if ones >= len(s) - ones:
                for j in list(s):
                    if nums[j][i] == '1':
                        s.remove(j)
            else:
                for j in list(s):
                    if nums[j][i] == '0':
                        s.remove(j)
            if len(s) == 1:
                co2 = int(nums[s.pop()], 2)

        return oxygen * co2

if __name__ == '__main__':
    s = Solution()
    nums = []
    with open('03.txt') as f:
        for line in f:
            num = line.rstrip()
            nums.append(num)
    print(s.part2(nums))
