size_x = 8
size_y = 8

board_delimiter = '#'

pieces = {'K': 'King',
          'Q': 'Queen',
          'H': 'Horse',
          'T': 'Tower',
          'B': 'Bishop',
          'P': 'Pawn'}

messages = {'CHOOSE_PIECE': "Turn for {} player, choose piece to move (V H):",
            'CHOOSE_MOVE': "Choose position to move (V H):",
            'MOVE_DONE': "Player {} has moved {} from {} to {}",
            'OWN_ATTACK': "We cannot attack our own piece",
            'WRONG_PIECE': "You must choose one of your pieces",
            'NO_MOVEMENT': "No possible movement to get from source to target",
            'WRONG_MOVEMENT': 'Wrong movement',
            'WRONG_POSITION': 'Wrong position',
            'PLAYER_WIN': 'Player {} wins!',
            'PROMOTE_PAWN': 'To which piece do you want to promote your pawn?\n1)Queen\n2)Horse\n3)Tower\n4)Bishop'}

letters = 'abcdefghijklmnopqrstuvwxyz'
