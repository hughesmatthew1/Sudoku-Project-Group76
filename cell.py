class Cell:
    def __int__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketch_value(self, value):
        pass

    def draw(self):
        pass