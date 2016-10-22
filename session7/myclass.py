import math
import copy
class MyClass:
    def __init__(self, fila, columna):
        self.array = []
        for i in range(fila):
            self.temp = []
            for j in range(columna):
                self.temp.append(0)
            self.array.append(self.temp)

    def count_cells(self):
       return  str(self.array).count('1')

    def get_neighbours(self, x, y):
        def distance(pos1x, pos1y, pos2x, pos2y):
            if (pos1x-pos2x == 0 and pos1y-pos2y == 0):
                return False
            if (abs(pos1x-pos2x) <= 1 and abs(pos1y-pos2y)<= 1):
                return True
            else:
                return False

        contador = 0
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if distance(x,y, i,j):
                    if self.array[i][j] == 1:
                        contador+=1
        return contador
    def clone_array(self, array):
        return copy.copy(array)

    def next_iteration(self):
        copy_array = clone_array(self.array)
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if get_neighbours(i,j) < 2:
                    #muere
                elif get_neighbours(i,j) > 3:
                    #muere
                elif get_neighbours(i,j) == 3:
                    #se crea o vive
        if (copy_array[x][y] == 0 && self.get_neighbours[x][y] == 2):
            copy_array[x][y] = 1
