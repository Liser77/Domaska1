def go_up(self):
    self.y += self.s

def go_down(self):
    self.y -= self.s

def go_left(self):
    self.x -= self.s

def go_right(self):
    self.x += self.s

def evolve(self):
    self.s += 1

def degrade(self):
    if self.s <= 1:
        raise ValueError("s cannot be less than or equal to 0")
    self.s -= 1

def count_moves(self, x2, y2):
    diff_x = abs(self.x - x2)
    diff_y = abs(self.y - y2)
    total_moves = diff_x + diff_y
    return total_moves