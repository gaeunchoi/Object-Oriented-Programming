from Block import *


class TetrisApp:
    level = 2
    score = 0
    is_game_over = False
    field = []      # grid
    height = 0
    width = 0
    screen_x = 120
    screen_y = 100
    zoom = 20

    block = None
    num_block_type = 7  # Number of block type

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.is_game_over = False

        # Set field (screen)
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def set_new_block(self):
        type = random.randint(0, self.num_block_type - 1)  # Set block type
        if type == 0:
            self.block = IBlock(3, 0)
        elif type == 1:
            self.block = ZBlock(3, 0)
        elif type == 2:
            self.block = SBlock(3, 0)
        elif type == 3:
            self.block = LBlock(3, 0)
        elif type == 4:
            self.block = JBlock(3, 0)
        elif type == 5:
            self.block = TBlock(3, 0)
        elif type == 6:
            self.block = OBlock(3, 0)

    def check_intersection(self):
        intersection = False
        # Write code here!

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.get_image():
                    # x grid 벗어난 경우
                    if self.block.x + j < 0 or self.block.x + j > 9 :
                        return True
                    # y grid 벗어난 경우
                    if self.block.y + i >= 20 :
                        return True
                    # 기존의 Block과 충돌하는 경우
                    if self.field[i + self.block.y][j + self.block.x] != 0 :
                        return True

        return intersection

    def delete_lines(self):
        lines = 0
        # Write code here!
        for i in range(self.height) :
            new_line = [0 for k in range(10)]
            if 0 not in self.field[i] :
                del(self.field[i])
                self.field.insert(0, new_line)
                lines += 1

        self.score += lines

    def move_straight_down(self):
        # Write code here!
        for k in range(self.block.y, self.height) :
            # move_down 코드지만 check_condition은 수행하지 않음.
            # 블럭과 충돌하거나 벽과 충돌할 때 까지 한줄씩 내려가기 수행
            self.block.y += 1
            if self.check_intersection():
                self.block.y -= 1
        self.check_condition()

    def move_down(self):
        self.block.y += 1
        if self.check_intersection():
            self.block.y -= 1
            self.check_condition()

    def check_condition(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.get_image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.idx_color
        self.delete_lines()
        self.set_new_block()
        if self.check_intersection():
            self.is_game_over = True

    def move_side(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.check_intersection():
            self.block.x = old_x

    def rotate(self):
        # Write code here!
        self.block.rotate();
        if self.check_intersection() :
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.block.get_image():
                        if self.block.x + j < 0 :
                            self.block.x += 1
                        if self.block.x + j > 9 :
                            self.block.x -= 1
                        if self.block.y + i >= 20 or self.field[i + self.block.y][j + self.block.x] != 0 :
                            self.block.y -= 1

        pass
