
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
                if(getNomberOfBishops(CurrentBoard) > getNomberOfBishops(Boards[-1]))
                    Boards.pop()
                    Boards.append(CurrentBoard)
                elif (getNomberOfBishops(CurrentBoard) == getNomberOfBishops(Boards[-1]))
                    Boards.append(CurrentBoard)
	 else:
	    for child in Children:
                BoardStack.append(child)

