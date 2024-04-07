from collections import defaultdict
class ChessBoard:
    def __init__(self) :
        self.board = [[None for col in range(8)] for row in range(8)]

class Piece:
    def __init__(self):
        self.pieces = defaultdict(list)
    def move(self,piece,dest):
        pass

class Player:
    def __init__(self,id,color):
        self.player_id = id
        self.color = color

p1 = Player("p1","white")
p2 = Player("p2","black")

