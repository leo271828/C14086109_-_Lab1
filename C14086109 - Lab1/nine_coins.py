import random
class Nine_Coins:
    def __init__(self, num):
        ''' num is the decimal value '''
        self.num = num
        self.coins = bin(self.num)[2:].zfill(9)
#         self.coins imply that turn decimal to binary
#         ex: 
#             7  -> 000000111
#             95 -> 001011111 
    
    def __str__(self):
        return f'binary: {self.coins} and decimal: {self.num}'
    
    def __repr__(self):
        coins_str = ''
#         Here are turn binary to alpha
#         ex: 
#             000000111 -> HHHHHHTTT 
#             001011111 -> HHTHTTTTT 
        for idx in self.coins:
            if int(idx):
                coins_str += 'T'
            else :
                coins_str += 'H'
        return f'Nine_Coins: {coins_str} '
    
    def toss(self):
        new_coins = random.randint(0, 511)
        self.num = new_coins
        self.coins = bin(self.num)[2:].zfill(9)