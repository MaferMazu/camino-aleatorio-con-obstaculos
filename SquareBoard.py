class SquareBoard():
    def __init__(self,size):
        self.board = [[ 0 for i in range(size)] for j in range(size)]

    def fillboard(self,mylist):
        for coord in mylist:
            try:
                if coord[0]<0 or coord[1]<0 or coord[0]>len(self.board)-1 or coord[1]>len(self.board)-1:
                    raise IndexError("Tienes que agregar coordenadas válidas. Nota: los índices empiezan en 0.")
                else:
                    self.board[coord[0]][coord[1]]=1
            except IndexError as ie:
                print(ie)

    def __len__(self):
        return len(self.board)

    def isFull(self,pos0,pos1):
        return self.board[pos0][pos1]==1

    def __str__(self):
        inverted = [[ 0 for i in range(len(self.board))] for j in range(len(self.board))]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 1:
                    inverted[len(self.board)-j-1][i]=1

        mystr=''
        for i in inverted:
            for j in i:
                if j == 0:
                    mystr=mystr+'|   '
                elif j == 1:
                    mystr=mystr+'| x '
            mystr=mystr+'|\n'
        
        return mystr

if __name__ == "__main__":
    board = SquareBoard(5)
    board.fillboard([[0,1],[1,1],[2,1],[1,3],[1,4],[3,3],[4,3]])
    print(board)
