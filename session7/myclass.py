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
