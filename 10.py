#
#  https://adventofcode.com/2021/day/10
#  Advent of Code 2021
#
#  Created on 2021-12-09.
#

import heapq
import math
from collections import defaultdict, deque
from itertools import combinations, permutations
from typing import List, Set, Dict, Tuple, Optional


class Solution:
    def part1(self, symbols: List[str]) -> int:
        res = 0

        for symbol in symbols:
            stack = []
            for c in symbol:
                if c == '[' or c == '(' or c == '{' or c == '<':
                    stack.append(c)
                else:
                    last = stack.pop()
                    if c == ')':
                        if last != '(':
                            res += 3
                    elif c == ']':
                        if last != '[':
                            res += 57
                    elif c == '}':
                        if last != '{':
                            res += 1197
                    elif c == '>':
                        if last != '<':
                            res += 25137

        return res

    def part2(self, symbols: List[str]) -> int:
        scores = []

        for symbol in symbols:
            stack = []
            score = 0
            for c in symbol:
                if c == '[' or c == '(' or c == '{' or c == '<':
                    stack.append(c)
                else:
                    last = stack.pop()
                    if c == ')':
                        if last != '(':
                            stack.clear()
                            break
                    elif c == ']':
                        if last != '[':
                            stack.clear()
                            break
                    elif c == '}':
                        if last != '{':
                            stack.clear()
                            break
                    elif c == '>':
                        if last != '<':
                            stack.clear()
                            break
            if stack:
                while stack:
                    c = stack.pop()
                    if c == '(':
                        score = score * 5 + 1
                    elif c == '[':
                        score = score * 5 + 2
                    elif c == '{':
                        score = score * 5 + 3
                    elif c == '<':
                        score = score * 5 + 4
                scores.append(score)

        scores.sort()
        res = scores[len(scores) // 2]

        return res

if __name__ == '__main__':
    s = Solution()
    symbols = []
    with open('10.txt') as f:
        lines = f.readlines()
        for line in lines:
            symbols.append(line.rstrip())
    print(s.part2(symbols))
