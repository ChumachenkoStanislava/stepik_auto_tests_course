
class MoneyBox:
    def init(self, capacity=0):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.capacity - self.coins >= v

    def add(self, v):
        self.coins += v

