import math
import random
import statistics


class Num:

    def __init__(self, col_position, col_name, nums):
        self.items_seen = 0
        self.col_pos = col_position or 0
        self.col_name = col_name or ""
        self.max_nums = nums or 512
        self.numbers = {}
        self.lo = math.inf
        self.hi = -math.inf
        self.is_sorted = True

    def nums(self):
        if not self.is_sorted:
            self.numbers = dict(sorted(self.numbers.items()))

    def add(self, v):
        pos = -1
        if v != "?":
            self.items_seen = self.items_seen + 1
            if self.lo > v:
                self.lo = v
            if self.hi < v:
                self.hi = v
            if len(self.numbers) < self.max_nums:
                pos = len(self.numbers)
            else:
                rand = random.randint(0, self.items_seen)
                if rand < self.max_nums - 1:
                    pos = rand
            if pos != -1:
                self.numbers[pos] = v
                self.is_sorted = False
                return pos

    def dev(self):
        return statistics.median(self.numbers)

    def mid(self):
        return statistics.median(self.numbers)
