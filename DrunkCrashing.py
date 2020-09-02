import random
import SquareBoard

class DrunkCrashing:
    def __init__(self,position,board):
        self.init_position=position
        self.position=position
        self.collide=0
        self.board=board

    def clearcollide(self):
        self.collide=0

    def clearposition(self):
        self.position=self.init_position

    def dist(self):
        x = self.init_position[0] - self.position[0]
        y = self.init_position[1] - self.position[1]
        return ((x**2)+(y**2))**0.5
    
    def move(self):
        myrandom = random.choice(["left","right","up","down"])
        if myrandom == "left":
            if self.position[0]==0:
                self.collide+=1
            else:
                if self.board.isFull(self.position[0]-1,self.position[1]):
                    self.collide+=1
                else:
                    self.position[0]-=1

        elif myrandom == "right":
            if self.position[0]==len(self.board)-1:
                self.collide+=1
            else:
                if self.board.isFull(self.position[0]+1,self.position[1]):
                    self.collide+=1
                else:
                    self.position[0]+=1

        elif myrandom == "up":
            if self.position[1]==len(self.board)-1:
                self.collide+=1
            else:
                if self.board.isFull(self.position[0],self.position[1]+1):
                    self.collide+=1
                else:
                    self.position[1]+=1
        elif myrandom == "down":
            if self.position[1]==0:
                self.collide+=1
            else:
                if self.board.isFull(self.position[0],self.position[1]-1):
                    self.collide+=1
                else:
                    self.position[1]-=1