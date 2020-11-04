class TaTeTi():

    def __init__(self, board={
            "1.1": "1.1",
            "1.2": "1.2",
            "1.3": "1.3",
            "2.1": "2.1",
            "2.2": "2.2",
            "2.3": "2.3",
            "3.1": "3.1",
            "3.2": "3.2",
            "3.3": "3.3",
        }, valid=['1.1', '1.2', '1.3',
                  '2.1', '2.2', '2.3',
                  '3.1', '3.2', '3.3'], piece='x'):
        self._board = board
        self._valid = valid
        self._piece = piece

    def __str__(self):
        result = ''
        i = 0
        for value in self.board:
            result += self.board[value]
            if(i == 2 or i == 5):
                result += '\n---+---+---\n'
            elif(i != 8):
                result += "|"
            i += 1
        return result

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valid):
        self._valid = valid

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if (len(self.valid) == 0 and not self.win()):
            winner = 'Ninguno'
        return winner

    def win(self):
        if(self.board['1.1'] == self.board['1.2'] == self.board['1.3']):
            return True
        if(self.board['2.1'] == self.board['2.2'] == self.board['2.3']):
            return True
        if(self.board['1.1'] == self.board['2.2'] == self.board['3.3']):
            return True
        if(self.board['1.3'] == self.board['2.2'] == self.board['3.1']):
            return True
        if(self.board['1.1'] == self.board['2.1'] == self.board['3.1']):
            return True
        if(self.board['1.2'] == self.board['2.2'] == self.board['3.2']):
            return True
        if(self.board['1.3'] == self.board['2.3'] == self.board['3.3']):
            return True
        return False

    def input_position(self):
        while True:
            valor = input("Ingrese la posicion deseada => ")
            if(valor in self.valid):
                self.valid.remove(valor)
                return valor
            print("El valor ingresado es incorrecto")


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
