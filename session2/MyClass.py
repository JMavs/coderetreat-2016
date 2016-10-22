class MyClass:
    def __init__(self, fil, columna):

        def add_level(columna):
            self.a1 = []
            for i in range(0, columna):
                self.a1.append(0)
            print self.a1
            return self.a1

        self.array = []
        for i in range(0, fil):
            self.fila = add_level(columna)
            self.array.append(self.fila)

    def addCell(self, fila, columna):
        self.array[fila][columna] = 1

    def count(self):
        return str(self.array).count('1')
