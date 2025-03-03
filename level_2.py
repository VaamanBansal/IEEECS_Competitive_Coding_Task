from sortedcontainers import SortedList
class Interval:
    def __init__(self):
        self.intervals = SortedList()
    def add_interval(self, a, b):
        self.intervals.add([a, b])
        m = SortedList()
        for i in self.intervals:
            if not m or m[-1][1] < i[0]:
                m.add(i)
            else:
                m[-1][1] = max(m[-1][1], i[1])
        self.intervals = m
    def get_interval(self):
        print(list(self.intervals))
I1 = Interval()
I1.add_interval(1, 5)
I1.add_interval(7, 10)
I1.add_interval(2, 9)
I1.get_interval()
