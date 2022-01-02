#
#  https://adventofcode.com/2021/day/9
#  Advent of Code 2021
#
#  Created on 2021-12-08.
#

import heapq
import math
from collections import defaultdict, deque
from itertools import combinations, permutations
from typing import List, Set, Dict, Tuple, Optional


class Solution:
    def part1(self, board: List[List[int]]) -> int:
        points = []
        m = len(board)
        n = len(board[0])

        def lower(i, j, x, y) -> bool:
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            if board[i][j] < board[x][y]:
                return True
            return False

        for i in range(m):
            for j in range(n):
                if lower(i, j, i-1, j) and lower(i, j, i+1, j) and lower(i, j, i, j-1) and lower(i, j, i, j+1):
                    points.append(board[i][j])

        return sum(points) + len(points)

    def part2(self, board: List[List[int]]) -> int:
        res = 0
        points = []
        sizes = []
        m = len(board)
        n = len(board[0])

        def lower(i, j, x, y) -> bool:
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            if board[i][j] < board[x][y]:
                return True
            return False

        def bfs(i, j) -> int:
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            visited = set()
            size = 0
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                top = queue.popleft()
                size += 1
                for d in dirs:
                    x = top[0] + d[0]
                    y = top[1] + d[1]
                    if x >= 0 and x < m and y >= 0 and y < n and board[x][y] != 9 and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
            return size

        for i in range(m):
            for j in range(n):
                if lower(i, j, i-1, j) and lower(i, j, i+1, j) and lower(i, j, i, j-1) and lower(i, j, i, j+1):
                    points.append([i,j])

        for p in points:
            size = bfs(p[0], p[1])
            sizes.append(size)

        sizes.sort(reverse=True)
        res = sizes[0] * sizes[1] * sizes[2]
        return res

if __name__ == '__main__':
    s = Solution()
    board = []
    with open('09.txt') as f:
        lines = f.readlines()
        for line in lines:
            row = [int(c) for c in line.rstrip()]
            board.append(row)
    print(s.part2(board))
