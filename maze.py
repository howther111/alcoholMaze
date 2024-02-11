import random
from PIL import Image, ImageDraw

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

    def draw_maze(self):
        x_max = 0
        x_max_sum = 0
        y_max = 0
        pix_size = 200
        for line in self.maze:
            for char in line:
                x_max_sum = x_max_sum + (pix_size ** 2)
            y_max = y_max + pix_size
        x_max = x_max_sum // y_max

        im = Image.new("RGB", (x_max, y_max), (255, 255, 255))

        #im.save("maze.png")
        wallImage = Image.open("mazewall.png")
        floorImage = Image.open("mazefloor.png")
        startImage = Image.open("mazefloorstart.png")
        goalImage = Image.open("mazefloorgoal.png")
        x_pos = 0
        y_pos = 0

        for line in self.maze:
            for char in line:
                if char == " ":
                    im.paste(floorImage, (x_pos, y_pos))
                elif char == "#":
                    im.paste(wallImage, (x_pos, y_pos))
                elif char == "S":
                    im.paste(startImage, (x_pos, y_pos))
                elif char == "G":
                    im.paste(goalImage, (x_pos, y_pos))
                x_pos = x_pos + pix_size
            y_pos = y_pos + pix_size
            x_pos = 0

        im.save("maze.png")

    def output_maze(self, print_width=1):
        ret = ""
        for line in self.maze:
            for char in line:
                ret = ret + char
            ret = ret + "\n"
        return ret

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
    mazetext = maze.output_maze()
    print(mazetext)
    maze.draw_maze()

    with open("maze.txt", "w", encoding="utf-8") as f:
        f.write(mazetext)
    #酒を探して