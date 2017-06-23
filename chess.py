import sys

def printTable(coordX, coordY, pieces):
   currCoorX = 0
   currCoorY = 0
   Line = ""
   positions = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I', 9:'J', 10:'K', 11:'L', 12:'M'}

   while currCoorY < coordY:
       currCoorX = 0
       Line = ""
       if currCoorY == 0:
           while currCoorX < coordX:
               if (currCoorX + 1) % 3 == 1:
                   Line = Line + " "
               if (currCoorX + 1) % 3 == 2:
                   Line = Line + str((currCoorX/3) + 1)
               else:
                   Line = Line + "_"
               currCoorX = currCoorX + 1
           print Line

       currCoorX = 0
       Line = ""
       while currCoorX < coordX:
           piecePut = False
           if currCoorX % 3 == 0:
               Line = Line + "|"
           if (currCoorX + 1,currCoorY) in pieces.keys():
               Line = Line + " " + str(pieces[(currCoorX + 1,currCoorY)])
               piecePut = True
           else:
               if ((currCoorY % 3 == 1) and piecePut == False) or (currCoorY % 3 == 0):  
                   if (currCoorX + 1) % 3 == 1:
                       Line = Line + "   "

               if currCoorY % 3 == 2:
                   Line = Line + "_"

           if currCoorX == (coordX - 1):
               Line = Line + "|"
               if currCoorY % 3 == 1:
                   Line = Line + positions[(currCoorY/3)]

           currCoorX = currCoorX + 1

       print Line
       currCoorY = currCoorY + 1

def choosePiece(turn, coords, pieces):
    if turn == 'W':
        print "turn for white player, choose piece to move (V H):"
    else:
        print "turn for black player, choose piece to move (V H):"
    position = str(sys.stdin.readline())
    position = position.split(' ')
    if ((((int(position[1])-1)*3) +1), (int(coords[position[0]])*3)+1) in pieces.keys():
        piece = pieces[(((int(position[1])*3) -2), (int(coords[position[0]])*3)+1)]
        if piece[1] == turn:
            return position
        else:
            print "choose one of your pieces"
            return 0
    else:
        print "wrong position"
        return 0

print "chess app"
print "------------------------------"
coordXor = 8
coordYor = 8

coordX = coordXor * 3
coordY = coordYor * 3

coords = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12}
pieces = {(1,1):'TB', (4,1):'HB', (7,1):'BB', (10,1):'QB', (13,1):'KB', (16,1):'BB', (19,1): 'HB', (22,1):'TB',
          (1,4):'PB', (4,4):'PB', (7,4):'PB', (10,4):'PB', (13,4):'PB', (16,4):'PB', (19,4): 'PB', (22,4):'PB',
          (1,(coordY - 5)):'PW', (4,(coordY - 5)):'PW', (7,(coordY - 5)):'PW', (10,(coordY - 5)):'PW', (13,(coordY - 5)):'PW', (16,(coordY - 5)):'PW', (19,(coordY - 5)): 'PW', (22,(coordY - 5)):'PW',
          (1,(coordY - 2)):'TW', (4,(coordY - 2)):'HW', (7,(coordY - 2)):'BW', (10,(coordY - 2)):'QW', (13,(coordY - 2)):'KW', (16,(coordY - 2)):'BW', (19,(coordY - 2)): 'HW', (22,(coordY - 2)):'TW'}
printTable(coordX, coordY, pieces)
turn = 'W'
while 1 == 1:
    position = 0
    while position == 0:
        position = choosePiece(turn, coords, pieces)
        piece = pieces[(((int(position[1])*3) -2), (int(coords[position[0]])*3)+1)]

    corrMov = False
    while corrMov == False:
        rechoosePos = False
        print "choose position to move (V H):"
        position2 = str(sys.stdin.readline())
        position2 = position2.split(' ')
        if not ((position2[0] == position[0]) and (int(position2[1]) == int(position[1]))):
            if (int(position2[1]) > 0) and (int(position2[1]) <= coordXor):
                if piece[0] == 'P':
                    if turn == 'W':
                        if (int(position2[1]) == int(position[1])) and (int(coords[position2[0]]) == int(coords[position[0]]) - 1):     #forward move
                            if not (((int(position2[1])-1)*3) +1, (int(coords[position2[0]])*3)+1) in pieces.keys():
                                pieces[(((int(position2[1])-1)*3) +1, (int(coords[position2[0]])*3)+1)] = piece
                                del pieces[(((int(position[1])-1)*3) +1, (int(coords[position[0]])*3)+1)]
                                corrMov = True
                            else:
                                if not list(pieces[(((int(position2[1])*3) -2), (int(coords[position2[0]])*3)+1)])[1] == turn:
                                    pieces[(((int(position2[1])-1)*3) +1, (int(coords[position2[0]])*3)+1)] = piece
                                    del pieces[(((int(position[1])-1)*3) +1, (int(coords[position[0]])*3)+1)]
                                    corrMov = True
                                else:
                                    print "Not a possible move"
                                    rechoosePos = True
                        if (int(position2[1]) == int(position[1]) - 1) and (int(coords[position2[0]]) == int(coords[position[0]]) - 1): #left  diagonal
                            pass
                        if (int(position2[1]) == int(position[1]) + 1) and (int(coords[position2[0]]) == int(coords[position[0]]) - 1): #right diagonal
                            pass
                        else:
                            print "Not a possible move"
                            rechoosePos = True
                    else:
                        if (int(position2[1]) == int(position[1])) and (int(coords[position2[0]]) == int(coords[position[0]]) + 1):
                            if not (((int(position2[1])*3) -2), (int(coords[position2[0]])*3)+1) in pieces.keys():
                                pieces[(((int(position2[1])-1)*3) +1, (int(coords[position2[0]])*3)+1)] = piece
                                del pieces[(((int(position[1])-1)*3) +1, (int(coords[position[0]])*3)+1)]
                                corrMov = True
                            else:
                                if not list(pieces[(((int(position2[1])*3) -2), (int(coords[position2[0]])*3)+1)])[1] == turn:
                                    pieces[(((int(position2[1])-1)*3) +1, (int(coords[position2[0]])*3)+1)] = piece
                                    del pieces[(((int(position[1])-1)*3) +1, (int(coords[position[0]])*3)+1)]
                                    corrMov = True
                                else:
                                    print "Not a possible move"
                                    rechoosePos = True
                        else:
                            print "Not a possible move"
                            rechoosePos = True
            else:
                print "Not a possible move"
                rechoosePos = True
        else:
            print "Not a possible move"
            rechoosePos = True
        if rechoosePos == True:
            position = 0
            while position == 0:
                position = choosePiece(turn, coords, pieces)
    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
    printTable(coordX, coordY, pieces)
