import random
class puzzle:
    def __init__(self):
        self.matriz = [
                  [2,8,3],
                  [1,6,4],
                  [7,0,5]]
        
    def printm(self, matriz):
        for i in range(3):
            for j in range(3):
                print(self.matriz[i][j], ' ', end='')
            print('\n')
    
    def CostFunction(self, matriz):
        errors = 0
        if matriz[0][0] != 1:
            errors+=1
        if matriz[0][1] != 2:
            errors+=1
        if matriz[0][2] != 3:
            errors+=1
        if matriz[1][2] != 4:
            errors+=1
        if matriz[2][2] != 5:
            errors+=1
        if matriz[2][1] != 6:
            errors+=1
        if matriz[2][0] != 7:
            errors+=1
        if matriz[1][0] != 8:
            errors+=1
        return errors
    
    def isNextTo(self, val):
        i = 0
        j = 0
        for _ in range(len(self.matriz)):
            for k in range(len(self.matriz)):
                if self.matriz[_][k]==val:
                    i = _
                    j = k
                    break
        
        if self.matriz[i-1][j]==0 and i-1 >= 0:
            #return (i-1,j)
            return True
        if i + 1 <= 2:
            if self.matriz[i+1][j]==0:
                return True
        if self.matriz[i][j-1]==0 and j - 1 >= 0:
            #return (i,j-1)
            return True
        if j + 1 <= 2:
            if self.matriz[i][j+1]==0:
                return True
        return False
    
    def getZeroIndex(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j]==0:
                    return i, j
    
    def swap(self, matriz):
        i = random.randint(0,2)
        j = random.randint(0,2)
        ii,jj = self.getZeroIndex()
        
        if (self.isNextTo(self.matriz[i][j])):
            matriz[i][j], matriz[ii][jj] = matriz[ii][jj], matriz[i][j]
            return matriz
        else:
            return self.swap(matriz)

    def HillClimbing(self, matriz):
        score = self.CostFunction(matriz)
        
        if score <= 0:
            print("Solucionado!")
            self.printm(matriz)
            return matriz
        
        while score >= 0:
            actual = matriz
            self.swap(actual)
            nuevo_score = self.CostFunction(actual)
            
            if nuevo_score <= 0:
                print("Solucionado!")
                print("--------")
                self.printm(actual)
                return actual
            elif nuevo_score < score:
                score = nuevo_score

mat = puzzle()
mat.HillClimbing(mat.matriz)
print("--------")
