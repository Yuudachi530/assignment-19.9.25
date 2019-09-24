def ColumnNumberValid(ColumnNumber):
    Valid = False
    if ColumnNumber >= 1 and ColumnNumber <= 7:
        if Board[6, ColumnNumber] == BLANK:
            Valid = True
    return Valid

def ThisPlayerChoosesColumn():
    print("Player", ThisPlayer, "'s Turn")
    ColumnNumber = int(input('Enter a valid column number: '))
    while ColumnNumberValid(ColumnNumber) != True:
        ColumnNumber = int(input('Enter a valid column number: '))
    return ColumnNumber

def FindNextFreePositionInColumn(ValidColumn):
    ThisRow = 1
    while Board[ThisRow, ValidColumn] != BLANK:
        ThisRow = ThisRow + 1
    return ThisRow

#InitialiseBoard
Board = {}
BLANK = 'EMPTY'
for Row in range(1, 6 + 1):
    for Column in range(1, 7 + 1):
        Board[Row, Column] = BLANK  
        
#SetupGame
ThisPlayer = '  O  '
GameFinished = False

#OutputBoard
for Row in range(6, 0, -1):
    for Column in range(1, 7 + 1):
        print(Board[Row,Column], end = '')
        print(' ', end = '')
    print()
    
while GameFinished == False:
    #ThisPlayerMakesMove
    ValidColumn = ThisPlayerChoosesColumn()
    ValidRow = FindNextFreePositionInColumn(ValidColumn)
    Board[ValidRow, ValidColumn] = ThisPlayer
    
    #OutputBoard
    print()
    for Row in range(6, 0, -1):
        for Column in range(1, 7 + 1):
            print(Board[Row,Column], end = '')
            print(' ', end = '')
        print()
    
    #CheckIfThisPlayerHasWon
    WinnerFound = False
    #CheckHorizontalLineInValidRow
    for i in range(1, 4 + 1):
        if Board[ValidRow, i] == ThisPlayer and Board[ValidRow, i + 1] == ThisPlayer and Board[ValidRow, i + 2] == ThisPlayer and Board[ValidRow, i + 3] == ThisPlayer:
            WinnerFound = True
    if WinnerFound == False:
        #CheckVerticalLineInValidColumn
        if ValidRow == 4 or ValidRow == 5 or ValidRow == 6:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow - 1, ValidColumn] == ThisPlayer and Board[ValidRow - 2, ValidColumn] == ThisPlayer and Board[ValidRow - 3, ValidColumn] == ThisPlayer:
                WinnerFound = True
    #CheckObliqueLineInValidColumn
    if WinnerFound == False:
        if ValidRow <= 4 and ValidColumn <= 3:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow + 1, ValidColumn + 1] == ThisPlayer and Board[ValidRow + 2, ValidColumn + 2] == ThisPlayer and Board[ValidRow  + 3, ValidColumn + 3] == ThisPlayer:
                WinnerFound = True
        if ValidRow <= 4 and ValidColumn >= 4:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow + 1, ValidColumn - 1] == ThisPlayer and Board[ValidRow + 2, ValidColumn - 2] == ThisPlayer and Board[ValidRow  + 3, ValidColumn - 3] == ThisPlayer:
                WinnerFound = True
        if ValidRow >= 4 and ValidColumn >= 4:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow - 1, ValidColumn - 1] == ThisPlayer and Board[ValidRow - 2, ValidColumn - 2] == ThisPlayer and Board[ValidRow  - 3, ValidColumn - 3] == ThisPlayer:
                WinnerFound = True
        if ValidRow >= 4 and ValidColumn <= 3:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow - 1, ValidColumn + 1] == ThisPlayer and Board[ValidRow - 2, ValidColumn + 2] == ThisPlayer and Board[ValidRow  - 3, ValidColumn + 3] == ThisPlayer:
                WinnerFound = True
    if WinnerFound == True:
        GameFinished = True
        print()
        print('GameOver,', ThisPlayer, 'is the winner')
    else:
        #CheckForFullBoard
        BlankFound = False
        ThisRow = 1
        while ThisRow <= 6 or BlankFound != True:
            ThisColumn = 1
            while ThisColumn <= 7 or BlankFound != True:
                if Board[ThisRow, ThisColumn] == BLANK:
                    BlankFound = True
                ThisColumn  = ThisColumn + 1
            ThisRow = ThisRow + 1
        if BlankFound == False:
            print('It is a draw')
            GameFinished = True
    
    if GameFinished == False:
        #SwapThisPlayer
        if ThisPlayer == '  O  ':
            ThisPlayer = '  X  '
        else:
            ThisPlayer = '  O  '

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    