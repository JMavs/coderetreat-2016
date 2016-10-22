class Hiker:
    def __init__(self, fila, columna):
        self.array = []
        for i in range(0, fila):
            temp = []
            self.array.append(temp)
            for j in range(0, columna):
                temp.append(0)


    def add_cells(cells_array):
        for item in cells_array:
            self.array[item[0]][item[1]] = 1

    def count_alives():
        alive = 0
        for i in self.array:
            for j in i:
                if j == 1:
                    alive += 1
        return alive

    def answer(self):
        return 6 * 9
