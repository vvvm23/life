import os
import time
import numpy as np

class board:
    def __init__(self):
        self.width = 75
        self.height = 40
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]

    def update_state(self):
        updated_board = [[0 for x in range(self.width)] for y in range(self.height)]

        for y in range(0, self.height):
            for x in range(0, self.width):
                #print(self.board[y-1:y+1, x-1:x+1])
                num_adj_alive = 0
                for s_y in range(y-1, y+2):
                    for s_x in range(x-1, x+2):
                        if s_y >= 0 and s_y < self.height and s_x >= 0 and s_x < self.width:
                            #print(s_y, s_x)
                            if self.board[s_y][s_x] == 1 and not [s_y, s_x] == [y,x]:
                                num_adj_alive += 1

                #print(y,x,num_adj_alive)

                #print('')
                #if self.board[y][x] == 1:
                #    num_adj_alive -= 1

                #print(y, x, num_adj_alive)

                #print(y,x)
                if self.board[y][x] == 1:
                    if num_adj_alive < 2 or num_adj_alive > 3:
                        updated_board[y][x] = 0
                    elif num_adj_alive == 2 or num_adj_alive == 3:
                        updated_board[y][x] = 1
                elif self.board[y][x] == 0:
                    if num_adj_alive == 3:
                        updated_board[y][x] = 1
                    else:
                        updated_board[y][x] = 0

        self.board = updated_board
        return self.board

    def initialise_board(self, seed):
        self.board = seed

    def display_board(self, axes=False):
        os.system('clear')
        count = 0
        write_string = ""
        if axes:
            for column in self.board:
                write_string += "{0}   ".format(count)
                count += 1

            print(write_string)
            count = 0

        for row in self.board:
            write_string = ""
            if axes:
                write_string = str(count)

            for cell in row:
                if cell:
                    write_string += "■ "
                else:
                    write_string += "  "

            if axes:
                write_string += str(count)
                count += 1
            print(write_string)
b = board()

seed = np.random.randint(2, size=(40,75))

for y in range(2,3):
    for x in range(2,5):
        seed[y][x] = 1


b.initialise_board(seed)
nb_iterations = 1000
fps = 30

for i in range(nb_iterations):
    b.display_board()
    state = b.update_state()
    time.sleep(1/fps)

#################################################################################################################