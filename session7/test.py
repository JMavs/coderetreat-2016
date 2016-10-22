import myclass

def test_cells_created():
    t1 = myclass.MyClass(2,2)
    t1.array[0][0] = 1
    t1.array[1][0] = 1

    assert (t1.array[0][0]==1)

def test_count_cells():
    t1 = myclass.MyClass(2,2)
    t1.array[0][0] = 1
    t1.array[1][0] = 1

    assert (t1.count_cells()== 2)


