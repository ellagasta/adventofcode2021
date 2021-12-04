import numpy as np

class Board:
    def __init__(self, input_list):
        self.matrix = np.array(input_list)
        self.called = np.zeros(self.matrix.shape)
        self.shape = self.matrix.shape
    def has_won(self):
        for x in range(self.shape[0]):
            if self.row_complete(x):
                return True
        for x in range(self.shape[1]):
            if self.column_complete(x):
                return True
        return False
    def call_number(self, num):
        for index, value in np.ndenumerate(self.matrix):
            if value == num:
                self.called[index] = True
                self.last_called = num
                if self.has_won():
                    break
    def row_complete(self, i):
        return all(self.called[i,:])
    def column_complete(self, i):
        return all(self.called[:,i])
    def score(self):
        last_called = int(self.last_called)
        sum_uncalled = 0
        for index, value in np.ndenumerate(self.called):
            if not value:
                sum_uncalled += int(self.matrix[index])

        return last_called * sum_uncalled




def find_winner(numbers, boards):
    for number in numbers:
        for board in boards:
            board.call_number(number)
            if board.has_won():
                return board

def find_loser(numbers, boards):
    for number in numbers:
        to_remove = []
        for i in range(len(boards)):
            board = boards[i]
            board.call_number(number)
            if board.has_won():
                loser = board
                to_remove.append(i)
        boards = [boards[i] for i in range(len(boards)) if i not in to_remove]
        if len(boards) == 0:
            break
    return loser



with open('input.txt') as f:
    input = f.readlines()

numbers = input.pop(0).rstrip().split(",")
input.pop(0)

boards = []

l = []
for line in input:
    if line.rstrip() == "":
        boards.append(Board(l))
        l = []
    else:
        x = line.rstrip().split()
        if x[0] == "":
            x.pop(0)
        l.append(x)

def q1():
    winner = find_winner(numbers,boards)
    print(winner.score())

def q2():
    loser = find_loser(numbers, boards)
    print(loser.score())


q2()