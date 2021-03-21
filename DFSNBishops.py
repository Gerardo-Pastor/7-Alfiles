
def DFSNBishops(n):
      InitialBoard = [ [ '-' for i in range(n) ] for j in range(n) ]
      BoardStack = []
      Boards = []
      BoardStack.append(InitialBoard)
      while(len(BoardStack) != 0):
         CurrentBoard = BoardStack.pop()
         Children = getChildrenBoards(CurrentBoard)
         if(len(Children) == 0): 
            if(len(Boards) == 0):
                Boards.append(CurrentBoard)
            else:
                if(getNumberOfBishops(CurrentBoard) > getNumberOfBishops(Boards[-1])):
                    Boards.pop()
                    Boards.append(CurrentBoard)
                elif (getNumberOfBishops(CurrentBoard) == getNumberOfBishops(Boards[-1])):
                    Boards.append(CurrentBoard)
	 else:
	    for child in Children:
                BoardStack.append(child)

