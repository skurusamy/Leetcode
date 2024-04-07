from collections import defaultdict
class Card:
    def __init__(self, c, token,color):
        self.card_id = c
        self.tokens = token
        self.color = color
class Players:
    def __init__(self,p,token) -> None:
        self.player_id = p
        self.p_tokens = token
        self.history = defaultdict(list)

class Game:
    def __init__(self) -> None:
        pass

    def updateStatus(self,c,p,status):
            p.history[c].append(status)
    def playGame(self, c, p):
        status = ""
        if "gold" in p.p_tokens.keys():
            gold_count = p.p_tokens["gold"]
        else:
            gold_count =0
        for clr in c.tokens.keys():
            if not clr in p.p_tokens.keys():
                if gold_count <= 0:
                    self.updateStatus(c.card_id,p,"Failed")
                    return False
                else:
                    if gold_count >= c.tokens[clr]:
                        pass
                    else:
                        self.updateStatus(c.card_id,p,"Failed")
                        return False
            else:   
                if p.p_tokens[clr] >= c.tokens[clr]:
                    pass
                else:
                    if gold_count >= c.tokens[clr]:
                        gold_count -= c.tokens[clr]
                    else:
                        self.updateStatus(c.card_id,p,"Failed")
                        return False

        for clr in c.tokens.keys():
            if clr in p.p_tokens and p.p_tokens[clr] >= c.tokens[clr]:
                p.p_tokens[clr] -= c.tokens[clr]  
            else:
                p.p_tokens["gold"] -= c.tokens[clr]             
        self.updateStatus(c.card_id,p,"Purchased")
        return True
    




c = Card('c1', {"white":2,"black":1,"blue":4},"GREEN")
p1 = Players('p1',{"white":2,"black":2,"blue":4})
p2 = Players('p2',{"white":2,"green":2,"blue":4,"gold":8})
g = Game()
print(c.tokens)
print(p2.p_tokens)
print(g.playGame(c,p2))
print(p2.p_tokens)
print(g.playGame(c,p2))
print(p2.p_tokens)
print(g.playGame(c,p2))
print(p2.p_tokens)


