class Interval:
    def __init__(self):
        self.intervals=[]
    def add_interval(self,a,b):
        self.intervals.append([a, b])
        self.intervals.sort()
        m= []
        for i in self.intervals:
            if not m or m[-1][1] < i[0]:
                m.append(i) 
            else:
                m[-1][1] = max(m[-1][1], i[1])
        self.intervals = m
    def get_interval(self):
        print(self.intervals)
