import random


class GenerateMaze():

    # widthとheightは共に奇数かつ5以上の整数
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [list('#'*width) for _ in range(height)]
        self._dig_walls()

    def _search_directions(self, y , x):
        directions = []
        if x - 2 > 0 and self.maze[y][x-2] == '#':
            directions.append('L')
        if x + 2 < self.width and self.maze[y][x+2] == '#':
            directions.append('R')
        if y - 2 > 0 and self.maze[y-2][x] == '#':
            directions.append('U')
        if y + 2 < self.height and self.maze[y+2][x] == '#':
            directions.append('D')
        return directions

    def _dig_walls(self):
        start_y = random.choice([i for i in range(1, self.height, 2)])
        start_x = random.choice([i for i in range(1, self.width, 2)])
        self.maze[start_y][start_x] = ' '
        stack = [(start_y, start_x)]
        while stack:
            y, x = stack[-1]
            directions = self._search_directions(y, x)
            if directions == []:
                stack.pop()
                continue

            choiced = random.choice(directions)
            if choiced == 'L':
                for i in range(1, 3):
                    self.maze[y][x-i] = ' '
                x -= i
            elif choiced == 'R':
                for i in range(1, 3):
                    self.maze[y][x+i] = ' '
                x += i
            elif choiced == 'U':
                for i in range(1, 3):
                    self.maze[y-i][x] = ' '
                y -= i
            elif choiced == 'D':
                for i in range(1, 3):
                    self.maze[y+i][x] = ' '
                y += i
            stack.append((y, x))

    def print_maze(self, print_width=2):
        for line in self.maze:
            for char in line:
                print(char.center(print_width), end='')
            print()

    # SとGをself.mazeに書き込み
    def preset_start_goal(self):
        self.start = (self.height-2, 0)
        self.maze[self.height-2][0] = 'S'
        self.goal = (1, self.width-1)
        self.maze[1][self.width-1] = 'G'

    def regenerate(self):
        self.maze = [list('#'*self.width) for _ in range(self.height)]
        self._dig_walls()


if __name__ == '__main__':

    def check_value(user):
        if user < 5 or user % 2 == 0:
            return False
        else:
            return True

    while True:
        print('迷路を出力します')
        print('幅と高さが5以上の奇数を入力')
        try:
            width = int(input('Width = '))
            height = int(input('Height = '))
        except ValueError:
            print('有効な数字を入力して下さい\n')
            continue

        if all([check_value(width), check_value(height)]):
            break

    maze = GenerateMaze(width, height)
    maze.preset_start_goal()
    maze.print_maze()
    #酒を探して